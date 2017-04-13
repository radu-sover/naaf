from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from naaf.base import Page


class TrainingsPage(Page):
    """
    Implement Add New Training, Search in List, Delete from list
    """
    url = 'trainings'

    def btn_new_training(self):
        self.click_on_element((By.ID, "newTrainingButton"))
        return self

    def text_filter_name(self, text):
        self.send_keys_on_element((By.NAME, 'name'), text)
        return self

    def btn_delete_for_item(self, search_text):
        locator = (By.CLASS_NAME, 'deleteCategoryButton')
        self._first_element_in_list(search_text).find_element(*locator).click()
        return self

    def btn_edit_for_item(self, search_text):
        locator = (By.CLASS_NAME, 'editCategoryButton')
        self._first_element_in_list(search_text).find_element(*locator).click()
        return self

    def _first_element_in_list(self, search_text):
        elements = self.driver.find_elements_by_repeater('training in $data')
        elements = [e for e in elements if search_text in e.text]
        if not len(elements):
            raise NoSuchElementException

        return elements[0]

    def list_trainings_contains(self, search_text):
        elements = self.driver.find_elements_by_repeater('training in $data')
        return any([e for e in elements if search_text in e.text])


class AddEditTrainingPage(Page):
    at_check_locator = (By.CLASS_NAME, 'modal-title')

    def text_name(self, text):
        self.send_keys_on_element((By.ID, 'name'), text)
        return self

    def text_description(self, text):
        self.send_keys_on_element((By.ID, 'description'), text)
        return self

    def select_category(self, option):
        self.select_option_on_element((By.ID, 'categories'), option_text=option)
        return self

    def text_modules(self, text):
        self.send_keys_on_element((By.ID, 'noOfModules'), text)
        return self

    def text_duration(self, text):
        self.send_keys_on_element((By.ID, 'moduleDuration'), text)
        return self

    def select_status(self, option):
        self.select_option_on_element((By.ID, 'status'), option_text=option)
        return self

    def btn_save(self):
        self.click_on_element((By.ID, "saveButton"))
        return self

    def at_check_element(self, element):
        return element.text in ['Add training', 'Edit training']


class DeleteTrainingPage(Page):
    at_check_locator = (By.ID, 'deleteTrainingModal')

    def btn_delete(self):
        self.click_on_element((By.ID, 'deleteButton'))
        return self

    def at_check_element(self, element):
        return element is not None
