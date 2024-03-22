from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

items = {}
search_keyword = input("Search: ")

def price_search(name,url,search_xpath,titles_css_selector,prices_css_selector,links_css_selector):

    driver = webdriver.Chrome()   
    driver.get(url)

    searchInput = driver.find_element(By.XPATH, search_xpath)

    searchInput.send_keys(search_keyword)
    searchInput.send_keys(Keys.RETURN)

    titles = driver.find_elements(By.CSS_SELECTOR, titles_css_selector)
    prices = driver.find_elements(By.CSS_SELECTOR, prices_css_selector)
    links = driver.find_elements(By.CSS_SELECTOR, links_css_selector)

    for title in titles:
        for link in links:
            for price in prices:
                items[name,title.text,link.get_attribute("href")] = float((price.text.replace(".","").replace(",",".")).split(" ")[0])
                links.remove(link)
                prices.remove(price)
                break
            break
    driver.close()
    return items


n11_values = {
    "name" : "N11",
    "url" : "https://www.n11.com/",
    "search_xpath" : "/html/body/div[1]/header/div/div/div/div[1]/div/div/div[1]/form/input[1]",
    "titles_css_selector" : "h3.productName",
    "prices_css_selector": "span.newPrice",
    "links_css_selector" : "a.plink"
}

price_search(n11_values["name"],
             n11_values["url"],
             n11_values["search_xpath"],
             n11_values["titles_css_selector"],
             n11_values["prices_css_selector"],
             n11_values["links_css_selector"]
             )

trendyol_values = {
    "name" : "Trendyol",
    "url" : "https://www.trendyol.com/",
    "search_xpath" : "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/input",
    "titles_css_selector" : "h3.prdct-desc-cntnr-ttl-w",
    "prices_css_selector": "div.discounted-price-container",
    "links_css_selector" : "div.p-card-chldrn-cntnr a"
}

price_search(trendyol_values["name"],
             trendyol_values["url"],
             trendyol_values["search_xpath"],
             trendyol_values["titles_css_selector"],
             trendyol_values["prices_css_selector"],
             trendyol_values["links_css_selector"]
             )


sorted_items = dict(sorted(items.items(), key= lambda x:x[1]))

{print(key[0]," - ",key[1]," -",key[2],"--- ",value) for key,value in sorted_items.items()}