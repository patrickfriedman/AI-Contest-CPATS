import os

import argparse
import logging
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

from utils.common_utils import (extract_folder_and_name_from_path,
                                read_files_from_directory)
from utils.log import logger
from utils.question_solver import QuestionSolver
from utils.data import search_dataset

from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# Load .env file
load_dotenv()

# Usage
question_folder, question_filename = extract_folder_and_name_from_path(
    "Question_FILE", "./questions/question.txt"
)
solution_folder, solution_filename = extract_folder_and_name_from_path(
    "Solution_FILE", "./solutions/solution.py"
)
data_folder, test_filename = extract_folder_and_name_from_path(
    "Data_FILE", "./data/data-120k-embeddings.csv"
)
parser = argparse.ArgumentParser(
    description="A script that accepts a question path and a solution save path"
)
parser.add_argument(
    "--question-path",
    default=question_folder,
    help="The path to the questions (folder)",
)
parser.add_argument(
    "--solution-save-path",
    default=solution_folder,
    help="The path to save the solution",
)
parser.add_argument(
    "--data-save-path",
    default=data_folder,
    help="Data set for prompt enrichment",
)
parser.add_argument(
    "--data-file-name",
    default="",
    help="Data set file for prompt enrichment",
)
parser.add_argument(
    "--message",
    help="Will be one of the following: SyntaxError or test_cases_count: 70, wrong_answer_count: 0, time_limit_count: 0.",
)

parser.add_argument("--debug", action="store_true", help="Set log level to DEBUG")
args = parser.parse_args()

if args.debug:
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)

if __name__ == "__main__":

    embedding_filename = args.data_file_name

    print(f"Embedding file name: {embedding_filename}")

    # Initialize an empty DataFrame with the columns 'Question file', 'code' and 'ChatGPT_thought'
    df = pd.DataFrame(columns=["Question file", "Solution code", "ChatGPT thought"])

    try:
        # Get vectorized data for prompt enrichment
        questions = read_files_from_directory(args.question_path)
        if len(questions) > 1:
            logger.warning(
                "According to the requirements of the competition server, we anticipate that there should only be"
                " one question.txt present, which is root/questions/question.txt, but now we've detected multiple!"
            )

        for q in tqdm(questions):
            solver = QuestionSolver()
            # Search dataset for most similar data with question

            similar_dict = {
                "add_this_to_prompt": False,
                "similarities": "",
                "instruction": "",
                "input": "",
                "output":  ""
            }

            # Retrieve embedded data from csv file
            if embedding_filename != "":
                embedding_filepath = os.path.join(os.getcwd(), os.path.join(f"{data_folder}", f"{embedding_filename}"))
                additional_df = pd.read_csv(embedding_filepath, sep=',', encoding='utf-8')

                similar_df = search_dataset(additional_df, q[1])

                print(f"This is the similarity score: {similar_df['similarities'].iloc[0]}")
        
                if similar_df['similarities'].iloc[0] >= 0.80:
                    similar_dict = {
                        "add_this_to_prompt": True,
                        "similarities": similar_df['similarities'].iloc[0],
                        "instruction": similar_df['instruction'].iloc[0],
                        "input": similar_df['input'].iloc[0],
                        "output": similar_df['output'].iloc[0]
                    }

            with get_openai_callback() as cb: # gets cost of api call
                result = solver.solve(q[1], similar_dict)
                logger.debug("result:\n" + str(result))

                chatgpt_thought = result["thought"]
                solution_code = result["solution_code"]
                new_row = pd.DataFrame(
                    {
                        "Question file": [q[0]],
                        "Solution code": [solution_code],
                        "ChatGPT thought": [chatgpt_thought],
                    }
                )

                df = pd.concat([df, new_row], ignore_index=True)
                print("\n\n" + str(cb) + "\n\n")

        name = "sol"

        # Save DataFrame to CSV
        solution_detail_save_path = f"{args.solution_save_path}/{name}.csv"
        df.to_csv(solution_detail_save_path, index=False)
        logger.info(f"Solution detail have been saved to {solution_detail_save_path}")

        solution_save_path = f"{args.solution_save_path}/{solution_filename}"
        with open(solution_save_path, "w") as f:
            f.write(df.loc[0, "Solution code"])
            logger.info(f"Solution file have been saved to {solution_save_path}")
            if len(questions) > 1:
                logger.warning(
                    "The competition server expects us to handle one question at a time, "
                    "but now we have received multiple answers because there are multiple txt files "
                    f"under the ./questions folder. However, we will only save question from {questions[0][0]}"
                    " as solutions/solution.py and it will be scored by the competition server."
                )

    except Exception as e:
        logger.error(f"Exception:\n {str(e)} happened!", exc_info=True)