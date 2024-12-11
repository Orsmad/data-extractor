
import re

from config.logger import logger
from models.params import HtmlExtractionParams
from models.post import Post

from utills.content_formatter import normalize_content, normalize_datetime


def extract_data_from_html(html:str, params:HtmlExtractionParams)  -> list[Post]:
    logger.debug("Starting data extraction from fetched html")
    post_num_match = re.findall(
        params.post_num_pattern, html, re.DOTALL | re.IGNORECASE)

    num_of_posts = int(post_num_match[-1]) if post_num_match else 0
    content_match = re.findall(params.content_regex, html, re.DOTALL)
    datetime_match = re.findall(params.datetime_regex, html)
    title_match = re.findall(params.title_regex, html, re.DOTALL)
    author_match = re.findall(params.author_regex, html, re.DOTALL)

    result_arr:list[Post] = []
    logger.info(f'Found {num_of_posts} posts, validating data....')
    for i in range(num_of_posts):
        result = {
            'title': normalize_content(title_match[i]) if i < len(title_match) else '',
            'text': normalize_content(content_match[i]) if i < len(content_match) else '',
            'published': normalize_datetime(datetime_match[i]) if i < len(datetime_match) else '',
            'author': author_match[i] if i < len(author_match) else ''
        }
        try:
            validated_result = Post(**result)
            result_arr.append(validated_result)
        except ValueError as e:
            logger.error(f"Validation failed for result {result}: {e}")
    logger.info(f'Validated {len(result_arr)} posts / {num_of_posts}')
    return result_arr


def extract_body_div(html_content, body_regex=r'<body.*?>(.*?)</body>') -> str :
    match = re.search(body_regex, html_content, re.DOTALL)
    if match:
        body_content = match.group(1)
        return body_content
    return ""
