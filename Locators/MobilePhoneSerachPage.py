import openpyxl


class MobileList:

    def __init__(self,driver):
        self.driver = driver

        self.all_mobiles_list = "//div[@data-component-type='s-search-result']"
        self.all_mobile_name_list_xpath = ".//span[@class='a-size-medium a-color-base a-text-normal']"
        self.all_mobile_price_list_xpath = ".//span[@class='a-price-whole']"











