import os


class Screenshot:
    def __init__(self, context, features_root_dir, dir_name):
        self.counter = 0
        self.driver = context.driver
        self.screenshot_dir = os.path.join(features_root_dir, dir_name)
        if not os.path.exists(self.screenshot_dir):
            os.mkdir(self.screenshot_dir)

    def _increment(self):
            self.counter += 1
            return self.counter

    def capture(self, file_name):
        file_path = os.path.join(self.screenshot_dir, '{:04d}-{}.png'.format(self._increment(), file_name))
        self.driver.save_screenshot(file_path)
