"""Logging bootstrapping"""

import logging

from elasticlogger import Logger
from chalicelib.config import CONFIG

LOGGER = Logger(CONFIG["app_name"], level=logging.DEBUG)
LOGGER.enable_sentry(endpoint=CONFIG["sentry"]["url"])
LOGGER.enable_elastic(endpoint=CONFIG["elastic"]["url"], index=CONFIG["elastic"]["index"])


def init_logger():
    """
    Bootstrap logger configuration options
    """

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    LOGGER.logger.propagate = False
