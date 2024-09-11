import os
import requests
from dotenv import load_dotenv

"""
This module provides functions to interact with backend services and analyze review sentiments.
"""

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    """
    Sends a GET request to the backend service.

    Args:
        endpoint (str): The API endpoint.
        **kwargs: Additional query parameters.

    Returns:
        dict: The JSON response from the backend service.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None

def analyze_review_sentiments(text):
    """
    Analyzes the sentiment of a given text using the sentiment analyzer service.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: The JSON response from the sentiment analyzer service.
    """
    request_url = f"{sentiment_analyzer_url}/analyze/{text}"
    print(request_url)

    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None

def post_review(data_dict):
    """
    Sends a POST request to insert a review into the backend service.

    Args:
        data_dict (dict): The review data to insert.

    Returns:
        dict: The JSON response from the backend service.
    """
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None
    