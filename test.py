import time
import datetime
import tkinter as tk
import tkinter.font

def showtime():
    info.set(str(datetime.datetime.now()).split()[1])
    root.after(1,showtime)

def showtime1():
    hms.set(time.strftime('%H:%M:%S',time.localtime()))
    root.after(1,showtime1)

def showtime2():
    x = str(time.perf_counter()).split('.')
    a.set((x[0]+'.'+x[1][0]))
    root.after(1,showtime2)

def timer():
    y = str(time.time()-st).split('.')
    b.set(y[0]+'.'+y[1][0])
    root.after(1,timer)
def start_t(event):
    global st
    global label5
    st = time.time()
    label5 = tk.Label(root,textvariable = b, width = '20',font = ft)
    label5.place(x = 50,y = 160)
    timer()

def end_t(event):
    end = time.time()
    z = str(end-st).split('.')
    w= z[0]+'.'+z[1][0]
    label5.destroy()
    label6 = tk.Label(root,text = w,width = '20', font = ft)
    label6.place(x = 50,y = 160)



if __name__ == "__main__":
    root = tk.Tk(className='时间')
    root.geometry('400x250+600+250')
    ft = tkinter.font.Font(family='Times New Roman',size='30',weight='bold')
    info = tk.StringVar()
    #带毫秒的时间
    lab_message = tk.Label(root,width = '25',textvariable = info,font = ft)
    lab_message.place(x=0,y=80)

    #日期   
    date_time = str(datetime.datetime.now()).split()[0]
    label2 = tk.Label(root, width = '9',text = date_time,font = ft)
    label2.place(x = 120,y=5)

    #小时，分钟，秒
    hms= tk.StringVar()
    label3 = tk.Label(root,textvariable = hms,font = ft)
    label3.place(x = 130, y = 40)

    #计时测试
    a = tk.StringVar()
    label4 = tk.Label(root,textvariable = a, font = ft)
    label4.place(x = 100,y = 120)


    b = tk.StringVar()
    b.set('0.0')

    #开始
    button1 = tk.Button(root,text = 'Start',width = '5',font = ft)
    button1.bind('<Button-1>',start_t)
    button1.place(x = 100,y=210)

    #结束
    button2 = tk.Button(root,text = 'End',width = '5',font = ft)
    button2.bind('<Button-1>',end_t)
    button2.place(x = 200, y = 210)


    showtime()
    showtime1()
    showtime2()

    root.mainloop()
    print(datetime.datetime.now())





