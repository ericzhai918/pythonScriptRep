import urllib
import urllib.request

def get_image(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('001.jpg','wb') as fp:
        fp.write(get_img)
        print('图片下载完成')
    return

url = 'http://img.taopic.com/uploads/allimg/140729/240450-140HZP45790.jpg'
get_image(url) 
