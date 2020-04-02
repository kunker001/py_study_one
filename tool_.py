import uuid
import requests
import socket




def get_host_name():
    #获取本机电脑名
    myname = socket.getfqdn(socket.gethostname())
    return myname

def get_host_ip():
    #获取本机ip
    myaddr = socket.gethostbyname(get_host_name())
    return myaddr 


#获取mac
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

#获取经纬度信息
def get_addr_info():
    try:
        html = requests.get("http://ip-api.com/json",timeout=2).text
        return html
    except:
        return 'error'
    return ''

#获取地址
def get_addr():
    try:
        html = requests.get("http://pv.sohu.com/cityjson",timeout=2).text
        return html
    except:
        return 'error'
    return ''
    # city_info=requests.get('http://pv.sohu.com/cityjson',timeout=2)
    # print(city_info.text)
    # addr=city_info.split('=')[1].split(',')[2].split('"')[3] #取出地址信息

#判断是否有网
def isConnected():
    try:
        html = requests.get("http://www.baidu.com",timeout=2)
    except:
        return False
    return True    