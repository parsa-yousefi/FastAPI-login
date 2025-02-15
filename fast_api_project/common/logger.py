import logging
import os
from logging.handlers import RotatingFileHandler


# Create log directory if it doesn't exist
log_dir = "../../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def get_logger(endpoint_name: str) -> logging.Logger:
    """
    Creates a logger for the given endpoint. The logs will be saved in `logs/{endpoint_name}_log.out.
    """
    logger = logging.getLogger(endpoint_name)
    logger.setLevel(logging.INFO)

    # Create a rotation file handler to handle log rotation ( max size 10MB )
    log_file = os.path.join(log_dir, f"{endpoint_name}.log")
    handler = RotatingFileHandler(log_file, maxBytes=10**7, backupCount=3)
    handler.setLevel(logging.INFO)

    # Create a formatter and attach it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger
