from Locators.HomePageLocators import HomePage_Locators


class HomePage_Utilities:

    def __init__(self,driver):
        self.driver=driver

    def search_mobile_phone(self):
        home_loc = HomePage_Locators(self.driver)
        self.driver.find_element("xpath",home_loc.search_box_xpath).send_keys("Mobile Phone")

    def click_search_button(self):
        home_loc = HomePage_Locators(self.driver)
        self.driver.find_element("xpath", home_loc.click_search_button_xpath).click()

    def hello_welcome_text(self):
        home_loc = HomePage_Locators(self.driver)
        self.driver.find_element("xpath",home_loc.hello_text_xpath)

    def click_on_account_and_order(self):
        home_loc = HomePage_Locators(self.driver)
        self.driver.find_element("xpath",home_loc.account_and_order_xpath).click()

    def Hello_sandhya_text_verify(self):
        home_loc = HomePage_Locators(self.driver)
        msg = self.driver.find_element("xpath",home_loc.hello_text_xpath).text
        return msg





