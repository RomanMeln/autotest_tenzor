from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def get_region(use_driver):
    # region = use_driver.find_elements(By.CLASS_NAME, 'sbis_ru-Region-Chooser')[1].text
    region = WebDriverWait(use_driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'sbis_ru-Region-Chooser'))
    )[1].text
    return region


def get_partners_list(use_driver):
    return WebDriverWait(use_driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'sbisru-Contacts-List__col-1'))
    )[0].text


url = "https://sbis.ru/"


def test_tests_task_2():
    driver = webdriver.Chrome()
    driver.get(url=url)

    # поиск и переход на страницу контакты
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sbisru-Header"))
    ).find_elements(By.TAG_NAME, 'a')[1].click()

    # поиск и определение региона и листа партнеров
    region = get_region(driver)
    partners_list = get_partners_list(driver)

    if len(region) > 0:
        if len(partners_list) > 0:
            # активировать элемент название региона
            driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text').click()
            # WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, 'sbis_ru-Region-Chooser__text'))
            # ).click()
            time.sleep(2)

            # выбор камчатского края в открывшемся окне
            driver.find_element(By.CSS_SELECTOR, '[title="Камчатский край"]').click()
            # WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Камчатский край"]'))
            # ).click()
            time.sleep(2)


            # определение региона, листа партнеров, текущего url, title
            new_region = get_region(driver)
            new_partner_list = get_partners_list(driver)
            new_url = driver.current_url
            title = driver.title

            assert len(region) > 0
            assert len(partners_list) > 0
            assert '41' in new_url
            assert new_region != region
            assert new_partner_list != partners_list
            assert 'Камчатский' in title

    driver.close()
    driver.quit()


if __name__ == '__main__':
    test_tests_task_2()
