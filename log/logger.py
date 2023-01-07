import inspect
import logging

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG

__LOG_FORMAT = '%(asctime)s %(levelname)s [%(module)s:%(lineno)d]: %(message)s'

'''
logging Filter
'''


class AppFilter(logging.Filter):
    def filter(self, record):
        return True


def logger(level=INFO, name=None):
    if name is None:
        name = __get_logger_name()

    log = logging.getLogger(name)
    # os.makedirs(__log_folder(), exist_ok=True)
    log.addFilter(AppFilter())
    log.setLevel(level)
    log.addHandler(__console_handler())
    return log


def __get_logger_name():
    frame = inspect.stack()[2].frame
    return frame.f_locals['__name__'].split('.')[-1]


def __console_handler():
    ch = logging.StreamHandler()
    ch.setFormatter(__formatter())
    return ch


def __formatter():
    return logging.Formatter(__LOG_FORMAT)
