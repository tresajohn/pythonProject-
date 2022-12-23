from configparser import RawConfigParser

config = RawConfigParser()
configFilePath = './Configurations/config.ini'
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('TestInformation', "baseURL")
        #url = 'http://admin-demo.nopcommerce.com'
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("TestInformation", "username")
        #username = 'admin@yourstore.com'
        return username

    @staticmethod
    def getPassword():
        password = config.get("TestInformation", "password")
        #password = 'admin'
        return password
