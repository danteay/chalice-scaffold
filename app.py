"""
App entrypoint
"""

from chalice import Chalice

from chalicelib.config import CONFIG
from chalicelib.commons.logger import init_logger, LOGGER as logger
from chalicelib.commons.http import response, error_response

from chalicelib.handlers.ping import handle

init_logger()

app = Chalice(app_name=CONFIG['app_name'], configure_logs=False)


@app.route('/ping', methods=['GET'])
def ping():
    try:
        return response(body=handle())
    except Exception as err:
        logger.error("ping handler error", err)
        return error_response(err)
