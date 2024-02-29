import pytest

from Utilities.HomePageUtilities import HomePage_Utilities
from Utilities.Mobile_Phone_Utilities import mobile_phone_searchpage


@pytest.mark.usefixtures("driver_initialization")
class TestHomePage:
    def test_search_mobile_phone_and_get_price(self,driver_initialization):

        #saving screeenshot after login
        self.driver.save_screenshot("../Log/screenshot1.png")

        home_utl = HomePage_Utilities(self.driver)
        mobile_utl = mobile_phone_searchpage(self.driver)

            #enter mobile_phone in text box
        home_utl.search_mobile_phone()

            #click on search button
        home_utl.click_search_button()

            #enter the price and name of mobile phones to excel sheet
        mobile_utl.list_of_all_mobile_phones_with_prices()




