import openpyxl
import pytest

from Utilities.HomePageUtilities import HomePage_Utilities
from Utilities.Mobile_Phone_Utilities import mobile_phone_searchpage
from Utilities.Login_Page_Utilities import login_page_utilities

@pytest.mark.usefixtures("driver_initialization")
class TestLogin:
    def test_validate_successful_login(self,driver_initialization):

        # for login to account

        home_utl = HomePage_Utilities(self.driver)
        login_utl = login_page_utilities(self.driver)

            #click on account to login
        home_utl.click_on_account_and_order()

            #enter Username
        login_utl.enter_email_or_number_textbox()
        login_utl.click_on_continue_button()

            #enter Password
        login_utl.enter_password_textbox()
        login_utl.click_on_sign_in_button()

            #message to check login is successful or not
        actual_msg_for_sign_in = home_utl.Hello_sandhya_text_verify()
        expected_msg_for_sign_in = "Hello, sandhya"

        assert actual_msg_for_sign_in == expected_msg_for_sign_in