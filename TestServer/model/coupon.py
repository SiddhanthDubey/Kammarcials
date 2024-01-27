import time
import mysql.connector
from app import app


class Coupon:

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            self.coupon_count = 0
            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def check_coupon_count(self):
        # Replace the following with your actual code to check the coupon count in the database
        while True:
            coupon_count = self.get_coupon_count_from_database()
            app.logger.info(f"Number of coupons in the database: {coupon_count}")
            time.sleep(5)  # Sleep for 60 seconds before checking again

    def get_coupon_count_from_database(self):
        # Replace this with your code to query the database and get the coupon count
        # For example, you might use SQLAlchemy or another database library
        # This is just a placeholder
        self.coupon_count = 10
        return self.coupon_count

    def get_coupon_count(self):
        return self.coupon_count
