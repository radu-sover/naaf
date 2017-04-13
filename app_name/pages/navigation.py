from selenium.webdriver.common.by import By

from naaf.base import Page


class NavigationSection(Page):
    """
    Implement navigation to Calendar and Trainings page to be able to assert the menu is working
    Page is the base class, even thou this is an element on the page (available on all pages)
    """
    _btn_trainings = (By.CSS_SELECTOR, "#trainings > a")
    _btn_calendar = (By.CSS_SELECTOR, "#calendar > a")

    def btn_trainings(self):
        self.click_on_element_ac(self._btn_trainings)
        return self

    def btn_calendar(self):
        self.click_on_element_ac(self._btn_calendar)
        return self
