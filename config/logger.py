import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("data-extractor")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = RotatingFileHandler(
    "logs/data_extractor.log", maxBytes=5 * 1024 * 1024, backupCount=5
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.propagate = False
