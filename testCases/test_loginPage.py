from selenium import webdriver

from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
import time

from utilities.readProperties import ReadConfig


class Test_001_loginpage:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_home_page_title(self,setup):
        self.driver = setup
        self.logger.info("************* login tilte same or not **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            assert True
            time.sleep(2)
            self.logger.info("************* login page title is same , testcase passed  **************")
            self.logger.info("************* login testcase 1 is passed  **************")
            self.driver.close()
        else:
            time.sleep(2)
            self.logger.info("************* login page title is same, testcase failed **************")
            self.logger.info("************* login 1st  testcase failed **************")
            self.driver.close()
            assert False

    def test_login_successful(self, setup):
        self.driver = setup
        self.logger.info("************* invalid inputs login successufull or not check  **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            self.logger.info("************* valid input to  login successful , testcase passed  **************")
            self.logger.info("************* login testcase 2 is passed  **************")
            self.driver.close()
        else:
            self.logger.info("************* invali input to login , testcase failed **************")
            self.logger.info("************* login 2nd testcase failed **************")
            self.driver.close()

    def test_invalid_email(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.logger.info("************* invalid email id and valid password **************")
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username("keerthana@gmail.com")
            self.login.set_password(self.password)
            self.login.set_login()
            error_msg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Invalid credentials or account blocked']")))
            print(error_msg.text)
            time.sleep(2)
            if error_msg.text == "Invalid credentials or account blocked":
                assert True

            else:
                assert False
            self.logger.info("************* invalid email id and valid passowrd testcase passed**************")
            self.logger.info("*********** login testcase invalid email , and valid password 3 testcase passed ************")
            self.driver.close()

        else:
            self.logger.info("************* invalid email id and valid password 3 testcase failed **************")
            self.logger.info("************* invalid email id and valid password **************")
            self.driver.close()
            assert False
    def test_invalid_password(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.logger.info("************* invalid password id and valid password **************")
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password("@@##@#")
            self.login.set_login()
            error_msg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Invalid credentials']")))
            print(error_msg.text)
            time.sleep(2)
            if error_msg.text == "Invalid credentials":
                assert True

            else:
                assert False
            self.logger.info("************* valid email id and invalid passowrd testcase passed**************")
            self.logger.info("*********** login testcase valid email , and invalid password 4 testcase passed ************")
            self.driver.close()

        else:
            self.logger.info("************* valid email id and invalid password 4th testcase failed **************")
            self.logger.info("************* valid email id and invalid password **************")
            self.driver.close()
            assert False

    def test_invalid_login(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.logger.info("************* invalid login and invalid password **************")
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username("admin@gmail.com")
            self.login.set_password("@@##@#")
            time.sleep(2)
            self.login.set_login()
            error_msg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Invalid credentials or account blocked']")))
            print(error_msg.text)
            time.sleep(2)
            if error_msg.text == "Invalid credentials or account blocked":
                assert True

            else:
                assert False
            self.logger.info("************* invalid email id and invalid passowrd testcase passed**************")
            self.logger.info("*********** login testcase valid email , and invalid password 5 testcase passed ************")
            self.driver.close()

        else:
            self.logger.info("************* invalid email id and invalid password 5th testcase failed **************")
            self.logger.info("************* invalid email id and invalid password **************")
            self.driver.close()
            assert False

    def test_login_dashboard_capture(self, setup):
        self.driver = setup
        self.logger.info("************* valid inputs to capure dashboard title **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            dashboard_title = self.driver.title
            if dashboard_title == "Outrace - Premium VTS":
                assert True
                self.logger.info("************* valid input to capture dashboard title , testcase passed  **************")
                self.logger.info("************* login testcase 6 is passed  **************")
                self.driver.close()
            else:
                assert False
        else:
            self.logger.info("************* valid input to capture dashboard title , testcase failed **************")
            self.logger.info("************* login 6 nd testcase failed **************")
            self.driver.close()

    def test_login_logout(self, setup):
        self.driver = setup
        self.logger.info("************* valid inputs and logout **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            dashboard_title = self.driver.title
            if dashboard_title == "Outrace - Premium VTS":
                time.sleep(2)
                self.login.set_logout()
                time.sleep(2)
                self.login.set_conform_logout()
                assert True
                self.logger.info("************* valid input to login and logout  , testcase passed  **************")
                self.logger.info("************* login testcase 7 is passed  **************")
                self.driver.close()
            else:
                assert False
        else:
            self.logger.info("************* valid input to login and logout  , testcase failed **************")
            self.logger.info("************* login 7 th  testcase failed **************")
            self.driver.close()

    def test_login_logout_keep_session(self, setup):
        self.driver = setup
        self.logger.info("************* valid inputs and before logout keep session **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            dashboard_title = self.driver.title
            if dashboard_title == "Outrace - Premium VTS":
                time.sleep(2)
                self.login.set_logout()
                time.sleep(2)
                self.login.set_keep_session()
                assert True
                self.logger.info("************* valid input to login before logout keep session  , testcase passed  **************")
                self.logger.info("************* login testcase 8 is passed  **************")
                self.driver.close()
            else:
                assert False
        else:
            self.logger.info("************* valid input to login before logout keep session  , testcase failed **************")
            self.logger.info("************* login 8 th  testcase failed **************")
            self.driver.close()

    def test_login_logout_profile(self, setup):
        self.driver = setup
        self.logger.info("************* valid inputs and logout **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            dashboard_title = self.driver.title
            if dashboard_title == "Outrace - Premium VTS":
                time.sleep(2)
                self.login.set_profile()
                time.sleep(2)
                self.login.set_session()
                time.sleep(2)
                self.login.set_conform_logout()
                assert True
                self.logger.info("************* valid input to login and logout  , testcase passed  **************")
                self.logger.info("************* login testcase 7 is passed  **************")
                self.driver.close()
            else:
                assert False
        else:
            self.logger.info("************* valid input to login and logout  , testcase failed **************")
            self.logger.info("************* login 7 th  testcase failed **************")
            self.driver.close()
    def test_login_logout_keep_session_profile(self, setup):
        self.driver = setup
        self.logger.info("************* valid inputs and before logout keep session **************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Outrace - Premium VTS":
            self.login.set_username(self.email)
            self.login.set_password(self.password)
            time.sleep(2)
            self.login.set_login()
            dashboard_title = self.driver.title
            if dashboard_title == "Outrace - Premium VTS":
                time.sleep(2)
                self.login.set_logout()
                time.sleep(2)
                self.login.set_keep_session_profile()
                assert True
                self.logger.info("************* valid input to login before logout keep session  , testcase passed  **************")
                self.logger.info("************* login testcase 8 is passed  **************")
                self.driver.close()
            else:
                assert False
        else:
            self.logger.info("************* valid input to login before logout keep session  , testcase failed **************")
            self.logger.info("************* login 8 th  testcase failed **************")
            self.driver.close()

