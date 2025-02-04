import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    service=Service(executable_path="C:\Automation Tools\chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()