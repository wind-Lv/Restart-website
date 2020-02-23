#Zombie_礼弥


#导入模块---------------------------------------------------------------------
import urllib.request
import urllib.parse
import json
import re


#list---------------------------------------------------------------
gvl = []

#请求城市ID-----------------------------------------------------------
def inp():
    sr = input('输入要查询的城市:')
    sr = urllib.parse.quote(sr)

    url = urllib.request.urlopen(f'http://toy1.weather.com.cn/search?cityname={sr}').read().decode("utf-8")

    cityid = re.search(r'("ref":")(\d*?)(~)',url)
    cityid = cityid.group(2)
    
    gvl.append(cityid)


#请求操作-------------------------------------------------------------

def index():
    i = gvl[0]
    i = urllib.parse.quote(i)

    a = urllib.request.urlopen(f'http://t.weather.sojson.com/api/weather/city/{i}').read().decode('utf-8')

    b = json.loads(a)
    
    gvl.append(b)
   

#变量(文字)------------------------------------------------------------
rq = '日期：'
gw = '最高：'
dw = '最低：'
xq = '星期：'
rc = '日出时间：'
rl = '日落时间：'
qi = '空气质量指数：'
fxi = '风向：'
fs = '风力：'
tq = '天气：'
tx = '建议：'
sd = '空气湿度：'
pm = 'PM2.5：'
p10 = 'PM10：'
zl = '质量：'
wd = '℃'


#城市名称
def city():
    
    city =   gvl[1]['cityInfo']['city']
    parent = gvl[1]['cityInfo']['parent']
    print(f'您是不是要查找：{parent} 的 {city} ?')


#实时天气
def real_time():
    shidu   = gvl[1]['data']['shidu']
    pm25    = gvl[1]['data']['pm25']
    pm10    = gvl[1]['data']['pm10']
    quality = gvl[1]['data']['quality']
    wendu   = gvl[1]['data']['wendu']
    ganmao  = gvl[1]['data']['ganmao']

    print(f'{sd}{shidu}\n{pm}{pm25}\n{p10}{pm10}\n{zl}{quality}\n温度：{wendu}{wd}\n{tx}{ganmao}')


#天气预报
#依次为:日期 最高气温 最低气温 星期 日出时间 日落时间 空气质量指数 风向 风力 天气 提醒

def day(s):
    
    ymd =         gvl[1]['data']['forecast'][s]['ymd']
    print(f'------------------------------{ymd}--------------------------------')
    high =        gvl[1]['data']['forecast'][s]['high']
    low =         gvl[1]['data']['forecast'][s]['low']
    week =        gvl[1]['data']['forecast'][s]['week']
    sunrise =     gvl[1]['data']['forecast'][s]['sunrise']
    sunset =      gvl[1]['data']['forecast'][s]['sunset']
    aqi =         gvl[1]['data']['forecast'][s]['aqi']
    fx =          gvl[1]['data']['forecast'][s]['fx']
    fl =          gvl[1]['data']['forecast'][s]['fl']
    tianqi =      gvl[1]['data']['forecast'][s]['type']
    notice =      gvl[1]['data']['forecast'][s]['notice']

    print(f'{rq}{ymd}\n{gw}{high}\n{dw}{low}\n{xq}{week}\n{rc}{sunrise}\n{rl}{sunset}\n{qi}{aqi}\n{fxi}{fx}\n{fs}{fl}\n{tq}{tianqi}\n{tx}{notice}')

    print('\n')
    

#显示城市
def cils():
    city()
    print("\n")


#列出天气(实时)
def ssls():
    print('----------------------------实时天气---------------------------\n')
    real_time()
    print('\n')


#列出天气(预报)


def ls():
    print('----------------------------预报天气---------------------------\n')
    s = 0
    while True:
        try:
            day(s)
            s += 1
        except:
            break


#执行
if __name__ == '__main__':
   inp()
   index()
   cils()
   ssls()
   ls()
   
   input('按Enter以退出')
