import time

import pytest

from Utilities.HomePageUtilities import HomePage_Utilities
from Utilities.Login_Page_Utilities import login_page_utilities
from Utilities.Mobile_Phone_Utilities import mobile_phone_searchpage
from Utilities.iPhone15_blue_Utilities import iPhone_red_refurbished_utilities
from Utilities.iPhone15_pro_search_utilities import iPhone_searchPage


@pytest.mark.usefixtures("driver_initialization")
class Test_iphone_15_pro:
    def test_search_iphone15_pro_256GB(self,driver_initialization):

        home_utl = HomePage_Utilities(self.driver)
        mob_utl = mobile_phone_searchpage(self.driver)
        iph_utl = iPhone_searchPage(self.driver)
        iPh_blue_utl = iPhone_red_refurbished_utilities(self.driver)
        login_utl = login_page_utilities(self.driver)

            #searcing for iphone 15 pro in searchbox
        iph_utl.search_iphone15_pro_in_seachbox()
        home_utl.click_search_button()

            #selecting 256gb checkbox
        iph_utl.click_on_checkbox_256gb()

            #select iPhone with 256gb blue
        iph_utl.select_iPhone_with_256gb()

            #switching driver to new tab for iphone 15 pro blue
        iph_utl.Switch_to_iPhone15_pro_tab()

            #adding item to kart
        iPh_blue_utl.iPhone15_blue_add_to_kart()

            #checking added to cart is successful or not
        actual_msg_for_cart = iPh_blue_utl.actual_added_to_kart_msg()

            #assert
        expected_msg_for_cart = "Added to Cart"
        assert actual_msg_for_cart == expected_msg_for_cart

            #click on proceed to checkout
        iPh_blue_utl.proceed_to_checkout()

            #login

        login_utl.enter_email_or_number_textbox()
        login_utl.click_on_continue_button()
        login_utl.enter_password_textbox()
        login_utl.click_on_sign_in_button()

            #add new adress
        iPh_blue_utl.add_new_address()
        iPh_blue_utl.Form_for_new_adress()

        time.sleep(7)











