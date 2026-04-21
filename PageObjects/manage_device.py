from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

class Manage_device:

    link_manage_device_xpath = "//span[text()='Manage Device']"
    btn_register_device_xpath = "//span[text()='Register New Device']"
    text_box_imei_number_xpath = "//input[@placeholder='Enter 15-digit IMEI']"
    text_box_tracker_id_xpath = "//input[@placeholder = 'e.g. TKR-101']"
    dropdown_model_xpath = "//label[text()='MODULE MODEL']/following-sibling::select"
    btn_complete_register_xpath = "//span[text()='Complete Register']"
    text_box_manage_device_search_xpath = "//input[@placeholder = 'Search IMEI, tracker ID, model...']"
    btn_edit_manage_Device_xpath = "//button[@title = 'Edit']"
    dropdown_module_model_xpath = "//label[text()='MODULE MODEL']/following-sibling::select"
    text_box_firmware_version_xpath = "//input[@placeholder = 'e.g. 1.0.4']"
    btn_update_device_xpath = "//span[text()='Update Device']"
    icon_view_device_xpath = "//button[@title='View Details']"
    btn_close_view_xpath = "//button[text()='Close']"
    btn_view_edit_device_xpath = "//span[text()='Edit Device']"
    icon_block_device_xpath = "//button[@title ='Block Device']"
    conform_block_Device_xpath = "//button[text()='Block Device']"


    def __init__(self,driver):
        self.driver = driver

    def set_manage_device(self):
        wait = WebDriverWait(self.driver, 10)
        manage_device_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.link_manage_device_xpath)))
        manage_device_fields.click()

    def set_register_device(self):
        wait = WebDriverWait(self.driver, 10)
        register_device_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_register_device_xpath)))
        register_device_fields.click()

    def set_imei_number(self,imei_number):
        wait = WebDriverWait(self.driver, 10)
        imei_number_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.text_box_imei_number_xpath)))
        imei_number_fields.send_keys(imei_number)

    def set_tracker_id(self,tracker_id):
        wait = WebDriverWait(self.driver, 10)
        tracker_id_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.text_box_tracker_id_xpath)))
        tracker_id_fields.send_keys(tracker_id)

    def set_dropdown_model(self):
        wait = WebDriverWait(self.driver, 10)
        model_fields = Select(wait.until(EC.presence_of_element_located((By.XPATH,self.dropdown_model_xpath))))
        selected_value = "SIM800L v2"
        model_fields.select_by_visible_text(selected_value)
        return selected_value


    def set_button_complete_register(self):
        wait = WebDriverWait(self.driver, 10)
        complete_register_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_complete_register_xpath)))
        complete_register_fields.click()

    def set_edit_manage_device(self):
        wait = WebDriverWait(self.driver, 10)
        edit_manage_device_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_edit_manage_Device_xpath)))
        edit_manage_device_fields.click()

    def view_edit_manage_device(self):
        wait = WebDriverWait(self.driver,10)
        view_edit_fields = wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_view_edit_device_xpath)))
        view_edit_fields.click()

    def block_device_xpath (self):
        wait = WebDriverWait(self.driver, 10)
        block_fields = wait.until(EC.element_to_be_clickable((By.XPATH,self.icon_block_device_xpath)))
        block_fields.click()

    def conform_block(self):
        wait = WebDriverWait(self.driver,10)
        conform_block_fields = WebDriverWait.until(EC.presence_of_element_located((By.XPATH,self.conform_block_Device_xpath)))
        conform_block_fields.click()
    def set_capture_edit_specific_user(self, device_id):

        wait = WebDriverWait(self.driver, 10)

        # Search device
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_manage_device_search_xpath))
        )
        search_box.clear()
        search_box.send_keys(device_id)

        # Wait for rows
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
        )

        for row in rows:

            # ✅ Match correct row
            if device_id in row.text:

                # Find edit button inside td/div
                divs = row.find_elements(By.XPATH, ".//td//div")

                for div in divs:
                    try:
                        edit_btn = div.find_element(By.XPATH, self.btn_edit_manage_Device_xpath)
                        edit_btn.click()
                        break
                    except:
                        continue
                break  # stop after correct row

        model_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_module_model_xpath))
        )

        Select(model_dropdown).select_by_visible_text("FMB920")

        # Enter firmware version
        version = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_firmware_version_xpath))
        )
        version.clear()
        version.send_keys("1.2.2")

        # Click update
        update_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.btn_update_device_xpath))
        )
        update_btn.click()

        # Validate success message
        update_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Device updated successfully')]")
            )
        )

        msg = update_message.text
        print(msg)

        assert "Device updated successfully" in msg, "❌ Update failed"

    def set_capture_view_specific_user(self, device_id, imei_number,model_module):

        wait = WebDriverWait(self.driver, 10)

        # Search
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_manage_device_search_xpath))
        )
        search_box.clear()
        search_box.send_keys(device_id)

        # Wait for rows
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
        )

        for row in rows:

            # 👉 check if this row has your device_id
            if device_id in row.text:

                # 👉 now ONLY inside this row search
                divs = row.find_elements(By.XPATH, ".//td//div")

                for div in divs:
                    try:
                        view_btn = div.find_element(By.XPATH, self.icon_view_device_xpath)

                        # click view
                        view_btn.click()
                        break
                    except:
                        continue
                break

        # Wait for popup
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='IMEI']"))
        )

        # Capture values
        imei_view = self.driver.find_element(
            By.XPATH, "//label[text()='IMEI']/following-sibling::div"
        ).text

        tracker_view = self.driver.find_element(
            By.XPATH, "//label[text()='TRACKER ID']/following-sibling::div"
        ).text

        model_view = self.driver.find_element(
            By.XPATH, "//label[contains(text(),'MODEL')]/following-sibling::div"
        ).text

        # Validate
        print("IMEI UI:", imei_view)
        print("Tracker UI:", tracker_view)
        print("Model UI:", model_view)

        assert imei_view.strip() == imei_number.strip()
        assert tracker_view.strip() == device_id.strip()
        assert model_view.strip() == model_module.strip()

        # ✅ CLOSE POPUP HERE
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
        ).click()

    def open_view(self,device_id):
        wait = WebDriverWait(self.driver, 10)

        # Search device
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_manage_device_search_xpath))
        )
        search_box.clear()
        search_box.send_keys(device_id)

        # Wait for rows
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
        )

        for row in rows:
            if device_id in row.text:
                divs = row.find_elements(By.XPATH, ".//td//div")
                for div in divs:
                    try:
                        view_btn = div.find_element(By.XPATH, self.icon_view_device_xpath)
                        view_btn.click()
                        return  # ✅ STOP after clicking
                    except:
                        continue
                raise Exception("View Button not found for device")

    def open_block(self,device_id):
        wait = WebDriverWait(self.driver, 10)

        # Search device
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_manage_device_search_xpath))
        )
        search_box.clear()
        search_box.send_keys(device_id)

        # Wait for rows
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
        )

        for row in rows:
            if device_id in row.text:
                divs = row.find_elements(By.XPATH, ".//td//div")
                for div in divs:
                    try:
                        block_btn = div.find_element(By.XPATH, self.icon_block_device_xpath)
                        block_btn.click()
                        block_btn = wait.until(
                            EC.presence_of_element_located((By.XPATH, self.conform_block_Device_xpath)))
                        block_btn.click()

                        block_message = wait.until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//span[contains(text(),'Device blocked successfully!')]")
                            )
                        )

                        msg = block_message.text
                        print(msg)

                        assert "Device blocked successfully!" in msg, "❌ Update failed"

                        return  # ✅ STOP after clicking
                    except:
                        continue
                raise Exception("View Button not found for device")



    def get_view_details(self):
        wait = WebDriverWait(self.driver, 10)

        # ✅ WAIT for popup FIRST
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='IMEI']"))
        )

        imei = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='IMEI']/following-sibling::div"))
        ).text

        tracker = self.driver.find_element(
            By.XPATH, "//label[text()='TRACKER ID']/following-sibling::div"
        ).text

        model = self.driver.find_element(
            By.XPATH, "//label[contains(text(),'MODEL')]/following-sibling::div"
        ).text

        firmware = self.driver.find_element(
            By.XPATH, "//label[text()='FIRMWARE']/following-sibling::div"
        ).text

        return {
            "imei": imei,
            "tracker": tracker,
            "model": model,
            "firmware": firmware
        }

    def update_device(self, new_model, new_firmware):

        wait = WebDriverWait(self.driver, 10)

        # click edit
        self.driver.find_element(By.XPATH, self.btn_view_edit_device_xpath).click()

        model_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, self.dropdown_module_model_xpath))
        )

        Select(model_dropdown).select_by_visible_text(new_model)

        version = wait.until(
            EC.presence_of_element_located((By.XPATH, self.text_box_firmware_version_xpath))
        )
        version.clear()
        version.send_keys(new_firmware)

        update_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.btn_update_device_xpath))
        )
        update_btn.click()

        msg = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Device updated successfully')]")
            )
        ).text

        assert "Device updated successfully" in msg


    #---capture total user -----
    def capture_all_data(self):

        total_data_device = []
        online_device = 0
        offline_device = 0
        activated_device = 0
        pending_device = 0

        wait = WebDriverWait(self.driver, 15)

        while True:

            # ✅ wait for real rows
            rows = wait.until(
                lambda d: d.find_elements(By.XPATH, "//table/tbody/tr[.//td]")
            )

            print(f"Rows found: {len(rows)}")

            for i in range(len(rows)):
                try:
                    row = self.driver.find_elements(By.XPATH, "//table/tbody/tr[.//td]")[i]
                    cols = row.find_elements(By.XPATH, ".//td")

                    if len(cols) >= 5:
                        imei_number = cols[1].text.strip()
                        status = cols[3].text.strip()
                        activated = cols[4].text.strip()

                        print("IMEI:", imei_number)

                        total_data_device.append(imei_number)

                        if status == "ONLINE":
                            online_device += 1
                        elif status == "OFFLINE":
                            offline_device += 1

                        if activated == " Activated":
                            activated_device += 1
                        elif activated == " Pending":
                            pending_device += 1

                except:
                    continue


            # ✅ pagination check
            next_buttons = self.driver.find_elements(
                By.XPATH, "//button[.//svg[contains(@class,'chevron-right')]]"
            )

            if not next_buttons:
                print("No pagination available")
                break

            next_btn = next_buttons[0]

            if next_btn.get_attribute("disabled"):
                print("Last page reached")
                break

            print("➡️ Clicking Next Page")

            first_row_before = rows[0].text

            self.driver.execute_script("arguments[0].click();", next_btn)

            # wait for change
            wait.until(
                lambda d: d.find_elements(By.XPATH, "//table/tbody/tr[.//td]")[0].text != first_row_before
            )

        print("Total:", len(total_data_device))
        print("Online:", online_device)
        print("Offline:", offline_device)
        print("Activated:", activated_device)
        print("Pending:", pending_device)

        return total_data_device, online_device, offline_device, activated_device, pending_device