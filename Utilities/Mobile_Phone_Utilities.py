import openpyxl

from Locators.MobilePhoneSerachPage import MobileList


class mobile_phone_searchpage:
    def __init__(self,driver):
        self.driver = driver


    def list_of_all_mobile_phones_with_prices(self):
        mob_loc = MobileList(self.driver)

        mobile_name = []
        mobile_price= []

        all = self.driver.find_elements("xpath",mob_loc.all_mobiles_list)

        for mobile in all:
            names = mobile.find_elements("xpath",mob_loc.all_mobile_name_list_xpath)

            for name in names:
                mobile_name.append(name.text)

            prices = mobile.find_elements("xpath",mob_loc.all_mobile_price_list_xpath)

            for price in prices:
                mobile_price.append(price.text)

        final = zip(mobile_name,mobile_price)

        workbook = openpyxl.Workbook()
        sheet1 = workbook.active
        sheet1.title = "Amazon_mobile_list"

        for y in list(final):
            sheet1.append(y)

        workbook.save("../Log/Amazon_Mobile_list.xlsx")