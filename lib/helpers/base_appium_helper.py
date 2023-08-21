from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators_android import LocatorsAndroid


class AppiumHelper:
    """
    Class contains low-level methods that call appium driver commands
    """

    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.locators = LocatorsAndroid

    def wait_for_element_present(self, locator, timeout=5):
        """
        Wait for the presence of UI element
        :param locator: locator of the element
        :param timeout: waiting time in seconds
        :return: element
        """
        wait = WebDriverWait(self.webdriver, timeout)
        message = f'UI element not found: {locator}'
        return wait.until(ec.presence_of_element_located(locator), message)

    def wait_for_element_present_and_click(self, locator, timeout=5):
        """
        Wait for the presence of UI element and click
        :param locator: locator of the element
        :param timeout: waiting time in seconds
        :return: element
        """
        element = self.wait_for_element_present(locator, timeout)
        element.click()
        return element

    def wait_for_element_present_and_send_keys(self, locator, text):
        """
        Wait for the UI element and send keys
        :param locator: locator of the element
        :param text: string for input
        :return:
        """
        element = self.wait_for_element_present(locator, timeout=1)
        element.send_keys(text)

    def wait_for_element_visible(self, locator, timeout=3):
        """
        wait for the element to be visible on screen
        :param locator: locator of the element
        :param timeout: timeout in seconds
        :return: element
        """
        wait = WebDriverWait(self.webdriver, timeout)
        message = f'Web element is not visible: {locator}'
        return wait.until(ec.visibility_of_element_located(locator), message)

    def get_text_from_element_found_by_locator(self, locator):
        """
        Get text from the element
        :param locator: locator of the element
        :return: string
        """
        element = self.wait_for_element_present(locator)
        text = element.text
        return text
