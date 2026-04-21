from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    text_box_email_xpath = "//input[@placeholder='name@outrace.com']"
    text_box_password_xpath = "//input[@placeholder='••••••••••••']"
    btn_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//span[text()='Logout Account']"
    btn_conform_logout_xpath = "//button[text()='Yes, Log Out']"
    btn_keep_session_xpath = "//button[text()='Keep Session']"
    btn_profile_xpath = "//span[text()='Super Admin']"
    btn_session_xpath = "//span[text()='Suspend Session']"
    btn_keep_session_profile_xpath = "//button[text()='Keep Session']"
    btn_profile_conform_logout_xpath = "//button[text()='Yes, Log Out']"

    def __init__(self, driver):
        self.driver = driver
    def set_username (self,username):
        wait = WebDriverWait(self.driver, 10)
        username_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.text_box_email_xpath)))
        username_fields.send_keys(username)

    def set_password (self,password):
        wait = WebDriverWait(self.driver, 10)
        password_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.text_box_password_xpath)))
        password_fields.send_keys(password)

    def set_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_button_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_login_xpath)))
        login_button_fields.click()

    def set_logout(self):
        wait = WebDriverWait(self.driver, 10)
        logout_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_logout_xpath)))
        logout_fields.click()

    def set_conform_logout(self):
        wait = WebDriverWait(self.driver, 10)
        conform_logout_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_conform_logout_xpath)))
        conform_logout_fields.click()

    def set_profile(self):
        wait = WebDriverWait(self.driver, 10)
        profile_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_profile_xpath)))
        profile_fields.click()

    def set_session(self):
        wait = WebDriverWait(self.driver, 10)
        session_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_session_xpath)))
        session_fields.click()

    def set_profile_conform(self):
        wait = WebDriverWait(self.driver, 10)
        profile_conform_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_profile_conform_logout_xpath)))
        profile_conform_fields.click()

    def set_keep_session(self):
        wait = WebDriverWait(self.driver,10)
        keep_session_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_keep_session_xpath)))
        keep_session_fields.click()

    def set_keep_session_profile(self):
        wait = WebDriverWait(self.driver,10)
        keep_session_profile_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_keep_session_profile_xpath)))
        keep_session_profile_fields.click()

