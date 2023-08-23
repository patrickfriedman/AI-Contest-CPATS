import glob
import os
from pathlib import Path
from typing import Any, List, Optional, Tuple

from langchain.chat_models import AzureChatOpenAI


def get_azure_chatbot(
    openai_api_key: Optional[str] = None,
    deployment_name: Optional[str] = None,
    openai_api_type: Optional[str] = None,
    openai_api_base: Optional[str] = None,
    openai_api_version: Optional[str] = None,
    **kwargs: Any,
) -> AzureChatOpenAI:
    """
    Create an instance of AzureChatOpenAI.
    Usage:
        azure_chat_openai = get_azure_chatbot()
    Args:
        openai_api_key: The OpenAI API key. If not provided, the method will try to get it from the
            environment variable OPENAI_API_KEY.
        deployment_name: The name of the deployment. If not provided, the method will try to get it
            from the environment variable DEPLOYMENT_NAME.
        openai_api_type: The type of the OpenAI API. If not provided, the method will try to get it
            from the environment variable OPENAI_API_TYPE.
        openai_api_base: The base of the OpenAI API. If not provided, the method will try to get it
        from the environment variable OPENAI_API_BASE.
        openai_api_version: The version of the OpenAI API. If not provided, the method will try to
        get it from the environment variable OPENAI_API_VERSION.
        kwargs: Other optional parameters.
    Returns:
        An instance of AzureChatOpenAI.
    """

    openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        raise ValueError(
            "openai_api_key is required. Please provide it as an argument or set the environment"
            " variable OPENAI_API_KEY."
        )

    deployment_name = deployment_name or os.getenv("DEPLOYMENT_NAME")
    if not deployment_name:
        raise ValueError(
            "deployment_name is required. Please provide it as an argument or set the environment"
            " variable DEPLOYMENT_NAME."
        )

    openai_api_type = openai_api_type or os.getenv("OPENAI_API_TYPE") or "azure"

    openai_api_base = openai_api_base or os.getenv("OPENAI_API_BASE")
    if not openai_api_base:
        raise ValueError(
            "openai_api_base is required. Please provide it as an argument or set the environment"
            " variable OPENAI_API_BASE."
        )

    openai_api_version = openai_api_version or os.getenv("OPENAI_API_VERSION")
    if not openai_api_version:
        raise ValueError(
            "openai_api_version is required. Please provide it as an argument or set the environment"
            " variable OPENAI_API_VERSION."
        )

    return AzureChatOpenAI(
        deployment_name=deployment_name,
        openai_api_type=openai_api_type,
        openai_api_base=openai_api_base,
        openai_api_version=openai_api_version,
        openai_api_key=openai_api_key,
        **kwargs,
    )


def read_files_from_directory(directory_path: str) -> List[Tuple[str, str]]:
    """
    This function reads all the .txt files from the specified directory path,
    and returns a list of tuples, where each tuple contains the filename and its corresponding content.

    Args:
        directory_path (str): The path to the directory containing the .txt files.

    Returns:
        file_content_list (list): A list of tuples, where each tuple has the filename as the first element and
                                  the corresponding content as the second element.
    """

    file_content_list = []
    txt_files = glob.glob(os.path.join(directory_path, "*.txt"))

    for txt_file in txt_files:
        with open(txt_file, "r", encoding="utf-8") as file:
            data = file.read()
            # Add a tuple (filename, content) to the list
            file_content_list.append((os.path.basename(txt_file), data))

    return file_content_list


def extract_folder_and_name_from_path(source_var: str, default_path: str) -> (str, str):
    """
    Extract and return the folder path and file name from a given source variable (can be an environment variable or regular variable).

    Args:
    - source_var (str): The name of the environment variable to fetch or directly a string path.
    - default_path (str): The default path to use if the environment variable is not set or the source_var doesn't contain a valid path.

    Returns:
    - folder_path (str): The folder path extracted from the provided source as a string.
    - file_name (str): The file name extracted from the provided source.
    """
    # If source_var is an environment variable name, fetch its value; otherwise use it directly as a path.
    file_path = os.environ.get(source_var, None)
    if not file_path:
        file_path = default_path
    folder_path = str(Path(file_path).parent)
    file_name = Path(file_path).name
    return folder_path, file_name
