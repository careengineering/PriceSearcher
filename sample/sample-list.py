item_list = []



titles = ["aaaa","bbbb","cccc"]
prices = [1.1,2.2,3.3]
links = ["haaaa","hbbbb","hcccc"]

if len(titles) == len(prices) and len(titles)==len(links):
    {item_list.append([titles[i],float(prices[i]),links[i]]) for i in range(len(titles))}
else:
    print("sonuçlar farklı")

{print(item[1]) for item in item_list}


