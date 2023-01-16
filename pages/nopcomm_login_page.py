import logging
import time
import requests
import os
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC

class nopComm_Login_Page(BaseDriver):
    log = Utils.logger()
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    nopcomm_login_email_xpath = "//input[@id='Email']"
    nopcomm_login_password_xpath = "//input[@id='Password']"
    nopcomm_login_button_xpath = "//button[normalize-space()='Log in']"
    nopcomm_logout_linktest = "Logout"

    def nopComm_login_page_title(self):
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.log.info(" **********>> verifying nopCommerce login page title is success <<**********")
        else:
            self.driver.save_screenshot("./screenshots/"+"nopComm_login_page_title.png")
            self.log.error(" **********>> verifying nopCommerce login page title is failed <<**********")
            assert False

    def nopComm_Email(self, email):
        self.driver.find_element(By.XPATH, self.nopcomm_login_email_xpath).clear()
        res = self.driver.find_element(By.XPATH, self.nopcomm_login_email_xpath)
        res.send_keys(email)
        self.log.info(" **********>> entring email is successfull <<**********")

    def nopComm_Password(self, password):
        self.driver.find_element(By.XPATH, self.nopcomm_login_password_xpath).clear()
        res = self.driver.find_element(By.XPATH, self.nopcomm_login_password_xpath)
        res.send_keys(password)
        # res.send_keys(Keys.ENTER)
        self.log.info(" **********>> entring password is successfull <<**********")

    def nopComm_Login_Button(self):
        res = self.wait_element_to_be_clickable(By.XPATH, self.nopcomm_login_button_xpath)
        res.click()

    def nopComm_Logout_Button(self):
        res = self.wait_element_to_be_clickable(By.LINK_TEXT, self.nopcomm_logout_linktest)
        res.click()

    def Login_Page(self, email, password):
        self.nopComm_Email(email)
        self.nopComm_Password(password)
        self.nopComm_Login_Button()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info(" **********>> Login Page to Dashboard is success <<**********")
        else:
            # self.driver.save_screenshot("./screenshots/"+"Login_Page_to_Dashboard.png")
            self.log.error(" **********>> Login Page to Dashboard is faild <<**********")
            assert False




     # def searches(self,):
        # res = self.driver.find_element(By.XPATH, self.)
        # res.click()
        # res.send_keys()
        # res.send_keys(Keys.ENTER)
        # self.log.info("")





    # def select_Date(self,  ):
        # approach1
        # driver.find_element(By.XPATH, " ").send_keys("05/30/2022")

        # approach2
        # self.wait_element_to_be_clickable(By.XPATH, self.).click()
        # time.sleep(3)
        # all_dates = self.wait_element_to_be_clickable(By.XPATH, self. ).find_elements(By.XPATH, self. )
        # for date in all_dates:
            # if date.get_attribute(" ") == :
            #     date.click()
            #     self.log.info("selected dste :" + date.text)
            #     break

        # approach3
        # year = '2021'
        # month = 'December'
        # date = '10'
        # self.wait_element_to_be_clickable(By.XPATH, self. ).click()
        # time.sleep(3)
        # while True:
        #     mon = self.driver.find_element(By.XPATH, self.).text
        #     yr = self.driver.find_element(By.XPATH, self. ).text
        #     if mon == month and yr == year:
        #         break
            # elif mon != month and yr != year:
            # else:
                # driver.find_element(By.XPATH, self. ).click() #next arrow
                # self.driver.find_element(By.XPATH, self. ).click()  # previous arrow

        # dates = self.driver.find_elements(By.XPATH, self. )
        # for ele in dates:
        #     if ele.text == date:
        #         ele.click()
        #         break
