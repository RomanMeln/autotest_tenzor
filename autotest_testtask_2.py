from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def get_region(use_driver):
    region = use_driver.find_elements(By.CLASS_NAME, 'sbis_ru-Region-Chooser')[1].text
    return region


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
    partners_list = driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts-List__col-1')[0].text

    if len(region) > 0:
        if len(partners_list) > 0:
            # активировать элемент название региона
            driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text').click()
            time.sleep(5)

            # выбор камчатского края в открывшемся окне
            driver.find_element(By.CSS_SELECTOR, '[title="Камчатский край"]').click()
            time.sleep(5)

            # определение региона, листа партнеров, текущего url, title
            new_region = get_region(driver)
            new_partner_list = driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts-List__col-1')[0].text
            new_url = driver.current_url
            title = driver.find_element(By.TAG_NAME, 'title').get_attribute('innerHTML')

            assert len(region) > 0
            assert len(partners_list) > 0
            assert '41' in new_url
            assert new_region != region
            assert new_partner_list != partners_list
            assert 'Камчатский' in title

    time.sleep(1)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    test_tests_task_2()
