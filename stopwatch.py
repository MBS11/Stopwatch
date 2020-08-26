from tkinter import *
from datetime import datetime



counter=66600
running=False


window=Tk()
window.title("StopWatch")
window.minsize(width=250,height=125)




def counter_label(label):
    def count():
        if running:
            global counter
            if counter==66600:
                display="Starting.."
            else:
                tt=datetime.fromtimestamp(counter)
                string=tt.strftime("%H:%M:%S")
                display=string
            label['text']=display
            label.after(1000,count)
            counter += 1
    count()


def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running=False

def Reset(label):
    global counter
    counter=66600
    if running==False:
        reset['state']='disabled'
        label['text']='Welcome!'
    else:
        label['text']='Starting..'
        






label=Label(window,text="Welcome!",fg="blue",font="Verdana 30 bold")
label.pack()

f=Frame(window)
f.pack(pady=10)

start=Button(f,text='Start',bd=5,width=6,command = lambda:Start(label))
start.grid(row=4,column=1)
stop=Button(f,text='Stop',bd=5,width=6,state='disabled',command = Stop)
stop.grid(row=4,column=3)
reset=Button(f,text='Reset',bd=5,width=6,state='disabled',command = lambda:Reset(label))
reset.grid(row=4,column=5)

window.mainloop()
