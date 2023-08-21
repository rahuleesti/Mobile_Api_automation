from selenium.webdriver.common.by import By


class LocatorsAndroid:
    location_access_app_popup = By.ID, "com.android.permissioncontroller:id/permission_message"
    location_access_while_using_app = By.ID, "com.android.permissioncontroller:id/" \
                                             "permission_allow_foreground_only_button"
    select_current_location = By.XPATH,  "//android.view.ViewGroup[contains(@content-desc,'Current location')]"
    location_settings_system_popup = By.ID, "android:id/alertTitle"
    location_system_settings_button = By.ID, "android:id/button1"
    location_toggle_switch = By.ID, "com.android.settings:id/switch_widget"
    delivery_destination_warning = By.ID, "components.DeliveryDestinationWarning.title"
    close_delivery_destination_warning = By.XPATH, "//android.widget.Button[@content-desc='Close delivery destination selection modal']"
    home_screen = By.ID, "navigation.GlobalTabBar.HomeStack"
    search_tab_bottom_nav_bar = By.XPATH, "//android.view.View[contains(@content-desc,'Search')]"
    search_screen = By.ID, "screens.Search.view"
    search_text_box = By.XPATH, "//android.widget.EditText[@content-desc='Restaurants or cuisines']"
    dinner_popular_categories = By.XPATH, "//android.widget.Button[contains(@content-desc,'Dinner')]"
    search_filter_chip_result = By.XPATH, "//android.view.ViewGroup[contains(@content-desc,'Dinner')]/android.widget.TextView[1]"
    provider_name = By.ID, "screens.Provider.providerName"
    search_button_menu = By.XPATH, "//android.widget.Button[@content-desc='Search from menu']"
    search_textbox_menu = By.ID, "components.StickyHeader.searchInput"
    add_button = By.XPATH, "//android.widget.Button[contains(@content-desc,'Add,')]"
    view_basket = By.ID, " screens.Provider.Menu.viewBasket"
    airplane_mode_switch = By.XPATH, "//android.view.ViewGroup[contains(@content-desc='Airplane,mode,Off')]/android.widget.ImageView"
    no_internet_banner = By.XPATH, "//android.widget.TextView[@text='No internet connection']"
    clear_notifications = By.XPATH, "//android.widget.TextView[@text='Clear']"
