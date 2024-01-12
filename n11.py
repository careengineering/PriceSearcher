from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

items = {}

search_keyword = "enjoy kedi maması 15"

driver = webdriver.Chrome()

# N11
driver.get("https://www.n11.com/")
searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/div/div[1]/div/div/div[1]/form/input[1]")

searchInput.send_keys(search_keyword)
searchInput.send_keys(Keys.RETURN)

titles = driver.find_elements(By.CSS_SELECTOR, 'h3.productName')
prices = driver.find_elements(By.CSS_SELECTOR, 'span.newPrice')
links = driver.find_elements(By.CSS_SELECTOR, 'a.plink')

for title in titles:
    for link in links:
        for price in prices:
            items["N11",title.text,link.get_attribute("href")] = float((price.text.replace(".","").replace(",",".")).split(" ")[0])
            links.remove(link)
            prices.remove(price)
            break
        break


sorted_items = dict(sorted(items.items(), key= lambda x:x[1]))

{print(key[0]," - ",key[1]," -",key[2],"--- ",value) for key,value in sorted_items.items()}

driver.close()

