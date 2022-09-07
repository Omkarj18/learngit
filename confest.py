
import pytest
from selenium import webdriver
import time
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")      ## decorator to create fixture and can be used on class level
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")   #pytest --browser_name "firefox"

     # parameter which can be passed with pytest command
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    else:
        driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
