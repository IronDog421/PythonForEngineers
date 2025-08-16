import atexit
import datetime as dt
import json
import logging
import logging.config
from typing import override

logger = logging.getLogger(__name__)

def setup_logging():
    logging.config.dictConfig(json.load(open("logging_configs/queued_json_config.json")))
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

def main():
    setup_logging()
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.info("This is an info message")

if __name__ == "__main__":
    main()