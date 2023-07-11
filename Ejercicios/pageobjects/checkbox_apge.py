from selenium.webdriver.common.by import By


class CheckboxPage(object):
    def __int__(self, driver):
        self.check1 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
        self.check2 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")


