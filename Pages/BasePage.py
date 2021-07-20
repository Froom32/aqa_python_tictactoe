from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://froom32.github.io/"

    def find_element(self, element_id, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, element_id)),
                                                      message=f"Can't find element by locator {element_id}")

    def click(self, element_id):
        return self.find_element(element_id).click()

    def go_to_site(self):
        return self.driver.get(self.base_url)
