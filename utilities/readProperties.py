import configparser
import os

config = configparser.RawConfigParser()

config_path = os.path.join(os.path.dirname(__file__), "../Configurations/config.ini")
config.read(config_path)
class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get("login info", "application_url")
    @staticmethod
    def get_username():
        return config.get("login info", "email")
    @staticmethod
    def get_password():
        return config.get("login info", "password")

    @staticmethod
    def get_imei_numer():
        return config.get("manage device", "imei_number")

    @staticmethod
    def get_tracker_id():
        return config.get("manage device", "tracker_id")

    @staticmethod
    def get_search():
        return config.get("manage device", "search")

