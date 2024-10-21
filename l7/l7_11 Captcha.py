import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

# Использование headless браузера чтобы избежать механизмов обнаружения ботов
options = Options()
options.headless = True

driver = webdriver.Chrome()
driver.get("https://example.com")

# Решение задачи CAPTCHA
captcha_element = driver.find_element(By.ID, "captcha")
captcha_image_src = captcha_element.get_attribute("src")
captcha_image_data = requests.get(captcha_image_src).content

# Использование OCR для решения задачи CAPTCHA
captcha_text = "CAPTCHA_SOLUTION"

captcha_input = driver.find_element(By.XPATH, "//div[@class = 'data-element']")
captcha_input.send_keys(captcha_text)

submit_button = driver.find_element(By.ID, "captcha_input")
submit_button.click()

time.sleep(3)

# Результаты
data = driver.find_elements(By.XPATH, "//div[@class='data-element']")
data_list = []

for item in data:
    data_list.append(item.text)

driver.quit()

print(data_list)