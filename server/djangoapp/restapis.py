import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("backend_url", "http://localhost:3030").rstrip("/")
SENTIMENT_ANALYZER_URL = os.getenv(
    "sentiment_analyzer_url",
    "http://localhost:5050",
).rstrip("/")


def get_request(endpoint: str, **kwargs: str) -> Optional[Dict[str, Any]]:
    """Send a GET request to the backend service."""
    request_url = f"{BACKEND_URL}/{endpoint.lstrip('/')}"
    print(f"GET from {request_url} with params {kwargs}")

    try:
        response = requests.get(
            request_url,
            params=kwargs,
            timeout=5,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"Network exception occurred: {exc}")
        return None


def analyze_review_sentiments(text: str) -> Optional[Dict[str, Any]]:
    """Send review text to sentiment analyzer service."""
    request_url = f"{SENTIMENT_ANALYZER_URL}/analyze/{text}"
    print(f"Analyzing sentiment via {request_url}")

    try:
        response = requests.get(
            request_url,
            timeout=5,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"Network exception occurred: {exc}")
        return None


def post_review(data_dict: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Post a new review to backend service."""
    request_url = f"{BACKEND_URL}/insert_review"
    print(f"POST to {request_url}")

    try:
        response = requests.post(
            request_url,
            json=data_dict,
            timeout=5,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"Network exception occurred: {exc}")
        return None
