
from lib.pages.home_page import HomePage
from utilities.utils import Utils

log = Utils.custom_logger()

log.info("Test case - Validate that no network banner is displayed")
def test_no_network_banner_displayed_in_airplane_mode_case(setup):
    log.info("Step 1: Launch the application")
    homepage = HomePage(setup)
    log.info("Step 2: toggle off the airplane mode button")
    homepage.toggle_on_airplane_mode()
    log.info("Step 3: Validate the no network banner is displayed")
    homepage.wait_for_element_visible(homepage.locators.no_internet_banner)
