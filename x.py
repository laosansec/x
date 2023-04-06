
import requests
import threading
from tkinter import *

def get_title(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            title = r.text.split('<title>')[1].split('</title>')[0]
            return title
        else:
            return 'Error ' + str(r.status_code)
    except:
        return 'Error'

def post_request(url, data):
    try:
        r = requests.post(url, data=data, timeout=5)
        if r.status_code == 200:
            title = r.text.split('<title>')[1].split('</title>')[0]
            return title
        else:
            return 'Error ' + str(r.status_code)
    except:
        return 'Error'

def header_request(url, headers):
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            title = r.text.split('<title>')[1].split('</title>')[0]
            return title
        else:
            return 'Error ' + str(r.status_code)
    except:
        return 'Error'

def start():
    urls = url_input.get('1.0', END).strip().split('\n')
    mode = var.get()
    thread_num = int(thread_input.get())
    if mode == 1:
        for url in urls:
            t = threading.Thread(target=get_title, args=(url,))
            t.setDaemon(True)
            t.start()
    elif mode == 2:
        data = data_input.get('1.0', END).strip()
        for url in urls:
            t = threading.Thread(target=post_request, args=(url, data))
            t.setDaemon(True)
            t.start()
    elif mode == 3:
        headers = eval(data_input.get('1.0', END).strip())
        for url in urls:
            t = threading.Thread(target=header_request, args=(url, headers))
            t.setDaemon(True)
            t.start()

def beautify(code):
    code_dict = {'200': '成功', '404': '未找到', '500': '服务器错误'}
    if code in code_dict:
        return code_dict[code]
    else:
        return code

root = Tk()
root.title('网站访问器')

url_label = Label(root, text='网址：')
url_label.grid(row=0, column=0)

url_input = Text(root, height=5, width=50)
url_input.grid(row=0, column=1)

mode_label = Label(root, text='访问方式：')
mode_label.grid(row=1, column=0)

var = IntVar()
get_radio = Radiobutton(root, text='GET', variable=var, value=1)
get_radio.grid(row=1, column=1)

post_radio = Radiobutton(root, text='POST', variable=var, value=2)
post_radio.grid(row=2, column=1)

header_radio = Radiobutton(root, text='HEADER', variable=var, value=3)
header_radio.grid(row=3, column=1)

data_label = Label(root, text='请求内容：')
data_label.grid(row=4, column=0)

data_input = Text(root, height=5, width=50)
data_input.grid(row=4, column=1)

thread_label = Label(root, text='线程数：')
thread_label.grid(row=5, column=0)

thread_input = Entry(root)
thread_input.grid(row=5, column=1)

start_btn = Button(root, text='开始', command=start)
start_btn.grid(row=6, column=1)

result_label = Label(root, text='结果：')
result_label.grid(row=7, column=0)

result_text = Text(root, height=10, width=50)
result_text.grid(row=7, column=1)

root.mainloop()

