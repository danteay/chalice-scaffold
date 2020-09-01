"""
Commons errors
"""


class HandlerError(Exception):
    """
    Generic handler error
    :param code: HTTP status code
    :param message: Error message
    :param errors: additional errors
    """

    def __init__(self, code, message, errors=None):
        super().__init__(message, errors)
        self.message = message
        self.code = code

    def get_message(self):
        """Get error message"""
        return self.message

    def get_code(self):
        """Get error code"""
        return self.code


class ConfigurationError(Exception):
    """
    Configuration loading error
    """
