from pathlib import Path

import pytest
from faker import Faker
# import softest
from utilities.utils import Utils
from utilities.readProperties import ReadConfig as rc
from pages.nopcomm_login_page import nopComm_Login_Page
from pages.nopComm_add_customer_page import nopComm_Add_Customer
from pages.nopComm_search_customer_page import nopComm_Search_Customer
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")

# class TestSearchAndVerifyFilter(softest.TestCase):
class Test_Login_001():
    log = Utils.logger()

    useremail = rc.getUserName()
    userpassword = rc.getPassword()

    # datafile = 'testdata.yaml'
    # filedir = 'testdata'
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # DATA_FILE = BASE_DIR.joinpath(filedir).joinpath(datafile)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = nopComm_Login_Page(self.driver)
        self.addcust = nopComm_Add_Customer(self.driver)
        self.sc = nopComm_Search_Customer(self.driver)
        self.ut = Utils()
        self.fake = Faker()

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.parametrize("gf,gt",[("NewDelhi","Mumb")])
    def test_001_nopCommmerce(self):
        self.log.info(" **********>> login <<**********")
        self.lp.nopComm_login_page_title()
        self.lp.Login_Page(self.useremail, self.userpassword)
        self.log.info(" **********>> nopCommmerce login Test successful <<**********")
        self.addcust.clickOnCustomerManu()
        self.log.info(" **********>> Clicking On Customer Manu is successful <<**********")
        self.addcust.clickOnCustomerManuItem()
        self.log.info(" **********>> Clicking On Manu Item Customer is successful <<**********")

        self.sc.setsearchEmail("kiyjcycyhjc676008@gmail.com")
        self.sc.clickOnSearchBtn()
        status = self.sc.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        assert True == status




        # if self.addcust.clickOnAddNew() is False:
        #     self.log.info(" **********>> Clicking On Add New button is unsuccessful <<**********")
        # else:
        #     self.log.info(" **********>> Clicking On Add New button is successful <<**********")
        #
        # self.email = self.fake.email()
        # self.addcust.setEmail(self.email)
        # self.password = self.fake.password()
        # self.addcust.setPassword(self.password)
        # self.addcust.setFirstName("moiz")
        # self.addcust.setLastName("ahmed")
        # self.addcust.setGender("Male")
        # self.addcust.setDateOfBirth("08/18/1995")
        # self.addcust.setcompanyname("pi-tech")
        # self.addcust.clickOnChkboxIsTaxExempt()
        # self.addcust.setDdNewsletter("Test store 2")
        # # self.addcust.setcustomerroles("Guests")# Administrators
        # self.addcust.setManagerOfVendor("Vendor 2")
        # self.addcust.clickOnChkboxActive()
        # self.addcust.setAdminComment("This is for testing....")
        # self.addcust.clickOnSaveBtn()
        #
        # self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        # if "The new customer has been added successfully." in self.msg:
        #     assert True == True
        # else:
        #     assert False == True
        #
        # self.lp.nopComm_Logout_Button()
        self.log.info(" **********>> Ending the nopCommerce Add Customer <<**********")













# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py

# command : pytest -vs -n=2 --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py

# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py --html=reports/reports.html

# command : pytest -v -m "sanity and regression  " --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/ --html=reports/report.html

# command : pytest -v -m "sanity or regression  " --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/ --html=reports/report.html

# command : pytest -v -n=2 --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py --html=reports/reports.html

