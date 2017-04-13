from pytractor import webdriver


DRIVER_CHROME = 'chromedriver'


def attach_driver(context):
    """
    Attach a webdriver to the behave context
    Uses behave configuration to select the driver
    :param context: behave context
    """
    context.base_url = context.config.userdata.get('server.url')
    driver_name = context.config.userdata.get('browser.driver', DRIVER_CHROME)
    headless = context.config.userdata.get('browser.headless', 'False')

    if headless == 'True':
        size = [int(s) for s in context.config.userdata.get('browser.size', '1920,1080').split(',')]
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(size[0], size[1]))
        display.start()
        context.display = display

    context.uses_protractor = True
    context.driver = _driver_from_config(driver_name)
    context.driver.maximize_window()


def _driver_from_config(driver_name):
    if driver_name == DRIVER_CHROME:
        return webdriver.Chrome()

    return None


def detach_driver(context):
    context.driver.quit()

    if hasattr(context, 'display'):
        context.display.stop()
