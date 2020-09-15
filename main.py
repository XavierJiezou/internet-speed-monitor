import tkinter as tk
from icon import img
import psutil
import base64
import os


def update():
    global last_up_data
    global last_dl_data
    global init
    if init:
        init = False
        last_up_data = psutil.net_io_counters().bytes_sent
        last_dl_data = psutil.net_io_counters().bytes_recv
        label_up.config(text=upload_text.format(0, 'K'))
        label_dl.config(text=dlload_text.format(0, 'K'))
    else:
        curr_up_data = psutil.net_io_counters().bytes_sent
        curr_dl_data = psutil.net_io_counters().bytes_recv
        temp_up_data = (curr_up_data-last_up_data)/1024
        temp_dl_data = (curr_dl_data-last_dl_data)/1024
        if temp_up_data > 1024:
            _upload_text = upload_text.format(temp_up_data/1024, 'M')
        else:
            _upload_text = upload_text.format(temp_up_data, 'K')
        if temp_dl_data > 1024:
            _dlload_text = dlload_text.format(temp_dl_data/1024, 'M')
        else:
            _dlload_text = dlload_text.format(temp_dl_data, 'K')
        label_up.config(text=_upload_text)
        label_dl.config(text=_dlload_text)
        last_up_data = curr_up_data
        last_dl_data = curr_dl_data
    app.after(1000, update)


if __name__ == "__main__":
    upload_text = '上传速度：{:.2f} {}b/s'
    dlload_text = '下载速度：{:.2f} {}b/s'

    last_up_data = 0
    last_dl_data = 0
    init = True

    app = tk.Tk()
    tmp = open("tmp.ico", "wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    app.iconbitmap('tmp.ico')
    os.remove("tmp.ico")
    app.title('网速监控')
    app.wm_attributes('-topmost', 1)
    app.geometry('300x100')
    label_up = tk.Label(text=upload_text.format(0, 'K'), font=('Microsoft YaHei', 20), fg='#ff0000')
    label_up.pack(fill=tk.BOTH, expand=True)
    label_dl = tk.Label(text=dlload_text.format(0, 'K'), font=('Microsoft YaHei', 20), fg='#0000ff')
    label_dl.pack(fill=tk.BOTH, expand=True)
    app.after(1000, update)
    app.mainloop()
