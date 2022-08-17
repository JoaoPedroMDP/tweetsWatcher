# coding: utf-8
from logging.config import dictConfig
from app.configs.config import LOGGING_LEVEL


def init_logging():
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s - %(message)s (%(funcName)s:%(lineno)s)',
            }
        },
        'handlers': {
            'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 10,  # 10 MB
                'backupCount': 4,  # mantém os 4 arquivos de log anteriores
                'filename': 'twitter.log',
                'formatter': 'default'
            },
            'root': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
        },
        'loggers': {
            'twitter': {
                'level': LOGGING_LEVEL,
                'handlers': ['default'],
                'propagate': False
            },
            'root': {
                'level': 'WARNING',
                'handlers': ['root']
            }
        },
    })
