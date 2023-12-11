from seleniumpagefactory import PageFactory
from selenium.webdriver.common.keys import Keys
from test.waiting import waiting_css_property
from test.logger import logger


# page_url = https://www.jetbrains.com/space

class Homepage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "logo_button": ("CSS", "._siteLogo__image_nnydt:first-child"),
        "country_button": ("CSS", "[data-test='footer-country-button']"),
        "changeCountryField": ("CSS", "[data-test='search-input']"),
        "changeCountryButton": ("CSS", "[data-test='footer-popup-confirm-country']"),
        "devtools_button": ("CSS", "[aria-label='Developer Tools: Open submenu'][data-test='main-menu-item-action']"),
        "team_tools_button": ("CSS", "[aria-label='Team Tools: Open submenu'][data-test='main-menu-item-action']"),

    }

    def click_logo_button(self):
        self.logo_button.click()
        logger.info("Кликнули по лого сайта.")

    def get_current_url(self):
        return self.driver.current_url

    def change_country(self):
        self.country_button.click()
        logger.info("Кликнули по кнопке выбора страны.")
        self.changeCountryField.send_keys("France")
        logger.info("Напечатали в поле ввода: France.")
        self.changeCountryField.send_keys(Keys.ENTER)
        logger.info("Нажали Enter.")
        self.changeCountryButton.click()
        logger.info("Кликнули по кнопке Choose.")
        return self.country_button.text

    def get_opacity_on_focus_team_tools_button(self):
        self.devtools_button.send_keys(Keys.TAB)
        logger.info("Установили фокус на кнопке " + self.team_tools_button.text + ".")
        waiting_css_property(self.team_tools_button, "opacity", "1", 3)
        return self.team_tools_button.value_of_css_property("opacity")
