import os
import time
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

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY") 
RESOURCE_ENDPOINT = os.getenv("OPENAI_API_BASE") 
DEPLOYMENT_NAME = os.getenv("ADA_DEPLOYMENT_NAME")

openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01"

url = openai.api_base + "/openai/deployments?api-version=2022-12-01" 

r = requests.get(url, headers={"api-key": API_KEY})

def get_embedding_with_delay(x):
    time.sleep(5)  # Add a 5-second delay
    return get_embedding(x, engine=DEPLOYMENT_NAME)

def vectorize_data(data_filepath):     
    df=pd.read_json(data_filepath)

    tokenizer = tiktoken.get_encoding("cl100k_base")
    df['n_tokens'] = df["instruction"].apply(lambda x: len(tokenizer.encode(x)))
    df = df[df.n_tokens<8192]

    df['ada_v2'] = df["instruction"].apply(get_embedding_with_delay)
    
    return df

def search_dataset(df, user_query, top_n=1, to_print=False):
    embedding = get_embedding(
        user_query,
        engine=DEPLOYMENT_NAME # engine should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model
    )
    df["similarities"] = df['ada_v2'].apply(eval).apply(np.array).apply(lambda x: cosine_similarity(x, embedding))

    res = (
        df.sort_values("similarities", ascending=False)
        .head(top_n)
    )
    if to_print:
        print(res)
    return res


