from tkinter import *
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    years = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text=hr)
    lab_mn.config(text=mi)
    lab_sc.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_man.config(text=month)
    lab_ye.config(text=years)
    lab_day.config(text=day)
    
    lab_hr.after(200,date_time)

# ***** Time *****
clock = Tk()
clock.geometry("1000x500")
clock.title("*** Digital Clock ***")
clock.config(bg="black")
new = Label(bg="red")
new.place(x=50,y=35,height=430,width=900)
lab_hr = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_hr.place(x=120,y=50,height=110,width=100)
lab_h1 = Label(text="Hour",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_h1.place(x=120,y=200,height=40,width=100)

lab_mn = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_mn.place(x=340,y=50,height=110,width=100)
lab_m1 = Label(text="Min",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_m1.place(x=340,y=200,height=40,width=100)

lab_sc = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_sc.place(x=560,y=50,height=110,width=100)
lab_s1 = Label(text="Sec",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_s1.place(x=560,y=200,height=40,width=100)

lab_am = Label(text="00",font=("Time New Roman",40,"bold"),bg="black",fg="white")
lab_am.place(x=780,y=50,height=110,width=100)
lab_a1 = Label(text="AM/PM",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_a1.place(x=780,y=200,height=40,width=100)

# ***** Date *****

lab_date = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date1 = Label(text="Date",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_date1.place(x=120,y=410,height=40,width=100)

lab_man = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_man.place(x=340,y=270,height=110,width=100)
lab_man1 = Label(text="Month",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_man1.place(x=340,y=410,height=40,width=100)

lab_ye = Label(text="00",font=("Time New Roman",50,"bold"),bg="black",fg="white")
lab_ye.place(x=560,y=270,height=110,width=100)
lab_ye1 = Label(text="Years",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_ye1.place(x=560,y=410,height=40,width=100)


lab_day = Label(text="00",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_day.place(x=780,y=270,height=110,width=100)
lab_ap1 = Label(text="Day",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_ap1.place(x=780,y=410,height=40,width=100)
date_time()
clock.mainloop()