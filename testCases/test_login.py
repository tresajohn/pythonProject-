from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*********INFO***********")
        self.logger.info("*********Verify HomePage***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("*********Home Page Pass***********")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*********Home Page Fail***********")
            assert False

    def test_login(self, setup):
        self.logger.info("*********INFO2***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            assert False
