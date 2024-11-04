from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument("start-maximized")


driver = webdriver.Chrome(options = options)
driver.get("https://www.citilink.ru")

time.sleep(2)

input = driver.find_element(By.NAME, "text")
input.send_keys("микрофон")
input.send_keys(Keys.ENTER)

time.sleep(2)
index = 1
page = 1
while True:
    print(f"Страница {page}")
    page+=1

    next = driver.find_element(By.CLASS_NAME, "app-catalog-5p06l4 e1m8swc80")
    # while True:
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='pageToInsert pagination__wrapper']")))
#         cards = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//article[@id]")))
#         count = len(cards)
#         driver.execute_script("window.scrollBy(0,2000)")
#         time.sleep(1)
#         cards = driver.find_elements(By.XPATH, '//article[@id]')
#         if len(cards) == count:
#              break
#         count_old = count


#     # card_items = []

#     for card in cards:
#         card_item = {}
#         card_item["index"] = index
#         index += 1
#         card_item["name"] = card.find_element(By.XPATH, "./div/a").get_attribute("aria-label")
#         card_item["price"] = card.find_element(By.CLASS_NAME,"price__lower-price").text
#         card_item["url"] = card.find_element(By.XPATH, "./div/a").get_attribute("href")
#         print(card_item)

#     # print(card_items)
#     # TODO: Save to database

#     try:
#         # Переключение страниц
#         btn_next = driver.find_element(By.CLASS_NAME, "pagination-next")
#         actions = ActionChains(driver)
#         actions.scroll_to_element(btn_next)
#         actions.perform()
#         btn_next.click()
#     except  Exception as e:
#         print(e)
#         break

print()

