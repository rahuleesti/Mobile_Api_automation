import logging

from lib.helpers.common_helper import CommonHelper
from utilities.utils import Utils


class SearchPage(CommonHelper):
    """

    """
    log = Utils.custom_logger(loglevel=logging.INFO)

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.webdriver = webdriver

    def search_screen_is_displayed(self):
        """
        To validate if search screen is displaued
        :return:
        """
        self.log.info("Search screen is displayed")
        self.wait_for_screen_to_open(self.locators.search_text_box, "Search Screen")

    def click_item_from_popular_categories(self):
        """
        To click on the UI element on the screen
        :return:
        """
        self.log.info("Click on item from popular categories")
        self.wait_for_element_present_and_click(self.locators.dinner_popular_categories)

    def enter_and_search_text(self, text):
        """
        To send text to the search field
        :param text:
        :return:
        """
        self.log.info("Click on search field and enter the text to be searched")
        self.wait_for_element_present_and_send_keys(self.locators.search_text_box, text)
        element = self.webdriver.find_element_by_xpath(
                "//android.widget.Button[contains(@content-desc,'" + text + "')]")
        self.wait_for_element_present_and_click(element)
