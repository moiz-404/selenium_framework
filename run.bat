REM pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py
REM pytest -vs -n=2 --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py
REM pytest -vs --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py --html=reports/reports.html
pytest -v -m "sanity and regression  " --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/ --html=reports/report.html
REM pytest -v -m "sanity or regression  " --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/ --html=reports/report.html
REM pytest -v -n=2 --browser chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F testcases/test_nopcommerce.py --html=reports/reports.html

