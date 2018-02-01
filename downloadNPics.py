
import urllib
import urllib.request
import re

def download_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern,repr(html))
    num = 1
    for img in get_img:
        image = download_page(img)
        with open('/data/app/deploy_prod/pic/%s.jpg'%num,'wb') as fp:
            fp.write(image)
            num += 1
            print('正在下载第%s张图片'%(num-1))
    return

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1517467478448_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=frog'
html = download_page(url)
get_image(html)

