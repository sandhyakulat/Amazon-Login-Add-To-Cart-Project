class login_page_locators:

    def __init__(self,driver):
        self.driver = driver

        self.Enter_email_or_number_text_xpath = "//input[@name='email']"
        self.Enter_password_text_xpath = "//input[@type='password']"
        self.sign_in_button_xpath = "//input[@id='signInSubmit']"
        self.continue_button_xpath = "//input[@id='continue']"