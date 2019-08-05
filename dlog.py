import logging, datetime, os, sys
from logging import DEBUG
from logging import INFO
from logging import WARN
from logging import ERROR
from logging import CRITICAL

def setup_root_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers = []
    file_prefix = "logs/log_"
    file_suffix = ".txt"
    time_stamp = TimeStamp.getInstance().time_stamp
    file_name = file_prefix + time_stamp + file_suffix

    if not os.path.isdir("logs"):
        os.mkdir("logs")

    formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)s] %(message)s")
    fh = logging.FileHandler(file_name)
    fh.setFormatter(formatter)
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setFormatter(formatter)

    root_logger.addHandler(fh)
    root_logger.addHandler(ch)

def get_logger(name):
    logger = logging.getLogger(name)
    return logger


class TimeStamp():
    __instance=None

    @classmethod
    def getInstance(cl):
        if cl.__instance == None:
            return cl()
        else:
            return cl.__instance
    
    def __init__(self):
        self.time_stamp = datetime.datetime.now().strftime("%d-%m-%Y-%H%M%S")
