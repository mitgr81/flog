from functools import wraps
import logging


def __get_func_name(func, args):
    try:
        qualname = func.__qualname__  # Added in python 3
    except AttributeError:
        try:
            # try to get it from its class
            qualname = '{}.{}'.format(args[0].__class__.__name__, func.__name__)
        except:
            # give up and just puke it out
            qualname = func.__name__
    return qualname


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(logging.NullHandler())
    return logger


def log_call(logger):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            met_name = '{}.{}'.format(function.__module__, __get_func_name(function, args))
            logger.debug('{}: args: {}, kwargs: {}'.format(met_name, args, kwargs))
            #If you're debugging, you'll want to step into that thing down there
            retval = function(*args, **kwargs)
            #If you're debugging and wanted to hit the function and haven't yet, it's already too late!
            logger.debug('{}: returns: {}'.format(met_name, retval))
            return retval
        return wrapper
    return decorator


def log_sensitive_call(logger):

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            met_name = '{}.{}'.format(function.__module__, __get_func_name(function, args))
            logger.debug('{}: args: XXXXXX, kwargs: **XXXXXXX'.format(met_name))
            #If you're debugging, you'll want to step into that thing down there
            retval = function(*args, **kwargs)
            #If you're debugging and wanted to hit the function and haven't yet, it's already too late!
            logger.debug('{}: returns: XXXXXXXXXX'.format(met_name))
            return retval
        return wrapper
    return decorator
