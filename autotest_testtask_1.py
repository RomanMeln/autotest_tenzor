from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://sbis.ru/"


def test_tests_task_1():
    driver = webdriver.Chrome()
    driver.get(url=url)

    time.sleep(5)
    # поиск и переход на страницу контакты
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sbisru-Header"))
    ).find_elements(By.TAG_NAME, 'a')[1].click()

    # поиск и активация элемента тензор
    driver.find_element(By.ID, 'contacts_clients').find_element(By.CSS_SELECTOR, '[title="tensor.ru"]').click()

    # переход на страницу тензор
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    # поиск и проверка наличия элемента
    power_in_human = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    text_power_in_human = power_in_human.text
    time.sleep(2)
    if 'Сила в людях' in text_power_in_human:
        power_in_human.find_element(By.XPATH, '//a[@href="/about"]').click()
        img = driver.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image')

        width_img = 0
        height_img = 0
        for i in img:
            width = i.get_attribute('width')
            height = i.get_attribute('height')
            if width_img == width:
                continue
            elif 0 < width_img != width:
                print('Ширина отличается.')
                continue
            else:
                width_img = width

            if height_img == height:
                continue
            elif 0 < height_img != height:
                print('Высота отличается.')
                continue
            else:
                height_img = height

            assert width_img == width
            assert height_img == height
        print(f'Ширина: {width_img}, Высота: {height_img}')
    else:
        print('Элемент со сзначением \"Сила в людях\" отсутствует')

    assert 'Сила в людях' in text_power_in_human

    time.sleep(3)

    driver.close()
    driver.quit()


if __name__ == '__main__':
    test_tests_task_1()
