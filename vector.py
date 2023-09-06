import os
import requests
from dotenv import load_dotenv
import openai
import re
import sys
from num2words import num2words
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import tiktoken
from utils.common_utils import (extract_folder_and_name_from_path,
                                read_files_from_directory)

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY") 
RESOURCE_ENDPOINT = os.getenv("OPENAI_API_BASE") 
DEPLOYMENT_NAME = os.getenv("ADA_DEPLOYMENT_NAME")

def vectorize_data(data_filepath): 
    openai.api_type = "azure"
    openai.api_key = API_KEY
    openai.api_base = RESOURCE_ENDPOINT
    openai.api_version = "2022-12-01"

    url = openai.api_base + "/openai/deployments?api-version=2022-12-01" 

    r = requests.get(url, headers={"api-key": API_KEY})
    
    df=pd.read_json(data_filepath)

    tokenizer = tiktoken.get_encoding("cl100k_base")
    df['n_tokens'] = df["instruction"].apply(lambda x: len(tokenizer.encode(x)))
    df = df[df.n_tokens<8192]
    df['ada_v2'] = df["instruction"].apply(lambda x : get_embedding(x, engine = DEPLOYMENT_NAME))
    return df

dataset_folder, dataset_filename = extract_folder_and_name_from_path(
    "Data_FILE", "./data/data.json"
)
vec_dataset_folder, vec_dataset_filename = extract_folder_and_name_from_path(
    "Data_FILE", "./data/data.csv"
)

dataset_filepath = os.path.join(os.getcwd(), os.path.join(f"{dataset_folder}", f"{dataset_filename}"))
vec_dataset_filepath = os.path.join(os.getcwd(), os.path.join(f"{vec_dataset_folder}", f"{vec_dataset_filename}"))
df = vectorize_data(dataset_filepath)
df.T.to_csv(vec_dataset_filepath)