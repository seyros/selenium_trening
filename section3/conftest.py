# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(executable_path='C:\chromedriver.exe')
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# объявление нужного языка для Chrome:
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})
# browser = webdriver.Chrome(options=options)

# Для Firefox объявление нужного языка будет выглядеть немного иначе:
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", user_language)
# browser = webdriver.Firefox(firefox_profile=fp)



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path='C:\geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
