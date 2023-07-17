import sys
import urllib.request
from lxml import etree
import json

def bark(handle):
    url = "https://codeforces.com/profile/{}/".format(handle)
    headers = {
        'user-agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    if response.code == 200:
        content = response.read().decode('utf-8')
        tree = etree.HTML(content)
        now = tree.xpath("//div[@class='info']/ul[1]/li[1]/span[1]/text()")
        max = tree.xpath("//div[@class='info']/ul[1]/li[1]//span[@class='smaller']/span[2]/text()")
        contribution = tree.xpath("//div[@class='info']//ul/li[2]/span/text()")
        woof = tree.xpath("//div[@class='user-rank']//span[@class='user-legendary']/text()")
        if contribution == []:
            contribution = tree.xpath("//div[@class='info']//li[1]/span")
            if contribution == []:
                sys.stderr.write("No such handle\n你在狗叫什么呀\n")
        if  not now or max ==[]:
            data ={
                "name":handle
            }
            kun = json.dumps(data)
            sys.stdout.write(kun + "\n")
        else:
            data ={
                "name":handle,
                "rating":int(now[0]),
                "rank":woof[0][:-1]
            }
            kun = json.dumps(data)
            sys.stdout.write(kun+"\n")
    else:
        sys.stderr.write("你是什么烂网络"+str(response.code+"\n"))
    return

def main():
    dog = sys.argv[1:]
    for handle in dog:
        bark(handle.strip())
if __name__ == '__main__':
    main()