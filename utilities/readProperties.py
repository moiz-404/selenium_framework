import configparser

config = configparser.RawConfigParser()
config.read("./configurationsfiles/config.ini")

class ReadConfig:
    @staticmethod
    def getUserName():
        username = config.get("common info", "useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "userpassword")
        return password