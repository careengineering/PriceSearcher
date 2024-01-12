items = {}



titles = ["aaaa","bbbb","cccc"]
prices = [4.1,2.2,3.3]
links = ["//haaaa","//hbbbb","//hcccc"]

for title in titles:
    for link in links:
        for price in prices:
            items["N11",title,link] = price
            links.remove(link)
            prices.remove(price)
            break
        break

sorted_items = dict(sorted(items.items(), key= lambda x:x[1]))

for key, value in sorted_items.items():
    print(key[0],":",value)



