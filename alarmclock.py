from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

bgcolor="#ffffff"
col='#566FC6'
window=Tk()
window.title("ALARM CLOCK")
window.geometry('400x200')
window.configure(bg=bgcolor)

frameline=Frame(window,width=400,height=5,bg=col)
frameline.grid(row=0,column=0)
framebody=Frame(window,width=400,height=290,bg=bgcolor)
framebody.grid(row=1,column=0)  
img=Image.open('clock1.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)
img1=Label(framebody,height=100,image=img)
img1.place(x=10,y=10)
name=Label(framebody,text="ALARM",height=1,font=('Ivy 18 bold'),bg=bgcolor)
name.place(x=125,y=10)

name1=Label(framebody,text="HOURS",height=1,font=('Ivy 9 bold'),bg=bgcolor)
name1.place(x=127,y=40)
hourscount=Combobox(framebody,width=2,font=('arial 15'))
hourscount['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
hourscount.place(x=131,y=60)
hourscount.current(0)

name2=Label(framebody,text="MINUTES",height=1,font=('Ivy 9 bold'),bg=bgcolor)
name2.place(x=200,y=40)
mincount=Combobox(framebody,width=2,font=('arial 15'))
mincount['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
mincount.place(x=200,y=60)
mincount.current(0)

name3=Label(framebody,text="SECONDS",height=1,font=('Ivy 9 bold'),bg=bgcolor)
name3.place(x=273,y=40)
seccount=Combobox(framebody,width=2,font=('arial 15'))
seccount['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
seccount.place(x=273,y=60)
seccount.current(0)

name4=Label(framebody,text="PERIOD",height=1,font=('Ivy 9 bold'),bg=bgcolor)
name4.place(x=346,y=40)
period=Combobox(framebody,width=3,font=('arial 15'))
period['values']=('AM','PM')
period.place(x=346,y=60)
period.current(0)
def activate_alarm():
    t=Thread(target=alarm)
    t.start()
    
def deactivate_alarm():
    print("Deactivated alarm : ",selected.get())
    mixer.music.stop()
    
selected=IntVar()

rad1=Radiobutton(framebody,font=('arial 10 bold'),value=1,text="Activate",bg=bgcolor,variable=selected,command=activate_alarm)
rad1.place(x=125,y=95)

rad2=Radiobutton(framebody,font=('arial 10 bold'),value=2,text="Deactivate",bg=bgcolor,variable=selected,command=deactivate_alarm)
rad2.place(x=200,y=95)

def sound_alarm():
    mixer.music.load('alarm-clock.mp3')
    mixer.music.play()
    selected.set(0)

def alarm():
    while True :
        control=selected.get()
        print(control)
        alarm_hour=hourscount.get()
        alarm_min=mincount.get()
        alarm_sec=seccount.get()
        alarm_period=period.get()
        alarm_period=str(alarm_period).upper()
        
        now=datetime.now()
        hour=now.strftime("%I")
        minute=now.strftime("%M")
        second=now.strftime("%S")
        periodd=now.strftime("%p")
        
        if control==1:
            if alarm_period==periodd:
                if alarm_hour==hour:
                    if alarm_min==minute:
                        if alarm_sec==second:
                            print("Time to take a break!!")
                            sound_alarm()
        sleep(1)
        
mixer.init()
window.mainloop()