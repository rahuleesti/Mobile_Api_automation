from lib.pages.home_page import HomePage
from lib.pages.search_page import SearchPage
from utilities.utils import Utils

log = Utils.custom_logger()

log.info("Validates the filter chip selected from popular categories is displayed "
         "on search results page")
def test_selected_filterchip_displayed_in_search_results(setup):
    log.info("Step 1: Launch the application")
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    log.info("Step 2: Provide the location access to the app")
    home_page.provide_location_access_current_location()
    log.info("Step 3: click on the search button")
    search_page.click_search_button()
    log.info("Step 4: click on the item from popular categories")
    search_page.click_item_from_popular_categories()
    log.info("Step 5: Check is filter chip text is same as selected from popular categories")
    filter_chip_text = (
            search_page.get_text_from_element_found_by_locator(search_page.locators.search_filter_chip_result))
    if "Dinner" in filter_chip_text:
        log.info("Step 6: Filter chip text is Dinner")

