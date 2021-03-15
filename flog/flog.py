import logging
import os
import uuid
from functools import wraps


class CorrelationLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if "correlation_id" in self.extra:
            msg = "[{}] {}".format(self.extra["correlation_id"], msg)
        return msg, kwargs


def __get_func_name(func, args):
    try:
        qualname = func.__qualname__  # Added in python 3
    except AttributeError:
        try:
            # try to calculate it from its class
            qualname = "{}.{}".format(func.im_self.__class__.__name__, func.__name__)
        except Exception:
            # give up and just puke it out
            qualname = func.__name__
    return qualname


def __get_log_function(logger):
    if callable(logger):
        return logger
    else:
        return logger.debug


def get_logger(name, add_correlation_id=False):
    """Gets a logger

    Arguments:
        name - the name you wish to log as
        add_correlation_id - wraps a logger with an adapter that will add a uuid4 to each log record

    Returns:
        A logger!
    """
    logger = logging.getLogger(name)
    logger.addHandler(logging.NullHandler())
    if add_correlation_id:
        return CorrelationLoggerAdapter(logger, {"correlation_id": str(uuid.uuid4())})
    return logger


def _log_call(logger):
    log_function = __get_log_function(logger)

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            full_function_name = "{}.{}".format(function.__module__, __get_func_name(function, args))
            log_function("{}: args: {}, kwargs: {}".format(full_function_name, args, kwargs))
            # If you're debugging, you'll want to step into that thing down there
            retval = function(*args, **kwargs)
            # If you're debugging and wanted to hit the function and haven't yet, it's already too late!
            log_function("{}: returns: {}".format(full_function_name, retval))
            return retval

        return wrapper

    return decorator


def _log_sensitive_call(logger):
    log_function = __get_log_function(logger)

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            full_function_name = "{}.{}".format(function.__module__, __get_func_name(function, args))
            log_function("{}: args: *XXXXXX, kwargs: **XXXXXXX".format(full_function_name))
            # If you're debugging, you'll want to step into that thing down there
            retval = function(*args, **kwargs)
            # If you're debugging and wanted to hit the function and haven't yet, it's already too late!
            log_function("{}: returns: XXXXXXXXXX".format(full_function_name))
            return retval

        return wrapper

    return decorator


if not __debug__ or os.environ.get("FLOG_NOWRAP", False):
    log_call = log_sensitive_call = lambda logger: lambda function: function
else:
    log_call = _log_call
    log_sensitive_call = _log_sensitive_call
