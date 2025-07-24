import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', 'configuration', 'config.ini'))

class ReadConfig():
    @staticmethod
    def get_url():
        return config.get('common', 'base_url')

    @staticmethod
    def get_email():
        return config.get('common', 'username')

    @staticmethod
    def get_password():
        return config.get('common', 'password')
