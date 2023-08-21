import logging

from lib.helpers.common_helper import CommonHelper
from utilities.utils import Utils


class HomePage(CommonHelper):
    log = Utils.custom_logger(loglevel=logging.INFO)

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.webdriver = webdriver

    def is_displayed_home_screen(self):
        """
        To check if home screen is displayed
        :return:
        """
        self.log.info(f"Home screen is displayed")
        self.wait_for_screen_to_open(self.locators.home_screen, "Home_Screen")
