import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
class BaseDriver:
    def __int__(self, driver):
        self.driver = driver

    # scroll down the page by pixels
    # approach1
    def page_scroll_by_pixels(self):
        self.driver.execute_script("window.scrollBy(0,3000)","")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("nuber of the pixels moved : ", value)

    # scroll down page till the element is visible
    # approach2
    def page_scroll_element_is_visible(self):
        flag = self.driver.find_element(by=By.XPATH, value="//img[@alt='Flag of Pakistan']")
        self.driver.execute_script("arguments[0].scrollIntoView()", flag)
        value = self.driver.execute_script("return window.pageYOffset;")
        print("scroll down page till the element is visible : ", value)

    # scroll down page till the end
    # approach3
    def page_scroll_till_end(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("scroll down page till the end pixels numbers : ", value)
        time.sleep(6)

    # scroll up the page
    # approach 4
    def page_scroll_up(self):
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("scroll up the page : ", value)

    def wait_for_presence_of_all_elements_located(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element

