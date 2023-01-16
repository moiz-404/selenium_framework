
import os.path
from datetime import datetime

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager
import requests
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver as uc

from utilities.utils import Utils


@pytest.fixture(scope="class")
def setup(request, browser, url):
    mylocation = "./reports"
    log = Utils.logger()
    if browser == "chrome":
        # download file in deesired location
        mylocation = {"download.default_directly":"/home/moiz/Downloads/"}
        # for pdf
        mylocation = {"download.default_directly":"~/home/moiz/Downloads/", "plugins.always_open_pdf_externally":True}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs", mylocation)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ops)
        # undetected
        # ops = uc.ChromeOptions()
        # ops.add_experimental_option("prefs", mylocation)
        # driver = uc.Chrome(options=ops)
        log.info(" **********>> Lunching chrome browser <<**********")

    elif  browser == "firefox":
        # setting for download
        ops = webdriver.FirefoxOptions()
        # mine type file
        ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "appliaction/pdf")
        ops.set_preference("browser.download.manager.showWhenStarting", False)
        # download file in deesired location
        ops.set_preference("browser.download.folderList", 2)  # 0 = desktop, 1 = download folder, 2 = desired loaction
        ops.set_preference("browser.download.dir", mylocation)
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=ops)
        log.info(" **********>> Lunching Firefox browser <<**********")
    else:
        log.error(" **********>> Lunching browser failed <<**********")

    driver.get(url)
    # driver.maximize_window()
    # driver.implicitly_wait(15)
    request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


#################  hookes  ####################
def pytest_html_report_title(report):
    report.title = "nopCommerce"


def pytest_configure(config):
    config._metadata["Project Name"] = "nopCommerce"
    config._metadata["Module Name"] = "login"
    config._metadata["Tester Name"] = "moiz"
    config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + " Report.html"

# @pytest.mark.optionalhook
# # def pytest_metadata(metadata):
# #     metadata.pop("JAVA_HOME", None)
# #     metadata.pop("Plugins", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            feature_request = item.funcargs["request"]
            driver = feature_request.getfixturevalue("setup")
            # only add additional html on failure
            # report_directory = os.path.dirname(item.config.option.htmlpath)
            screenshots_directory = "./screenshots"
            file_name = report.nodeid.replace("::", "_")+".png"
            # file_name = str(int(round(time.time()*1000)))+".png"
            destinationfile = os.path.join(screenshots_directory, file_name)
            driver.save_screenshot(destinationfile)
            # screenshots = destinationfile
            # if file_name:
            #     html = '<div><img src="%s" alt="screenshot" style ="width:300px;height=200px" ' \
            #            'onclick="window.open(this.src)" align="right"></div>'%file_name
            extra.append(pytest_html.extras.html("<div></div>"))
        report.extra = extra
