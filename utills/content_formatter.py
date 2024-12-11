
import re
from datetime import datetime



def normalize_datetime(datetime_str) -> str: 
    input_format = "%Y-%m-%dT%H:%M:%S%z" 

    # Parse the datetime string to a datetime object
    try:
        dt_object = datetime.strptime(datetime_str, input_format)

        # Format the datetime object to the desired output format
        normalized_datetime = dt_object.strftime("%Y/%m/%d %H:%M")
        return normalized_datetime

    except ValueError:
        return "Invalid datetime format"


def normalize_content(content)->str:
    # Remove all HTML tags and their attributes (e.g., <a href="...">, <span class="...">, etc.)
    content = re.sub(r'<[^>]+>', '', content)

    # Replace newlines and tabs with spaces
    content = re.sub(r'[\n\t]', ' ', content)

    # Replace multiple spaces with a single space
    content = re.sub(r'\s+', ' ', content).strip()

    return content