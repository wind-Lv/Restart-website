from string import digits
with open('E:\work\project\website\data_lib\quotes.txt','r',encoding="utf-8") as f:
    a = f.read()

remove_digits = str.maketrans('', '', digits)
res = a.translate(remove_digits)
pp = res.replace("\n",'').replace('.','"').replace(" ",'",')
print(pp)
