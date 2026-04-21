from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.loginPage import LoginPage
from PageObjects.manage_device import Manage_device
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import random


class Test_manage_device:

    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    #  ----------- Dynamic Data Generators ----------- #
    def generate_imei(self):
        return str(random.randint(800000000000000, 899999999999999))

    def generate_tracker(self):
        return "THY-" + str(random.randint(100, 999))

    # ----------- Common Method ----------- #
    def create_device_and_get_message(self, imei, tracker):
        wait = WebDriverWait(self.driver, 10)

        self.manage_device.set_manage_device()
        self.manage_device.set_register_device()
        self.manage_device.set_imei_number(imei)
        self.manage_device.set_tracker_id(tracker)
        module_selected = self.manage_device.set_dropdown_model()
        self.manage_device.set_button_complete_register()

        message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'successfully') or contains(text(),'exists')]")
            )
        )
        return message.text,module_selected

    # 🔥 ----------- CREATE TEST ----------- #
    @pytest.mark.parametrize("imei_num", [
        "111111111111111",
        "111111111111111"
    ])
    def test_manage_device_create(self, setup, imei_num):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Manage Device Create *****")

        tracker = self.generate_tracker()

        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS", "❌ Login Failed"

        self.manage_device = Manage_device(self.driver)

        self.logger.info(f"Creating device IMEI: {imei_num}, Tracker: {tracker}")

        self.manage_device.set_manage_device()
        self.manage_device.set_register_device()
        self.manage_device.set_imei_number(imei_num)
        self.manage_device.set_tracker_id(tracker)
        model_selected = self.manage_device.set_dropdown_model()
        self.manage_device.set_button_complete_register()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'successfully') or contains(text(),'exists')]")
            )
        )
        msg_text = message.text
        self.logger.info(f"System message: {msg_text}")

        assert "successfully" in msg_text or "exists" in msg_text

    #  ----------- EDIT TEST ----------- #
    def test_manage_device_edit(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Manage Device Edit *****")

        imei = self.generate_imei()
        tracker = self.generate_tracker()

        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS", "❌ Login Failed"

        self.manage_device = Manage_device(self.driver)

        msg_text,_ = self.create_device_and_get_message(imei, tracker)

        self.logger.info(f"Create message: {msg_text}")
        assert "successfully" in msg_text

        # Edit flow
        self.manage_device.set_capture_edit_specific_user(tracker)

        self.logger.info("✅ Edit validation completed")

    # 🔥 ----------- VIEW TEST ----------- #
    def test_manage_device_view(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Manage Device View *****")

        imei = self.generate_imei()
        tracker = self.generate_tracker()

        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS", "Login Failed"

        self.manage_device = Manage_device(self.driver)

        # Create device + get selected model
        msg_text, model_selected = self.create_device_and_get_message(imei, tracker)

        self.logger.info(f"Create message: {msg_text}")
        assert "successfully" in msg_text

        # ✅ View validation (PASS MODEL ALSO)
        self.manage_device.set_capture_view_specific_user(
            tracker,
            imei,
            model_selected
        )

        self.logger.info("✅ View validation completed")

    def test_manage_device_update_and_verify_view(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Device View → Update → Re-Verify *****")

        imei = self.generate_imei()
        tracker = self.generate_tracker()

        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS"

        self.manage_device = Manage_device(self.driver)

        # Create
        msg_text, model_selected = self.create_device_and_get_message(imei, tracker)
        assert "successfully" in msg_text

        # STEP 1: View BEFORE update
        self.manage_device.open_view(tracker)
        before_data = self.manage_device.get_view_details()

        print("Before:", before_data)

        assert before_data["imei"].strip() == imei
        assert before_data["tracker"].strip() == tracker

        # STEP 2: Update
        new_model = "FMB920"
        new_firmware = "1.2.5"

        self.manage_device.update_device(new_model, new_firmware)

        # Close popup
        try:
            close_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
            )
            close_btn.click()
        except:
            print("Popup already closed after update")

        # STEP 3: View AFTER update
        self.manage_device.open_view(tracker)
        after_data = self.manage_device.get_view_details()

        print("After:", after_data)

        assert after_data["model"].strip() == new_model
        assert after_data["firmware"].strip() == new_firmware




    #--------capture all table data -------------------

    def test_capture_all_table(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Manage device capture all table data  *****")


        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS", "Login Failed"

        self.manage_device = Manage_device(self.driver)
        self.manage_device.set_manage_device()
        self.manage_device.capture_all_data()

    def test_manage_device_block_user(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.logger.info("***** TEST: Device View → Update → Re-Verify *****")
        tracker = "THY-696"

        # Login
        self.login = LoginPage(self.driver)
        self.login.set_username(self.email)
        self.login.set_password(self.password)
        self.login.set_login()

        assert self.driver.title == "Outrace - Premium VTS"

        self.manage_device = Manage_device(self.driver)
        self.manage_device.set_manage_device()
        self.manage_device.open_block(tracker)

