from config.logger import logger
from models.post import Post
from services.services import fetch_data
from utills.uttils import extract_data_from_html, extract_body_div
from utills.file_operations import write_posts_to_file

from config.configs import extraction_configs


def extract_and_write_data(url, params, output_file):
    fetched_page: str = fetch_data(url)
    body_div: str = extract_body_div(fetched_page)
    if not body_div:
        logger.error("Couldn't find html body")
        return
    extracted_data: list[Post] = extract_data_from_html(body_div, params)
    write_posts_to_file(extracted_data, output_file)


def data_extractor():
    logger.info("Data_extractor starting...")
    for config in extraction_configs:
        extract_and_write_data(config["url"], config["params"], config["output_file"])
    logger.info("Done!")


if __name__ == "__main__":
    data_extractor()
