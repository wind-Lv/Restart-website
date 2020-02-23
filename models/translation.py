import urllib.request
import urllib.parse
import json

print('中英互译')

while True:
    i = input('>>>')

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    hear = {}
    hear['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    
    data ={}
    data['i'] = i
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15552264644984'
    data['sign'] = 'dd5843f78e2e5f4762e0d6d61cd96a25'
    data['ts'] ='1555226464498'
    data['bv'] = '6945a57e1923a3517303cdcdb2d3d15e'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] ='FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8')

    a = urllib.request.urlopen(url,data).read().decode('utf-8')
   

    gay = json.loads(a)
    guy = gay['translateResult'][0][0]['tgt']

    print(guy)

