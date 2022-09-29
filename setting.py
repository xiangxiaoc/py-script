LOGGING_DIC = {
    'version': 1.0,
    'disable_existing_loggers': False,
    # log format
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(threadName)s:%(thread)d [%(name)s] %(levelname)s [%(pathname)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s  %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'test': {
            'format': '%(asctime)s '
        }
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
            'filename': 'abc.log',
            'maxBytes': 10 * 1024 * 1024,  # 日志大小 10M
            'backupCount': 3,  # 日志文件保存数量限制
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'file_deal_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': 'deal.log',  # 日志存放的路径
            'encoding': 'utf-8',  # 日志文件的编码
            'formatter': 'standard',
        },
        'file_operate_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': 'operate.log',  # 日志存放的路径
            'encoding': 'utf-8',  # 日志文件的编码
            'formatter': 'standard',
        },
    },
    # 日志记录器
    'loggers': {
        'logger1': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'DEBUG',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
        '': {
            'handlers': ['console_debug_handler', 'file_info_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        '用户操作': {
            'handlers': ['console_debug_handler', 'file_operate_handler'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
