import datetime as dt
import json
import logging
import logging.config
from typing import override

logger = logging.getLogger(__name__)

def setup_logging():
    logging.config.dictConfig(json.load(open("logging_configs/stderr_config.json")))

def main():
    setup_logging()
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.info("This is an info message")

if __name__ == "__main__":
    main()