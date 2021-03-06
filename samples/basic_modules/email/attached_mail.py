# -*-coding:utf-8-*-

import smtplib
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

'''
编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，
因为如果包含中文，需要通过Header对象进行编码。
'''


def _format_addr(s):
    name, addr = parseaddr(s)
    print parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


from_addr = 'wgp3033@163.com'
password = raw_input('Password: ')  # 1****
to_addr = 'yoursunlight@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个文件:
with open('F:\google.csv', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('None', 'csv', filename='google.csv')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
