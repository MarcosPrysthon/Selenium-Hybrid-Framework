from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    PATH = 'C:/Users/marcosvn/Documents/studies/ict/chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    return driver