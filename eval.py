import argparse
import importlib.util
import os
import unittest

import pandas as pd

from utils.log import logger

# Initialize ArgumentParser
parser = argparse.ArgumentParser(description="Evaluation script for solutions")
parser.add_argument(
    "--solution-path",
    type=str,
    default="./solutions/20230726_174815.csv",
    help="Path to the solution file",
)
args = parser.parse_args()

# Read the contents of solutions.csv
df = pd.read_csv(args.solution_path)

# Convert the DataFrame into a dictionary where the keys are the 'Question file' and the values are 'Solution code'
solutions = df.set_index("Question file")["Solution code"].to_dict()

# List all .py files in the eval directory
test_files = [f for f in os.listdir("eval") if f.endswith(".py")]

# For each test file
for test_file in test_files:
    logger.info("In " + str(test_file))
    # Get the corresponding solution code from the solutions dictionary
    # Note: We replace the .py extension with .txt to match with the question file names in solutions.csv
    solution_code = solutions.get(test_file.replace(".py", ".txt"), None)

    if solution_code is None:
        logger.warning(f"No solution found for {test_file}")
        continue

    # Create a new module spec and module
    spec = importlib.util.spec_from_file_location(
        test_file, os.path.join("eval", test_file)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Insert the solution code into the module
    exec(solution_code, module.__dict__)

    # Run the tests
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    unittest.TextTestRunner().run(suite)
