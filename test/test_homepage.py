import unittest

from selenium import webdriver
from src.pages.homepage import Homepage


class SpacePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.jetbrains.com/space")
        self.homepage = Homepage(self.driver)

    def test_logo_button(self):
        self.homepage.click_logo_button()
        self.assertTrue("https://www.jetbrains.com/" == self.homepage.get_current_url(),
                        "Не перешли на https://www.jetbrains.com/")

    def test_change_country(self):
        self.assertTrue("France" == self.homepage.change_country(), "Fail!")

    def test_on_focus_color_team_tools_button(self):
        self.assertTrue("1" == self.homepage.get_opacity_on_focus_team_tools_button(), "Fail!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
