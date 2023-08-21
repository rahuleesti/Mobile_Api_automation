import logging
import time

from appium.webdriver.common.touch_action import TouchAction

from lib.helpers.base_appium_helper import AppiumHelper
from utilities.utils import Utils


class CommonHelper(AppiumHelper):
    """
    Class contains the high level methods than can be used for all the screens,
    """
    log = Utils.custom_logger(loglevel=logging.INFO)

    def __init__(self, webdriver):
        super().__init__(webdriver)

    def click_allow_while_using_the_app_button(self):
        """
        Allow the access to location
        """
        self.log.info("Click 'While using the app' button on system dialog")
        self.wait_for_element_present_and_click(self.locators.location_access_while_using_app)

    def click_back_via_system_navigation(self):
        """
        To navigate back using system keys
        :return:
        """
        self.log.info("Go back from the screen using system navigation")
        self.webdriver.press_keycode(4)

    def wait_for_popup_to_appear(self, locator, popup_title, timeout=3):
        """
        wait for the element to confirm popup is displayed
        :param locator: locator of the element
        :param popup_title: pop-up title
        :param timeout: timeout in seconds
        :return:
        """
        self.log.info(f"Wait for {popup_title} popup to appear")
        self.wait_for_element_visible(locator, timeout)

    def click_settings_button_location_access_popup(self):
        """
        Click settings button on system pop-up
        :return:
        """
        self.log.info("Click 'Settings' button on location access popup")
        self.wait_for_element_present_and_click(self.locators.location_system_settings_button)

    def click_location_toggle_switch(self):
        """
        Click on the location toggle switch
        :param
        :return:
        """
        self.log.info("Click location toggle switch in location settings page")
        self.wait_for_element_present_and_click(self.locators.location_toggle_switch)

    def click_search_button(self):
        """
        Click on the search button in the app
        :return:
        """
        self.log.info("Click the search button in bottom navigation bar")
        self.wait_for_element_present_and_click(self.locators.search_tab_bottom_nav_bar)

    def click_current_location_destination_overlay(self):
        """
        Click on the location destination delivery pop-up
        :return:
        """
        self.log.info("Click 'Current location' in delivery destination overlay")
        self.wait_for_element_present_and_click(self.locators.select_current_location, 10)

    def close_delivery_destination_overlay(self):
        """
        click on close button on location destination delivery pop-up
        :return:
        """
        self.log.info("Close delivery destination overlay")
        self.wait_for_element_present_and_click(self.locators.close_delivery_destination_warning)

    def provide_location_access_current_location(self):
        """
        click on the current location on location destination delivery pop-up
        :return:
        """
        self.log.info("Provide location access and select current location")
        self.click_current_location_destination_overlay()
        self.click_settings_button_location_access_popup()
        self.click_location_toggle_switch()
        self.click_back_via_system_navigation()
        time.sleep(5)
        self.wait_for_element_present_and_click(self.locators.search_tab_bottom_nav_bar, 10)

    def wait_for_screen_to_open(self, locator, screen_title, timeout=3):
        """
        wait for the app screen to open
        :param locator: locator of the screen
        :param screen_title: title of the screen/page name
        :param timeout: timeout in seconds
        :return: element
        """
        self.log.info(f"Wait for {screen_title} to open")
        self.wait_for_element_visible(locator, timeout=timeout)

    def wait_for_text_to_be_displayed(self, locator):
        """
        wait for the text to be displayed on screen
        :param locator: locator of the text
        :return:
        """
        text = locator
        self.log.info(f"Wait for the text to be displayed: {text}")
        self.wait_for_element_visible(locator)

    def toggle_on_airplane_mode(self):
        """
        To toggle the airplane mode button
        :return:
        """
        action = TouchAction(self.webdriver)

        size = self.webdriver.get_window_size()
        start_x = int(size["width"] * .5)
        start_y = int(size["height"] * .1)
        end_y = int(size["height"] * .8)
        self.webdriver.open_notifications()
        action.long_press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()
        self.log.info(f"Click on Airplane mode icon and switch on it")
        self.wait_for_element_visible(self.locators.airplane_mode_switch, 5)
        action.tap(self.locators.airplane_mode_switch)
        self.click_back_via_system_navigation()
