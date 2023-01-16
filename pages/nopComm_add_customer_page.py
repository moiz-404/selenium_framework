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

class nopComm_Add_Customer(BaseDriver):
    log = Utils.logger()
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    linkCustomers_manu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_manuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_customer_xpath = "//a[normalize-space()='Add new']"

    email_xpath = "//input[@id='Email']"
    password_xpath = "//input[@id='Password']"
    firstName_xpath = "//input[@id='FirstName']"
    lastName_xpath = "//input[@id='LastName']"
    rdGender_Male_id = "Gender_Male"
    rdGender_Female_id = "Gender_Female"
    DateOfBirth_xpath = "//input[@id='DateOfBirth']"
    companyname_xpath = "//input[@id='Company']"
    chkbox_isTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    dd_newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    txt_listitem_newsletters_TestStore_xpath = "//li[contains(text(),'Test store 2')]"
    txt_listitem_newsletter_YourStoreName_xpath = "//li[contains(text(),'Your store name')]"

    customerroles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    txt_listitem_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    txt_listitem_Registered_xpath = "//li[contains(text(),'Registered')]"
    txt_listitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    txt_listitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    dd_Manager_vendor_xpath = " //*[@id='VendorId']"
    chkbox_Active_xpath = "//*[@id='Active']" #"//input[@id='Active']"

    textarea_AdminComment_xpath="//textarea[@id='AdminComment']"
    save_btn_xpath = "//button[@name='save']"


    def clickOnCustomerManu(self):
        res = self.driver.find_element(By.XPATH, self.linkCustomers_manu_xpath)
        res.click()

    def clickOnCustomerManuItem(self):
        res = self.driver.find_element(By.XPATH, self.linkCustomers_manuitem_xpath)
        res.click()

    def clickOnAddNew(self):
        res = self.driver.find_element(By.XPATH, self.add_customer_xpath)
        res.click()

    def setEmail(self, email):
        res = self.driver.find_element(By.XPATH, self.email_xpath)
        res.send_keys(email)

    def setPassword(self, password):
        res = self.driver.find_element(By.XPATH, self.password_xpath)
        res.send_keys(password)

    def setFirstName(self, firstName):
        res = self.driver.find_element(By.XPATH, self.firstName_xpath)
        res.send_keys(firstName)

    def setLastName(self, lastName):
        res = self.driver.find_element(By.XPATH, self.lastName_xpath)
        res.send_keys(lastName)

    def setGender(self, gender):
        if gender == "Male" or gender == "male":
            self.driver.find_element(By.ID, self.rdGender_Male_id).click()
        if gender == "Female" or gender == "female":
            self.driver.find_element(By.ID, self.rdGender_Female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdGender_Male_id).click()


    def setDateOfBirth(self, dateOfBirth):
        res = self.driver.find_element(By.XPATH, self.DateOfBirth_xpath)
        res.send_keys(dateOfBirth)

    def setcompanyname(self, companyname):
        res = self.driver.find_element(By.XPATH, self.companyname_xpath)
        res.send_keys(companyname)

    def clickOnChkboxIsTaxExempt(self):
        res = self.driver.find_element(By.XPATH, self.chkbox_isTaxExempt_xpath)
        res.click()

    def setDdNewsletter(self, role):
        res = self.driver.find_element(By.XPATH, self.dd_newsletter_xpath)
        res.click()
        time.sleep(2)
        if role =='Your store name':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_newsletter_YourStoreName_xpath)
        else:
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleId_taglist']/li/span[2]").click()
            # self.driver.find_element(By.XPATH, "//span[@class='k-icon k-i-close']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_newsletters_TestStore_xpath)

        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.listitem)

    def setcustomerroles(self, role):
        res = self.driver.find_element(By.XPATH, self.customerroles_xpath)
        res.click()
        time.sleep(2)
        if role =='Registered':
            time.sleep(2)
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_Registered_xpath)
        elif role =='Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_Administrators_xpath)
        elif role =='Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_Guests_xpath)
        elif role =='Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.txt_listitem_Guests_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.listitem)


    def setManagerOfVendor(self, value):
        dorpdown_ele = Select(self.driver.find_element(By.XPATH, self.dd_Manager_vendor_xpath))
        dorpdown_ele.select_by_visible_text(value)

    def clickOnChkboxActive(self):
        checkbox = self.driver.find_element(By.XPATH, self.chkbox_Active_xpath)
        act = ActionChains(self.driver)
        act.double_click(checkbox).perform()


    def setAdminComment(self, content):
        time.sleep(3)
        res = self.driver.find_element(By.XPATH, self.textarea_AdminComment_xpath)
        res.send_keys(content)

    def clickOnSaveBtn(self):
        res = self.driver.find_element(By.XPATH, self.save_btn_xpath)
        res.click()
        time.sleep(5)