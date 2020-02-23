import random

with open("E:/work/project/website/data_lib/quotes.txt",'r',encoding="utf-8") as f:
    a = f.read()
b = eval(a)

def number(): 
    nums = random.randint(0,149)
    return nums

def quotes(num):
    nums = number()
    quo = b["data"][nums]
    return quo

if __name__ == "__main__":
    nums = number()
    print(quotes(nums))