from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

items = {}

search_keyword = "enjoy kedi maması 15"

driver = webdriver.Chrome()

# Trendyol
driver.get("https://www.trendyol.com/")
searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/input")

searchInput.send_keys(search_keyword)
searchInput.send_keys(Keys.RETURN)

titles = driver.find_elements(By.CSS_SELECTOR, 'h3.prdct-desc-cntnr-ttl-w')
prices = driver.find_elements(By.CSS_SELECTOR, 'div.discounted-price-container')
links = driver.find_elements(By.CSS_SELECTOR, 'div.p-card-chldrn-cntnr a')

for title in titles:
    for link in links:
        for price in prices:
            items["Trendyol",title.text,link.get_attribute("href")] = float((price.text.replace(".","").replace(",",".")).split(" ")[0])
            links.remove(link)
            prices.remove(price)
            break
        break


sorted_items = dict(sorted(items.items(), key= lambda x:x[1]))

{print(key[0]," - ",key[1]," -",key[2],"--- ",
       value) for key,value in sorted_items.items()}

driver.close()

