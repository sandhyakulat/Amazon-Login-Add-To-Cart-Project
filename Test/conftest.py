from selenium import webdriver
import pytest


@pytest.fixture
def driver_initialization(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://www.amazon.in/")
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    yield
    request.cls.driver.quit()


