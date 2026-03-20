from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # импорт всех клавишь в системе
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    sleep(3)
    chrome_driver.quit()

def test_id_name(driver):
    input_data = 'привет'
    driver.get('https://ya.ru/')
    text_string = driver.find_element(By.ID, 'text')
    text_string.send_keys(input_data)
    #text_string.submit() # просим форму form отправить текст
    text_string.send_keys(Keys.ENTER) # используем клавишу Enter для ввода
    # result_text = driver.find_element(By.NAME, 'text') # пока что не работает из-за того, что страница перезагружается
    # assert result_text.text == input_data


def test_class_name(driver):
    input_data = 'привет'
    driver.get('https://ya.ru/')
    text_string = driver.find_element(By.CLASS_NAME, 'mini-suggest__input') # поиск по классу
    # но класс может содержать несколкьо методов внутри надо указывать 1 метод при поиске
    text_string.send_keys(input_data)

def test_teg_name(driver):
    driver.get('https://ya.ru/')
    text_h1 = driver.find_element(By.TAG_NAME, 'h1')
    print(text_h1.text) # 1 вариант распечатки результата поиска просто через .text может не сработать и
    print(text_h1.get_attribute('innerText')) # 2 вариант распечатки результата поиска через .get_attribute('innerText')

def test_link(driver):
    driver.get('https://ya.ru/')
    medic = driver.find_element(By.LINK_TEXT, 'Медицина') # поиск по названию ссылки
    # medic = driver.find_element(By.PARTIAL_LINK_TEXT, 'Медиц') # поиск по частичному названию ссылки
    medic.click()
    # assert driver.find_element(By.TAG_NAME, 'h1').text == 'Поиск по врачам и клиникам в Архангельске'
    # Проблема: Элемент не успел загрузиться

def test_css_selector(driver):
    driver.get('https://ya.ru/')
    money = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]')
    # text_string = driver.find_element(By.CSS_SELECTOR, '.mini-suggest__input')  # поиск по классу через cелектор
    # text_string = driver.find_element(By.CSS_SELECTOR, '#text') # поиск по id через cелектор
    # если нету id или name ,то можем искать по уникальному css селектору
    # money.click()
    print(money.value_of_css_property('border-color'))
    assert money.get_dom_attribute('data-statlog') == '2informers.stocks.item.300000000101470118'

def test_xpath(driver):
    driver.get('https://ya.ru/')
    money = driver.find_element(By.XPATH, '//*[@data-statlog="2informers.stocks.item.300000000101470118"]')
    # text_string = driver.find_element(By.CSS_SELECTOR, '.mini-suggest__input')  # поиск по классу через cелектор
    # text_string = driver.find_element(By.CSS_SELECTOR, '#text') # поиск по id через cелектор
    # если нету id или name ,то можем искать по уникальному css селектору
    money.click()