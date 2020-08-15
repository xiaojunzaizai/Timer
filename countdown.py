import tkinter as tk
import time
import tkinter.font

def count():
    global h
    global m 
    global s
    while h> -1:
        while m> -1:
            while s> -1:
                v.set('%02d:%02d:%02d'%(h,m,s))
                root2.update()
                s = s-1
                time.sleep(1)
            m = m -1
            s = 59
        h = h-1
        m = 59
    label_mention = tk.Label(root2,text = '到时间啦！！！', font = ('Times New Roman',30,'bold'))
    label_mention.place(x = 150,y = 15)
    button_retry = tk.Button(root2,text = '重新设定',font = ('Times New Roman',15,'bold'))
    button_retry.place(x= 180, y = 65)
    button_retry.bind('<Button-1>',retry)
    button_close = tk.Button(root2,text = '退出',font = ('Times New Roman',15,'bold'))
    button_close.place(x= 350, y = 65)
    button_close.bind('<Button-1>',close)


def retry(event):
    root2.destroy()
    setcount()
    countdown()

def close(event):
    root2.destroy()

def ensure (event):
    global h
    global m 
    global s 
    if (str(entry_hour.get()).isdigit() or str(entry_hour.get()) == '' )and (str(entry_minute.get()).isdigit() or str(entry_minute.get()) == '' )and (str(entry_second.get()).isdigit() or str(entry_second.get()) == ''):
        if str(entry_hour.get()) == '':
            h = 0
        else:
            h = int(entry_hour.get())
        if str(entry_minute.get()) == '':
            m = 0
        else:
            m = int(entry_minute.get())
        if str(entry_second.get()) == '':
            s = 0
        else:
            s = int(entry_second.get())
        root1.destroy()
    else:
        root1.destroy()
        setcount()


#window1
def setcount():
    global root1
    global entry_hour
    global entry_minute
    global entry_second

    root1 = tk.Tk()
    root1.title('设定时间')
    root1.geometry('480x100+450+400')
    ft = tkinter.font.Font(family = 'Times New Roman',size = '18',weight = 'bold')
    
    #hour
    entry_hour = tk.Entry(root1,width = '10',font = ft)
    label_hour = tk.Label(root1,text = '小时', font = ft)
    entry_hour.place(x = 20, y = 10)
    label_hour.place(x = 120, y = 12)
    
    #minute
    entry_minute = tk.Entry(root1,width = '10',font = ft)
    label_minute = tk.Label(root1,text = '分钟', font = ft)
    entry_minute.place(x = 170, y = 10)
    label_minute.place(x = 270, y = 12)
    
    #second
    entry_second = tk.Entry(root1,width = '10',font = ft)
    label_second = tk.Label(root1,text = '秒', font = ft)
    entry_second.place(x = 320, y = 10)
    label_second.place(x = 420, y = 12)

    #ensure
    button_check = tk.Button(root1,text = '确定',font = ft)
    button_check.place(x = 200, y = 60)
    button_check.bind('<Button-1>',ensure)

    root1.mainloop()

#window2

def countdown():
    global root2
    global v
    root2 = tk.Tk()
    root2.title('倒计时')
    root2.geometry('480x100+450+400')
    ft = tkinter.font.Font(family = 'Times New Roman',size = '30',weight = 'bold')
    v = tk.StringVar()
    v.set(' 0 0 : 0 0 : 0 0 ')
    label_time = tk.Label(root2,textvariable= v,font = ft)
    label_time.place(x = 170, y = 15)
    count()
    #另一种方式
    # while h> -1:
    #     while m> -1:
    #         while s> -1:
    #             print('%02d : %02d : %02d'%(h,m,s))
    #             label_time.config(text = '%02d:%02d:%02d'%(h,m,s))
    #             root2.update()
    #             s = s-1
    #             time.sleep(1)
    #         m = m -1
    #         s = 59
    #     h = h-1
    #     m = 59
    root2.mainloop()



setcount()
countdown()

