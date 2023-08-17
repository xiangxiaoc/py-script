"""
Project Main Settings
"""

"""
########################################################################################################################
Logging Configuration
"""
LOGDIR_BASE_PATH = "./logs"

LOGGING_CONFIG = {
    "version": 1.0,
    "disable_existing_loggers": False,
    # log format
    # Reference: https://docs.python.org/zh-cn/3/library/logging.html#logrecord-attributes
    "formatters": {
        "standard": {
            "format": "%(asctime)s PID=%(process)d thread=%(threadName)s logger=%(name)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d|%H:%M:%S%z",
        },
        "cli_console": {
            "format": "%(asctime)s thread=%(threadName)s logger=%(name)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d|%H:%M:%S%z",
        },
        "simple": {
            "format": "%(asctime)s logger=%(name)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d|%H:%M:%S%z",
        },
    },
    # log filter
    "filters": {},
    # log handler
    "handlers": {
        "console_handler": {
            "level": "DEBUG",  # 日志处理的最高级别，如果 logger 的级别低于此级别，则使用 logger 的级别
            "class": "logging.StreamHandler",  # 输出到终端
            "formatter": "cli_console",  # 日志格式
        },
        "file_handler": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",  # 保存到文件,日志轮转
            "filename": f"{LOGDIR_BASE_PATH}/main.log",
            "maxBytes": 100 * 1024 * 1024,  # 单个文件日志大小，单位：字节
            "backupCount": 10,  # 日志文件数量限制
            "encoding": "utf-8",
            "formatter": "standard",
        },
    },
    # 日志记录器，logging.getLogger() 根据传入的名字匹配以下日志记录器
    "loggers": {
        "console_debug": {  # 导入时logging.getLogger时使用的app_name
            "handlers": ["console_handler"],  # 日志分配到哪个handlers中
            "level": "DEBUG",  # 日志记录的级别限制
            "propagate": False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
        "file_info": {
            "handlers": ["file_handler"],
            "level": "INFO",
            "propagate": False,
        },
        # 默认日志记录器，如果没有在这里匹配上日志记录器，则使用次日志记录器，并按创建日志记录器的名字命名
        "": {
            "handlers": ["console_handler", "file_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
