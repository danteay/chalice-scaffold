"""
Ping routes
"""

from chalice import Blueprint

from chalicelib.commons.http import response, error_response
from chalicelib.commons.logger import LOGGER as logger
from chalicelib.handlers.ping import handle

ping_router = Blueprint(__name__)


@ping_router.route("/ping", methods=["GET"])
def ping():
    """
    Ping rote handler
    :return: Chalice Response
    """

    try:
        return response(body=handle())
    except Exception as err:
        logger.error("ping handler error", err)
        return error_response(err)
