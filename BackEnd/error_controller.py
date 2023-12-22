import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    filename='app.log',  # Specify the log file
    filemode='w'  # Set the file mode ('w' for write, 'a' for append)
)


class AppLogger:
    def __init__(self):
        # Configure the logging settings
        self.logger = logging.getLogger(__name__)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, exception, message=None):
        if message:
            self.logger.error(f"{message}: {str(exception)}")
        else:
            self.logger.error(str(exception))
