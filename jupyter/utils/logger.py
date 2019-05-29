"""
Logger module
"""

import os
from logging import Logger, getLogger, StreamHandler, Formatter, Handler
from logging.config import dictConfig
from pythonjsonlogger.jsonlogger import JsonFormatter
import logstash

valid_formatters = ['json']
valid_handlers = ['stream', 'logstash']


def get_handler(handler_name: str) -> Handler:
    """
    Return a handler according to its name

    :param handler_name:
    :return:
    """
    if handler_name.lower() == 'stream':
        return StreamHandler()

    if handler_name.lower() == 'logstash':
        host = os.getenv('LOG_LOGSTASH_HOST', None)

        if host is None:
            raise RuntimeError('Host for logstash handler must be defined')

        port = os.getenv('LOG_LOGSTASH_PORT', None)

        if port is None:
            raise RuntimeError('Port for logstash handler must be defined')

        return logstash.TCPLogstashHandler(host, port)

    raise RuntimeError('Unknown handler name')


def get_logger() -> Logger:
    """
    Return logger according to the config

    :return: Logger
    """
    dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
    })

    logger = getLogger(__name__)

    if not logger.handlers:
        formatter = os.getenv('LOG_FORMATTER', 'json')
        handlers_names = os.getenv('LOG_HANDLER', 'stream')

        if ',' in handlers_names:
            handlers = [get_handler(name) for name in handlers_names.split(',')]
        else:
            handlers = [get_handler(handlers_names)]

        for handler in handlers:
            if formatter is not None and formatter.lower() in valid_formatters:
                if formatter.lower() == 'json':
                    handler.setFormatter(configure_json_formatter())
                    logger.addHandler(handler)
            else:
                formatter = Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)

        level = os.getenv('LOG_LEVEL', 'DEBUG')
        logger.setLevel(level)

    return logger


def configure_json_formatter():
    """
    Configure the log formatter

    :return:
    """
    log_keys = [
        'asctime',
        'created',
        'filename',
        'funcName',
        'levelname',
        'levelno',
        'lineno',
        'module',
        'msecs',
        'message',
        'name',
        'pathname',
        'process',
        'processName',
        'relativeCreated',
        'thread',
        'threadName',
    ]

    log_format = ' '.join(['%({0:s})'.format(i) for i in log_keys])

    return JsonFormatter(log_format)
