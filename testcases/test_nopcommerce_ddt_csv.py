from pathlib import Path

import pytest

# import softest
from utilities.utils import Utils
from utilities.readProperties import ReadConfig as rc
from pages.nopcomm_login_page import nopComm_Login_Page


@pytest.mark.usefixtures("setup")
# class TestSearchAndVerifyFilter(softest.TestCase):
class Test_Login_ddt_CSV_001():
    log = Utils.logger()
    datafile = 'testdata.csv'
    filedir = 'testdata'
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_FILE = BASE_DIR.joinpath(filedir).joinpath(datafile)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = nopComm_Login_Page(self.driver)
        self.ut = Utils()

    @pytest.mark.parametrize("useremail, userpassword, expacted", Utils.readAllDataFromcsv(DATA_FILE))
    def test_001_nopCommmerce_login_DDT(self, useremail, userpassword, expacted):
        self.log.info(" **********>> nopCommmerce login DDT CSV test<<**********")
        expacted_status_list=[]

        self.lp.Login_Page(useremail, userpassword)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            if expacted == "Pass":
                self.log.info(" **********>> passed <<**********")
                self.lp.nopComm_Logout_Button()
                expacted_status_list.append("Pass")
            elif expacted == "Fail":
                self.log.info(" **********>> failed <<**********")
                self.lp.nopComm_Logout_Button()
                expacted_status_list.append("Fail")

        elif act_title != "Dashboard / nopCommerce administration":
            if expacted == "Pass":
                self.log.info(" **********>> failed <<**********")
                expacted_status_list.append("Fail")

            elif expacted == "Fail":
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


# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce_ddt_csv.py

# command : pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce_ddt_csv.py --html=reports/reports.html