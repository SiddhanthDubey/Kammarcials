import mysql.connector
import logging


class AppLogger:
    def __init__(self, log_file='coupon.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


# Create a logger instance for your module or script
logger_coupon = AppLogger()


class Coupon:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_coupon.log_info("Connection Successful")
        except Exception as e:
            logger_coupon.log_error(f"Error during connection: {e}")

    def get_user_coupon_count_from_database(self):
        try:
            self.cur.execute(f"SELECT * FROM coupons WHERE is_used = 'False'")
            result = self.cur.fetchall()
            #logger_coupon.log_info(f"Number of Coupons: {len(result)}")
            return len(result)
        except Exception as e:
            logger_coupon.log_error(f"Error in get_user_coupon_count_from_database: {e}")
            return "An error occurred while processing your request to get user coupon count from the database"
