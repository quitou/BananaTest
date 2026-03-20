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
    driver_chrom.implicitly_wait(0.3)
    yield driver_chrom
    driver_chrom.quit()


def check_cost_update(driver):
    """Возвращает (минимальная_цена, id_товара) или (inf, None) при ошибке"""
    for _ in range(3):
        try:
            store = WebDriverWait(driver, 0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#store'))
            )
            elements = store.find_elements(By.CSS_SELECTOR, '[id]')

            elements_list = []
            for element in elements:
                try:
                    elem_id = element.get_attribute('id')
                    if elem_id:
                        elements_list.append(elem_id)
                except StaleElementReferenceException:
                    continue

            list_cost = []
            for elem_id in elements_list:
                try:
                    elem = driver.find_element(By.ID, elem_id)
                    price_text = elem.find_element(By.TAG_NAME, 'b').text
                    if ' - ' in price_text:
                        price_str = price_text.split(' - ')[-1].replace(',', '').strip()
                        if price_str:
                            list_cost.append(int(float(price_str)))
                except:
                    continue

            if not list_cost:
                continue

            min_value = min(list_cost)
            id_value = elements_list[list_cost.index(min_value)]
            return min_value, id_value

        except StaleElementReferenceException:
            time.sleep(0.1)  # Короткая пауза перед повторной попыткой
            continue

    return float('inf'), None


def get_current_money(driver):
    try:
        money_el = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#money'))
        )
        raw_money = money_el.text.replace(',', '').strip()
        return int(float(raw_money)) if raw_money else 0
    except:
        return 0


def test_cookies_clicker(driver):
    driver.get('https://orteil.dashnet.org/experiments/cookie/')

    main_cookie = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#cookie'))
    )

    target_money = 50000
    counter = 0
    check_interval = 50  # Проверка магазина каждые 15 кликов (можно менять)

    while get_current_money(driver) < target_money:
        main_cookie.click()
        counter += 1

        # Проверяем магазин строго по интервалу
        if counter >= check_interval:
            cost_store = check_cost_update(driver)

            # Если данные получены успешно — пробуем купить
            if cost_store[1] is not None:
                min_price, item_id = cost_store
                current_money = get_current_money(driver)

                if current_money >= min_price:
                    try:
                        buy_btn = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, item_id))
                        )
                        driver.execute_script("arguments[0].click();", buy_btn)
                        time.sleep(0.05)  # Даём игре время обработать покупку
                    except (TimeoutException, StaleElementReferenceException) as e:
                        print(f"Ошибка покупки: {e}")

            # 🔥 ВАЖНО: сбрасываем счётчик В ЛЮБОМ СЛУЧАЕ, даже если покупка не удалась
            counter = 0

    assert get_current_money(driver) >= target_money