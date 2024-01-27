import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask


def setup_logger(app: Flask):
    log_folder = os.path.join(app.root_path, 'logs')

    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    log_file = os.path.join(log_folder, 'app.log')

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s"
    )

    file_handler = RotatingFileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    app.logger.info("Logger initialized")
