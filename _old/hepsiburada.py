from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

items = {}

search_keyword = "enjoy kedi maması 15"

name="Hepsiburada"
url="https://www.hepsiburada.com"

search_xpath= '/html/body/div[3]/div[2]/div[1]/div/div/div/div[1]/div[3]/div[2]/div/div/div/div/div/div/div[1]/div[2]'

search_css_selector=""

titles_css_selector="h3[data-test-id='product-card-name']"
prices_css_selector="div.moria-ProductCard-gLgbbO"
links_css_selector="a.moria-ProductCard-gyqBb"


driver = webdriver.Chrome()

driver.get(url)

searchInput = driver.find_element(By.XPATH, search_xpath)

searchInput.send_keys(search_keyword)
searchInput.send_keys(Keys.RETURN)

titles = driver.find_elements(By.CSS_SELECTOR, titles_css_selector)


for title in titles:
    print(title.text)


driver.close()

