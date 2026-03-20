from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # импорт всех клавишь в системе
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(5) # - ожидание пока страница загрузится (сек) он ждёт пока элемент не появится не дольше
    yield chrome_driver
    sleep(3)
    chrome_driver.close()


def test_clear(driver):
    input_data = "Я люблю питон"
    driver.get('https://ya.ru/')
    text_string = driver.find_element(By.ID, 'text')
    text_string.send_keys(input_data)
    sleep(2)
    # text_string.clear() бывает не срабатывает по этому решение ниже
    entered_value = text_string.get_attribute('value')
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()

def test_enabled_and_select(driver):
    driver.get('https://seleniumbase.io/demo_page')

    select = driver.find_element(By.ID, 'mySelect')
    dropdown = Select(select)
    print(dropdown.first_selected_option.text)
    dropdown.select_by_value('75%')
    print(dropdown.first_selected_option.text)
    # в уроке пример с селектором и активной / не активной кнопкой. Я такую форму на др. сайте не нашёл
    # def test_enabled_and_select(driver):
    #     driver.get('https://www.qa-practice.com/elements/button/disabled')
    #     button = driver.find_element(By.NAME, 'submit')
    #     print(button.is_enabled())
    #     select = driver.find_element(By.ID, 'id_select_state')
    #     dropdown = Select(select)
    #     dropdown.select_by_value('enabled')
    #     print(button.is_enabled())

def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()

def test_cart(driver): # не работает в примере вообще по другому написано
    driver.get('https://www.zazzle.com/owasp_hooded_sweatshirt_choose_your_color-235391306213516420')
    select = driver.find_element(By.ID,'Level1Droplist-droplist2')
    size = driver.find_element(By.ID, 'DroplistPalette_option_1_a_m')
    add_cart = driver.find_element(By.CSS_SELECTOR, '.AddToCartButton')
    select.click()
    size.click()
    add_cart.click()
    #WebDriverWait(driver, 5).until(EC.element_to_be_clickable( ))
    cart = driver.find_element(By.CSS_SELECTOR,'.Header2021RightContent_cartCount')
    assert cart.text == '1'

def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()
    driver.add_cookie({'name': 'testname', 'value': 'testvalue'})
    print(driver.get_cookies())

# пример с товарами их 12 шт. и они возращаются, как список
def test_same_elements(driver): # работать не будет, сайт не доступен
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(2)
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[0].text)
    print(product_link[-1].text)

# пример с товарами их 12 шт. и они возращаются, как список. Берём данные из самих товаров
def test_same_cards(driver): # работать не будет, сайт не доступен
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(2)
    product_cards = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    for card in product_cards:
        print(card.find_element(By.CLASS_NAME, 'price').text)
    # print(product_cards[0].find_element(By.CLASS_NAME, 'price').text)