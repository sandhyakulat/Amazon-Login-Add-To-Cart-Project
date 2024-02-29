

class HomePage_Locators:
    def __init__(self,driver):
        self.driver = driver

        self.search_box_xpath="//input[@type='text']"
        self.click_search_button_xpath = "//input[@id='nav-search-submit-button']"

        self.hello_text_xpath = "//span[@id='nav-link-accountList-nav-line-1']"
        self.account_and_order_xpath = "//a[@id='nav-link-accountList']"
        self.hello_sandhya_text = "//span[@id='nav-link-accountList-nav-line-1']"



