import datetime
import tkinter as tk
import tkinter.font
import time

def tm():
    t = time.strftime('%H:%M:%S',time.localtime())
    c.set(t)
    root.after(1,tm)

def cw(event):
    root.destroy()

root = tk.Tk(className= ' 时 间  ')
root.geometry('300x200+600+250')
ft = tkinter.font.Font(family = 'Times New Roman',size = '30', weight = 'bold')

a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()



a.set(str(datetime.datetime.now()).split()[0])
b.set(time.ctime().split()[0])



#label1
label1 = tk.Label(root,textvariable = a, font = ft)
label1.place(x = 35, y =20)

#label2
label2 = tk.Label(root,textvariable = b, font = ft)
label2.place(x = 225,y = 20)

#label 3
label3 = tk.Label(root,textvariable = c, font = ft)
label3.place(x = 100, y = 70)

# button
close = tk.Button(root,text='关闭',font = ft)
close.bind('<Button-1>',cw)
close.place(x = 120, y =  130)

tm()
root.mainloop()
