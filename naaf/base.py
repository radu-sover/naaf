from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Page:
    """
    URL where the Page is found
    At_check_locator, if exists, a check_at_element should be implemented to test the element found by locator
    """
    url = None
    at_check_locator = None

    def __init__(self, context):
        self.context = context
        self.driver = context.driver

    # region Fluent Actions
    def navigate(self):
        self.driver.get(self.context.base_url + self.url)
        return self

    def click_on_element(self, locator):
        self.wait_for_element_present(locator)
        self.driver.find_element(*locator).click()
        return self

    def click_on_element_ac(self, locator):
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element_with_offset(element, 0, 20).click().perform()
        return self

    def send_keys_on_element(self, locator, text):
        self.wait_for_element_present(locator)
        self.driver.find_element(*locator).send_keys(text)
        return self

    def select_option_on_element(self, locator, option_text):
        self.wait_for_element_present(locator)
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(option_text)
        return self

    def wait_for_element_present(self, element, seconds=20):
        if self.context.uses_protractor:
            # protractor waits for elements by default
            return self

        # read more on the http://selenium-python.readthedocs.io/waits.html#waits
        WebDriverWait(self.driver, seconds).until(
            expected_conditions.presence_of_element_located(element))
        return self
    # endregion

    # region Tell/Get Something
    def at(self):
        url_match = False
        check_match = False

        if getattr(self, 'url'):
            url_match = self.context.base_url + self.url == self.driver.current_url
        else:
            url_match = True

        if getattr(self, 'at_check_locator'):
            element = self.get_element(self.at_check_locator)
            check_match = self.at_check_element(element)
        else:
            check_match = True

        return url_match and check_match

    def at_check_element(self, element):
        return element is not None

    def get_element(self, locator):
        self.wait_for_element_present(locator)
        return self.driver.find_element(*locator)
    # endregion


class CurrentPage:
    def __init__(self, context):
        self.context = context
        self.driver = context.driver

    def __call__(self):
        return self.driver

    def __getattr__(self, name):
        attr = getattr(self.driver, name)
        if not attr:
            raise AttributeError

        return attr

    def __iter__(self):
        return iter(self.driver.page_source)

    def wait(self, seconds=5):
        sleep(seconds)
        return self
