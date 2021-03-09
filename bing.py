import requests
import os,getpass
from bs4 import BeautifulSoup
import time



def getHTMLText(url):
    '''
	此函数用于获取网页的html文档
	'''
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return'产生异常'

def getCurTime():
    curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return curTime

def main():
    '''
	主函数
	'''
    #目标网页
    url='https://cn.bing.com/'


    #工作环境准备
    username=getpass.getuser()
    workpath=''
    if username=='root':
        workpath='/root/Bing'
    else:
        workpath='/home/'+username+'/Bing'
    picpath=workpath+'/picture'

    if not os.path.exists(workpath):
        os.mkdir(workpath)

    if not os.path.exists(picpath):
        os.mkdir(picpath)
    
    demo=getHTMLText(url)
    print(getCurTime())
    print("执行中...")
    #解析HTML代码
    soup=BeautifulSoup(demo,'html.parser')
	#得到图片网址
    pic=url+soup.find(id='bgLink').get('href')
	#获得图片名字
    name=soup.find(id='sh_cp').get('title')
    #将名字中的/替换
    name=name.replace('/','_',5)
	
    name=picpath+'/'+name+'.jpg'
    r=requests.get(pic)
    with open(name,'wb')as f:
        f.write(r.content)
    print("完成!","\n\n\n")


if __name__ == '__main__':
    main()
	