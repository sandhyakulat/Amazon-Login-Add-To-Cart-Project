from Locators.LoginPageLocators import login_page_locators


class login_page_utilities:

    def __init__(self,driver):
        self.driver = driver


    def enter_email_or_number_textbox(self):
        login_loc = login_page_locators(self.driver)
        self.driver.find_element("xpath",login_loc.Enter_email_or_number_text_xpath).send_keys("7666050508")

    def enter_password_textbox(self):
        login_loc = login_page_locators(self.driver)
        self.driver.find_element("xpath",login_loc.Enter_password_text_xpath).send_keys("amazonpassword")

    def click_on_continue_button(self):
        login_loc = login_page_locators(self.driver)
        self.driver.find_element("xpath",login_loc.continue_button_xpath).click()

    def click_on_sign_in_button(self):
        login_loc = login_page_locators(self.driver)
        self.driver.find_element("xpath",login_loc.sign_in_button_xpath).click()




