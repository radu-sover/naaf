from selenium.webdriver.common.by import By

from naaf.base import Page


class CalendarPage(Page):
    url = 'calendar'

    _btn_plan_training = (By.ID, "planTrainingButton")

    def btn_plan_training(self):
        self.click_on_element(self._btn_plan_training)
        return self


class PlanTrainingPage(Page):
    at_check_locator = (By.CLASS_NAME, "modal-title")

    def at_check_element(self, element):
        return element.text == 'Plan training'
