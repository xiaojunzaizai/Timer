import time
import tkinter as tk
import tkinter.font

def start_f():
    time1 =str(time.time()-s).split('.')
    time1_1 = time1[0]+'.'+time1[1][:2]
    v.set(time1_1)
    root.after(1,start_f)





def start_t(event):
    global s
    global label2
    s = time.time()
    label1.destroy()
    label2 = tk.Label(root,textvariable = v,width = '15',font = ft)
    label2.place(x= 0, y = 30)
    start_f()
    

def end_t(event):
    end = time.time()
    time2 = str(end- s).split('.')
    time2_2 = time2[0]+'.'+time2[1][:2]
    label2.destroy()
    label3 = tk.Label(root,text = time2_2,width = '15',font = ft)
    label3.place(x= 0, y = 30)



if __name__ == "__main__":
    root = tk.Tk(className= 'T i m e r')
    root.geometry('350x200+600+250')
    ft = tkinter.font.Font(family='Times New Roman',size='30',weight='bold')
    v = tk.StringVar()
    #label
    label1 = tk.Label(root,text = '0.00',width = '15',font = ft)
    label1.place(x= 0, y = 30)


    #start
    start = tk.Button(root,text = 'Start', width = '5', font = ft)
    start.bind('<Button-1>',start_t)
    start.place(x = 40, y = 100)

    #end
    end = tk.Button(root,text = 'End', width = '5',font = ft)
    end.bind('<Button-1>',end_t)
    end.place(x = 180,y = 100)

    root.mainloop()
