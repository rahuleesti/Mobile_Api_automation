import logging

from lib.helpers.common_helper import CommonHelper
from utilities.utils import Utils


class MenuPage(CommonHelper):
    """

    """
    log = Utils.custom_logger(loglevel=logging.INFO)

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.webdriver = webdriver


    def click_add_to_cart(self):
        """
        Click on the ui element add cart
        :return:
        """
        self.log.info("Click on Add button to add the item to cart")
        self.wait_for_element_present_and_click(self.locators.add_button)

    def enter_and_search_text_menu(self, text):
        """
        Click on the search and send text
        :param text:
        :return:
        """
        self.log.info("Click on search field and enter the text to be searched")
        self.wait_for_element_present_and_send_keys(self.locators.search_textbox_menu, text)
        element = self.webdriver.find_element_by_xpath(
                "//android.widget.Button[contains(@content-desc,'" + text + "')]")
        self.wait_for_element_present_and_click(element)

    def click_search_button_menu(self):
        """
        click on the search button present on the menu
        :return:
        """
        self.log.info(f"Click the search button in bottom navigation bar")
        self.wait_for_element_present_and_click(self.locators.search_button_menu)

    def click_view_basket(self):
        """
        click on the ui element
        :return:
        """
        self.log.info(f"Click on View basket to view the added item in cart")
        self.wait_for_element_present_and_click(self.locators.view_basket)

    def is_visible_in_cart(self, text):
        """
        Validate if the element is displayed on the screen
        :param text: text to located on the screen
        :return:
        """
        self.log.info(f"Selected item is visible in the cart")
        element = self.webdriver.find_element_by_xpath(
                "//android.view.ViewGroup[contains(@content-desc,'" + text + "')]")
        self.wait_for_element_visible(element)
