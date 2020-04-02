# coding=utf-8
import smtplib
import os
import tool_
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
    '''% (tool_.get_host_name(),tool_.get_host_ip(),tool_.get_mac_address(),tool_.get_addr_info(),tool_.get_addr())
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

