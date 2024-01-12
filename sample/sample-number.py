x = '1.039,90 TL'

print(float((x.replace(".","").replace(",",".")).split(" ")[0]))

