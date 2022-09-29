import logging.config
import setting

logging.config.dictConfig(setting.LOGGING_DIC)


def get_logger() -> logging.Logger:
    return logging.getLogger('dsa')
