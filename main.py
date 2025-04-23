import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/vladivostok/category/svet"
driver.get(url)
time.sleep(3)

lamps = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for lamp in lamps:
    try:
        title = lamp.find_element(By.CSS_SELECTOR, 'span').text
        print(title)
        price = lamp.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        print(price)
        link = lamp.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        print(link)
    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append([title, price, link])

driver.quit()

with open("lamp.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название лампы', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)