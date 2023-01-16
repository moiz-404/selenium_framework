from pathlib import Path

import pytest

# import softest
from utilities.utils import Utils
from utilities.readProperties import ReadConfig as rc
from pages.nopcomm_login_page import nopComm_Login_Page


@pytest.mark.usefixtures("setup")
# class TestSearchAndVerifyFilter(softest.TestCase):
class Test_Login_ddt_001():
    log = Utils.logger()

    datafile = 'testdata.xlsx'
    filedir = 'testdata'
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_FILE = BASE_DIR.joinpath(filedir).joinpath(datafile)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = nopComm_Login_Page(self.driver)
        self.ut = Utils()

    # @pytest.mark.parametrize("gf,gt",[("NewDelhi","Mumb")])
    def test_001_nopCommmerce_login_DDT(self):
        self.lp.nopComm_login_page_title()
        self.log.info(" **********>> n success <<**********")
        self.log.info(" **********>> nopCommmerce login DDT test<<**********")

        self.rows =self.ut.getRowCount(self.DATA_FILE, 'Sheet1')
        print("Number of Rows in Excel file :", self.rows)

        expacted_status_list=[]
        for r in range(2, self.rows+1):
            self.useremail =self.ut.readData(self.DATA_FILE, 'Sheet1', r, 1)
            self.userpassword =self.ut.readData(self.DATA_FILE, 'Sheet1', r, 2)
            self.expacted =self.ut.readData(self.DATA_FILE, 'Sheet1', r, 3)

            self.lp.Login_Page(self.useremail, self.userpassword)
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.expacted == "Pass":
                    self.log.info(" **********>> passed <<**********")
                    assert True
                    self.lp.nopComm_Logout_Button()
                    expacted_status_list.append("Pass")
                elif self.expacted == "Fail":
                    self.log.info(" **********>> failed <<**********")
                    assert True
                    self.lp.nopComm_Logout_Button()
                    expacted_status_list.append("Fail")

            elif act_title != "Dashboard / nopCommerce administration":
                if self.expacted == "Pass":
                    self.log.info(" **********>> failed <<**********")
                    expacted_status_list.append("Fail")

                elif self.expacted == "Fail":
                    self.log.info(" **********>> passed <<**********")
                    expacted_status_list.append("Pass")

        if "Fail" not in expacted_status_list:
            self.log.info(" **********>> login DDT test passed <<**********")
            assert True
        else:
            self.log.info(" **********>> login DDT test failed <<**********")

            assert False

        self.log.info(" **********>> End of login DDT Test <<**********")
        self.log.info(" **********>> Completed Test_Login_ddt_001  <<**********")

# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py

# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py --html=reports/reports.html