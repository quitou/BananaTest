from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
# options.add_argument('start-maximized') # -развернуть на весь экран, через параметры
# options.add_argument('--window-size=500,1080') # - задаём определённый размер, через параметры
# options.add_experimental_option('detach',True) # - не закрывает хром после отработки программы.
# удобно когда пишем тесты
driver = webdriver.Chrome(options=options)

# driver.maximize_window() -развернуть на весь экран
# driver.set_window_size(500,1080) - задаём определённый размер
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
search_input_button = driver.find_element(By.NAME, 'btnK')
search_input_button.click()
print(driver.title)

sleep(3)