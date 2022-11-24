import textwrap

LOGDIR_BASE_PATH = './logs'

LOGGING_CONFIG = {
    'version': 1.0,
    'disable_existing_loggers': False,
    # log format
    'formatters': {
        'standard': {
            'format': textwrap.dedent("""\
            %(asctime)s %(threadName)s:%(thread)d [%(name)s] %(levelname)s [%(pathname)s:%(lineno)d] %(message)s\
            """),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'cli_console': {
            'format': textwrap.dedent("""\
            %(asctime)s %(thread)d:%(threadName)s [%(filename)s:%(lineno)d] [%(name)s] [%(levelname)s] %(message)s\
            """),
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s -- %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    # log filter
    'filters': {},
    # log handler
    'handlers': {
        'console_debug_handler': {
            'level': 'DEBUG',  # 日志处理的级别限制
            'class': 'logging.StreamHandler',  # 输出到终端
            'formatter': 'standard'  # 日志格式
        },
        'console_info_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file_info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'filename': f'{LOGDIR_BASE_PATH}/main.py.log',
            'maxBytes': 10 * 1024 * 1024,  # 日志大小 10M
            'backupCount': 3,  # 日志文件保存数量限制
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
    },
    # 日志记录器，logging.getLogger() 根据传入的名字匹配以下日志记录器
    'loggers': {
        'console_debug': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'DEBUG',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
        'file_info': {
            'handlers': ['file_info_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        # 默认日志记录器，如果没有在这里匹配上日志记录器，则使用次日志记录器，并按创建日志记录器的名字命名
        '': {
            'handlers': ['console_debug_handler', 'file_info_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
