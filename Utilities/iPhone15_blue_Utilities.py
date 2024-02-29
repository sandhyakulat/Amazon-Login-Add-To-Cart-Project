from Locators.iPhone15BlueCartLocators import iPhone15_blue_cart_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class iPhone_red_refurbished_utilities:
    def __init__(self,driver):
        self.driver = driver

    def iPhone15_blue_add_to_kart(self):
        iP_red_loc = iPhone15_blue_cart_locators(self.driver)
        Form = self.driver.find_element("xpath", iP_red_loc.form_for_add_to_kart_id)
        Form.find_element("xpath",iP_red_loc.add_to_cart_xpath).click()

    def actual_added_to_kart_msg(self):
        iP_red_loc = iPhone15_blue_cart_locators(self.driver)
        added_to_kart_msg = self.driver.find_element("xpath",iP_red_loc.added_to_kart_msg_xpath)
        return (added_to_kart_msg.get_attribute("innerText"))

    def proceed_to_checkout(self):
        iP_red_loc = iPhone15_blue_cart_locators(self.driver)
        self.driver.find_element("xpath",iP_red_loc.proceed_to_checkout).click()

    def add_new_address(self):
        iP_red_loc = iPhone15_blue_cart_locators(self.driver)
        self.driver.find_element("xpath",iP_red_loc.add_new_address_xpath).click()

    def Form_for_new_adress(self):
        iP_red_loc = iPhone15_blue_cart_locators(self.driver)
        form_for_new_adress_fill = self.driver.find_element("xpath",iP_red_loc.form_for_new_adress_xpath)
        form_for_new_adress_fill.find_element("xpath",iP_red_loc.full_name_xpath).send_keys("sandhya")
        form_for_new_adress_fill.find_element("xpath",iP_red_loc.mobile_no_xpath).send_keys("1234567890")
        form_for_new_adress_fill.find_element("xpath",iP_red_loc.pin_code_xpath).send_keys("412207")
        form_for_new_adress_fill.find_element("xpath",iP_red_loc.flat_house_apartment_xpath).send_keys("A101 Bleatch Icon Imperio, Ivy Estate Road, Wagholi")
        form_for_new_adress_fill.find_element("xpath",iP_red_loc.area_strret_sector_xpath).send_keys("wagholi")
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(("xpath",iP_red_loc.use_this_adress_xpath)))

        form_for_new_adress_fill.find_element("xpath",iP_red_loc.use_this_adress_xpath).click()


