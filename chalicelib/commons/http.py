"""
Http common functions
"""

import http.client

from chalice import Response
from chalicelib.commons.errors import HandlerError
from chalicelib.commons.logger import LOGGER as logger


def response(code=200, body=None, error=None, cors=False):
    """
    Http lambda response formatting
    :param code: (int) Http response code
    :param body: (dict) Response json body
    :param error: (Exception|dict|str) Possible error on response body
    :param cors: (bool) enable cors support
    :return: (dict)
    """

    if not body:
        body = {}

    if error is not None:
        if isinstance(error, HandlerError):
            body["errors"] = error.get_message()
        else:
            body["errors"] = get_error_from_code(code)
            body["message"] = str(error).replace("\n", "")

    logger.field("res", body)

    if "errors" in body and body["errors"] is not None:
        logger.error("handled request", error=body["errors"])
    else:
        logger.info("handled request")

    headers = None

    if cors:
        headers = cors_headers()

    return Response(body=body, headers=headers, status_code=code)


def get_error_from_code(code):
    """
    Transform http status code into a standard error message
    :param code: HTTP status code
    """
    error = http.client.responses[code]
    error = error.lower().replace(" ", "-")
    return error


def cors_headers():
    """
    Add cors headers to response headers
    :return: new headers dict
    """

    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
    }


def error_response(error, cors=False):
    """
    Identify the error type an respond with the proper error
    :param error: Handled error
    :param cors: enable cors support
    :returns: Api gateway response format
    """

    if isinstance(error, HandlerError):
        return response(code=error.get_code(), error=error)

    return response(code=500, error=error, cors=cors)
