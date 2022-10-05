import logging.config

import setting


def get_logger(log_basedir) -> logging.Logger:
    d = setting.get_log_setting(log_basedir)
    logging.config.dictConfig(d)
    return logging.getLogger('dsa')
