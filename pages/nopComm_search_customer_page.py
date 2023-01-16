import logging
import time
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC

class nopComm_Search_Customer(BaseDriver):
    log = Utils.logger()

    txt_search_Email_xpath = "//input[@id='SearchEmail']"
    txt_FirstName_id = "SearchFirstName"
    txt_LastName_id = "SearchLastName"
    search_Btn_xpath = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def setsearchEmail(self, email):
        time.sleep(3)
        res = self.driver.find_element(By.XPATH, self.txt_search_Email_xpath)
        res.send_keys(email)

    def setFirstName(self, firstName):
        time.sleep(3)
        res = self.driver.find_element(By.ID, self.txt_FirstName_id)
        res.send_keys(firstName)

    def setLastName(self, lastName):
        time.sleep(3)
        res = self.driver.find_element(By.ID, self.txt_LastName_id)
        res.send_keys(lastName)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def clickOnSearchBtn(self):
        res = self.driver.find_element(By.XPATH, self.search_Btn_xpath)
        res.click()
        time.sleep(5)

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if emailid == name:
                flag = True
                break
        return flag

