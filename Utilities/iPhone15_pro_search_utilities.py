from Locators.HomePageLocators import HomePage_Locators
from Locators.iPhone15SerchPageLocators import iPhone15_Locators
from Locators.iPhone15BlueCartLocators import iPhone15_blue_cart_locators


class iPhone_searchPage:
    def __init__(self,driver):
        self.driver = driver

    def search_iphone15_pro_in_seachbox(self):
        home_loc = HomePage_Locators(self.driver)
        self.driver.find_element("xpath",home_loc.search_box_xpath).send_keys("iPhone 15 pro")

    def click_on_checkbox_256gb(self):
        IP_locator = iPhone15_Locators(self.driver)
        self.driver.find_element("xpath", IP_locator.checkbox_for_256gb).click()

    def select_iPhone_with_256gb(self):
        IP_locator = iPhone15_Locators(self.driver)
        self.driver.find_element("xpath", IP_locator.select_iPhone15_blue_with_256gb).click()

    def Switch_to_iPhone15_pro_tab(self):
        print("all_windows", self.driver.window_handles)
        print("window_handles[1] =",self.driver.window_handles[1])
        return self.driver.switch_to.window(self.driver.window_handles[1])


