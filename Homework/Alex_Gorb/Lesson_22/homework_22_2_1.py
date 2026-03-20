from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time


@pytest.fixture()
def driver():
    driver_chrom = webdriver.Chrome()
    yield driver_chrom
    driver_chrom.quit()


def get_current_money(driver):
    try:
        # Ждем, пока текст обновится, чтобы избежать чтения промежуточных значений
        money_el = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#money'))
        )
        raw_money = money_el.text.replace(',', '').strip()
        # Обработка случаев, когда число с точкой или пустое
        return int(float(raw_money)) if raw_money else 0
    except:
        return 0


def try_buy_best_item(driver):
    """
    Пытается купить самый дешевый доступный товар.
    Возвращает True, если покупка успешна, иначе False.
    """
    try:
        store = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#store'))
        )
        # Ищем все товары, у которых есть ID
        elements = store.find_elements(By.CSS_SELECTOR, '[id]')

        best_item = None
        min_price = float('inf')

        for element in elements:
            elem_id = element.get_attribute('id')
            if not elem_id:
                continue

            try:
                # Ищем цену внутри элемента (обычно в теге <b>)
                price_text = element.find_element(By.TAG_NAME, 'b').text
                if ' - ' in price_text:
                    price_str = price_text.split(' - ')[-1].replace(',', '').strip()
                    current_price = int(float(price_str))

                    # Ищем самый дешевый товар, который мы можем себе позволить
                    if current_price < min_price:
                        min_price = current_price
                        best_item = (elem_id, current_price, element)
            except:
                continue

        # Если нашли подходящий товар, пытаемся купить
        if best_item and get_current_money(driver) >= min_price:
            elem_id, price, element = best_item
            # Кликаем по самому элементу товара, это надежнее, чем искать вложенные кнопки
            element.click()
            # Небольшая пауза для обработки анимации покупки игрой
            time.sleep(0.1)
            return True

    except StaleElementReferenceException:
        # Если элементы обновились, просто пробуем снова в следующем цикле
        pass
    except Exception as e:
        print(f"Ошибка при покупке: {e}")

    return False


def test_cookies_clicker(driver):
    driver.get('https://orteil.dashnet.org/experiments/cookie/')

    # Ждем загрузки основного куки
    main_cookie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#cookie'))
    )

    target_money = 500
    clicks_since_last_buy = 0

    while get_current_money(driver) < target_money:
        main_cookie.click()
        clicks_since_last_buy += 1

        # Проверяем магазин КАЖДЫЙ клик (или можно раз в 5-10 кликов для производительности)
        # Это гарантирует, что мы не пропустим момент покупки
        if clicks_since_last_buy >= 1:
            if try_buy_best_item(driver):
                clicks_since_last_buy = 0  # Сбрасываем счетчик после успешной покупки

        # Защита от бесконечного цикла, если игра зависла
        if clicks_since_last_buy > 1000:
            break

    final_money = get_current_money(driver)
    print(f"Финальный счет: {final_money}")
    assert final_money >= 500