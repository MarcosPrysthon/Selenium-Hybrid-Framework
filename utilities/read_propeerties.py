import configparser

config = configparser.RawConfigParser()
config.read('.\\config\\config.ini')

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('common info', 'base_URL')

    @staticmethod
    def get_username():
        return config.get('common info', 'username')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')