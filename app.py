"""
App entrypoint
"""

from chalice import Chalice

from chalicelib.config import CONFIG
from chalicelib.commons.logger import init_logger
from chalicelib.routes import ping_router

init_logger()

app = Chalice(app_name=CONFIG['app_name'], configure_logs=False)
app.register_blueprint(ping_router)
