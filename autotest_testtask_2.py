from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# import requests

url = "https://sbis.ru/"

# проверка кода страницы
# page_code = request.get(url)
# if page_code.STATUS_CODE == 200:

driver = webdriver.Chrome()

try:
    driver.get(url=url)
    time.sleep(2)

    # сделал переход по страницам
    driver.find_element(By.CLASS_NAME, "sbisru-Header").find_elements(By.TAG_NAME, 'a')[1].click()
    time.sleep(4)

    region = driver.find_elements(By.CLASS_NAME, 'sbis_ru-Region-Chooser')[1].text
    partners_list = driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts-List__col-1')[0].text

    if len(region) > 0:
        if len(partners_list) > 0:
            driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text').click()
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, '[title="Камчатский край"]').click()
            time.sleep(1)

            new_region = driver.find_elements(By.CLASS_NAME, 'sbis_ru-Region-Chooser')[1].text
            new_partner_list = driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts-List__col-1')[0].text
            new_url = driver.current_url
            title = driver.find_element(By.TAG_NAME, 'title').get_attribute('innerHTML')

            if '41' in new_url:
                print('корректное отображение адреса')
            else:
                print('Error address')

            if new_region != region:
                print('region OK')
            else:
                print('адресс не сменился')

            if new_partner_list != partners_list:
                print('new partner list OK!')
            else:
                print('не сменился список партнеров')

            if 'Камчатский' in title:
                print('Камчатский в названии')
            else:
                print('нет такого')

            time.sleep(3)

    time.sleep(1)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
