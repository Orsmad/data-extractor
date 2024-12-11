import json
from config.logger import logger
from models.post import Post

def write_posts_to_file(data:list[Post], file_path) -> None:
    logger.debug(f'Writing results to {file_path}')
    data_dict = [post.model_dump() for post in data]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)
    logger.debug(f'Finished writing results to file')
