import requests
from config.logger import logger


def fetch_data(url: str) -> str | None:
    """
    Fetch data from the given URL and log the result.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict or str: The response data, parsed as JSON if possible, or raw text.
    """
    try:
        logger.debug(f"Sending GET request to URL: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.text
        logger.info("Data successfully fetched")
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")
        return None
