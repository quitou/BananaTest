from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_fil_forms(driver):
    driver.get('https://secure-retreat-92358.herokuapp.com/')

    fname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fName"))
    )
    fname.send_keys('Alex')
    lname = driver.find_element(By.NAME, "lName")
    lname.send_keys('Gorb')
    email = driver.find_element(By.NAME, "email")
    email.send_keys('it.obl@yandex.ru')
    button = driver.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert success_message.text == 'Success!'