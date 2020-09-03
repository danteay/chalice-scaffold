"""
HTTP API authorizer middleware
"""

from chalice import AuthResponse
from chalicelib.config import CONFIG


def raw_api_key(request):
    """
    Authorize raw token from Authorization header
    :param request: request data
    :return: Authorization response
    """

    token = request.token

    if token == CONFIG["api_key"]:
        return AuthResponse(["*"], principal_id=CONFIG["app_name"])

    return AuthResponse([], CONFIG["APP_NAME"])
