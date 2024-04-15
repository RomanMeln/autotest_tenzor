from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import requests

url = "https://sbis.ru/"
# url = "https://tensor.ru/"
# driver = webdriver.Chrome(executable_path="/Users/roman/PycharmProjects/autotest_tenzor/chromedriver")

# проверка кода страницы
# page_code = request.get(url)
# if page_code.STATUS_CODE == 200:

driver = webdriver.Chrome()



try:
    driver.get(url=url)

    time.sleep(5)
    # сделал переход по страницам
    driver.find_element(By.CLASS_NAME, "sbisru-Header").find_elements(By.TAG_NAME, 'a')[1].click()
    time.sleep(4)
    driver.find_element(By.ID, 'contacts_clients').find_element(By.CSS_SELECTOR, '[title="tensor.ru"]').click()
    # print(driver.window_handles) #страницы
    driver.switch_to.window(driver.window_handles[1]) # переход на страницу тензор
    time.sleep(4)
    # print(driver.current_url) #  проверка перехода на текущую страницу

    # проверка наличия элемента
    power_in_human = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    print(power_in_human.get_attribute('innerHTML'))
    time.sleep(2)
    if 'Сила в людях' in power_in_human.text:
        print(True)
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
        print(f'Ширина: {width_img}, Высота: {height_img}')
    else:
        print('Элемент со сзначением \"Сила в людях\" отсутствует')
        # print(a)

    # a = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-content').get_attribute('innerHTML')
    # print(a)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
