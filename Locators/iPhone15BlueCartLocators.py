

class iPhone15_blue_cart_locators:

    def __init__(self,driver):
        self.driver = driver

        self.add_to_cart_xpath = "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']"
        self.form_for_add_to_kart_id = "//*[@id='addToCart']"
        self.added_to_kart_msg_xpath = "//*[@id='attachDisplayAddBaseAlert']/div/h4"
        self.proceed_to_checkout = "//*[@id='attach-sidesheet-checkout-button']/span/input"
        self.add_new_address_xpath = "//a[@id='add-new-address-popover-link']"
        self.form_for_new_adress_xpath = "//*[@id='address-ui-checkout-form']"
        self.full_name_xpath = "//*[@id='address-ui-widgets-enterAddressFullName']"
        self.mobile_no_xpath = "//input[@id='address-ui-widgets-enterAddressPhoneNumber']"
        self.pin_code_xpath = "//input[@id='address-ui-widgets-enterAddressPostalCode']"
        self.flat_house_apartment_xpath = "//input[@id='address-ui-widgets-enterAddressLine1']"
        self.town_city_xpath = "//input[@id='address-ui-widgets-enterAddressCity']"
        self.choose_state = "//span[@id='address-ui-widgets-enterAddressStateOrRegion']//span[@role='button']"
        self.maharastra_state_xpath = "//div[@class='a-popover-inner a-lgtbox-vertical-scroll']//a[@id='address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId_20']"
        self.area_strret_sector_xpath = "//input[@id='address-ui-widgets-enterAddressLine2']"
        self.use_this_adress_xpath = "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']"