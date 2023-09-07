import os
import json
import requests
import numpy as np
from utils.common_utils import extract_folder_and_name_from_path
from utils.data import vectorize_data

data_folder, data_filename = extract_folder_and_name_from_path(
    "Data_FILE", "./data/data.json"
)

data_folder, embedding_filename = extract_folder_and_name_from_path(
    "Data_FILE", "./data/data-embeddings.csv"
)

data_filepath = os.path.join(os.getcwd(), os.path.join(f"{data_folder}", f"{data_filename}"))
embedding_filepath = os.path.join(os.getcwd(), os.path.join(f"{data_folder}", f"{embedding_filename}"))

df = vectorize_data(data_filepath)
df.to_csv(embedding_filepath, sep=',', header='true')
