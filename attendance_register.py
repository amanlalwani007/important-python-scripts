from tkinter import Tk,StringVar,ttk
from tkinter import *
import time
from tkinter import messagebox
import datetime
root=Tk()
root.title("Attendance Register")
root.geometry('1350x650+0+0')
root.configure(background='black')

#------------------------Frame-----------------------
LeftMayFrame=Frame(root,width=1000,height=650,bd=8,relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(root,width=350,height=650,bd=8,relief="raise")
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1=Frame(LeftMayFrame,width=1000,height=100,bd=8,relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=1000,height=550,bd=8,relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1=Frame(RightMayFrame,width=350,height=215,bd=8,relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=350,height=415,bd=8,relief="raise")
RightMayFrame2.pack(side=TOP)
#-----------------------------------------------------
cont1=Canvas(RightMayFrame2,width=350,height=425,bg="black",)
cont1.grid(row=0,column=0)
image5=PhotoImage(file="gla.png")
cont1.create_image(200,200,image=image5)

#-----------------------------------------------------
cont=Canvas(RightMayFrame1,width=350,height=215)
cont.grid(row=0,column=0)
image1=PhotoImage(file="aman.png")
image=cont.create_image(200,200,image=image1)
def pic1():
    image=cont.create_image(200,200,image=image1)
image2=PhotoImage(file="image2.png")
def pic2():
    image=cont.create_image(200,200,image=image2)
image3=PhotoImage(file="aman.png")
def pic3():
    image=cont.create_image(200,200,image=image3)
image4=PhotoImage(file="image2.png")
def pic4():
    image = cont.create_image(200, 200, image=image4)




#---------------------variables--------------------------------
DateofOrder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
value10=StringVar()
value11=StringVar()
def Mark_Register():
    if value0.get()=="/":
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
    elif value0.get()=="0":
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")
        value8.set("0")
        value9.set("0")
        value10.set("0")
        value11.set("0")
    elif value0.get()=="S":
        value1.set("S")
        value2.set("S")
        value3.set("S")
        value4.set("S")
        value5.set("S")
        value6.set("S")
        value7.set("S")
        value8.set("S")
        value9.set("S")
        value10.set("S")
        value11.set("S")
    elif value0.get()=="A":
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
        value11.set("A")
    elif value0.get()=="L":
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        value10.set("L")
        value11.set("L")
    elif value0.get()==" ":
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        value10.set(" ")
        value11.set(" ")

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
def qExit():
    qExit=messagebox.askyesno("Exit System Do you want to Quit?")
    if qExit>0:
        root.destroy()
        return



#--------------------Componente-------------------
DateofOrder.set(time.strftime("%d/%m/%Y"))
#-------------------Left May Frame1------------------
lb1No=Label(LeftMayFrame1,font=('arial',10,'bold'),text="No.",bd=16)
lb1No.grid(row=0,column=0,sticky=W)
lb1StudentNo=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student No.",bd=16)
lb1StudentNo.grid(row=0,column=1,sticky=W)
lb1StudentName=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student Name",bd=16)
lb1StudentName.grid(row=0,column=2,sticky=W)
lb1StudentCode=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Course code",bd=16)
lb1StudentCode.grid(row=0,column=3,sticky=W)
box=ttk.Combobox(LeftMayFrame1,textvariable=value0,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnFill=Button(LeftMayFrame1,text='Fill',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'),width=12,height=1,command=Mark_Register).grid(row=0,column=5)
btnReset=Button(LeftMayFrame1,text='Reset',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'),width=12,height=1,command=Reset).grid(row=0,column=6)
btnExit=Button(LeftMayFrame1,text='Exit',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'),width=12,height=1,command=qExit).grid(row=0,column=7)
lb1DateofOrder=Label(LeftMayFrame1,font=('arial',10,'bold'),textvariable=DateofOrder,padx=2,
                     pady=2,bd=2,fg='black',bg='white',relief='sunken')
lb1DateofOrder.grid(row=0,column=8,sticky=W)



#-------------------Left May Frame2 row1------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1",bd=16)
lb1No.grid(row=0,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500067",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=0,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Aman Lalwani",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=0,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value1,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=0,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=0,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=0,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic4).grid(row=0,column=8)




#-------------------Left May Frame2 row2------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="2",bd=16)
lb1No.grid(row=1,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500068",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=1,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Aman Rajput",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=1,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value2,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=1,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=1,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=1,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=1,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic4).grid(row=1,column=8)


#-------------------Left May Frame2 row3------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3",bd=16)
lb1No.grid(row=2,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500090",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=2,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Ankit Sharma",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=2,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=2,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=2,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=2,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=2,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=2,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic4).grid(row=2,column=8)

#-------------------Left May Frame2 row4------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="4",bd=16)
lb1No.grid(row=3,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500069",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=3,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Amisha Pandey",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=3,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value4,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=3,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=3,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=3,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=3,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command=pic4).grid(row=3,column=8)



#-------------------Left May Frame2 row6------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="5",bd=16)
lb1No.grid(row=4,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500055",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=4,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Akash Pateriya",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=4,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value5,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=4,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=8)


#-------------------Left May Frame2 row7------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="6",bd=16)
lb1No.grid(row=5,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500066",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=5,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Aman srivastava",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=5,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value6,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=5,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=8)


#-------------------Left May Frame2 row8------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="7",bd=16)
lb1No.grid(row=6,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500064",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=6,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Aman gupta",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=6,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value7,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=6,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=8)


#-------------------Left May Frame2 row9------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="8",bd=16)
lb1No.grid(row=7,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500070",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=7,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Amit kumar",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=7,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value8,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=7,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=8)




#-------------------Left May Frame2 row9------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="9",bd=16)
lb1No.grid(row=8,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500071",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=8,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Amit kumar2",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=8,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value9,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=8,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=8)



#-------------------Left May Frame2 row10------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="10",bd=16)
lb1No.grid(row=9,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500072",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=9,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Amit sharma",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=9,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=9,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value10,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=9,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=8)





#-------------------Left May Frame2 row11------------------
lb1No=Label(LeftMayFrame2,font=('arial',10,'bold'),text="11",bd=16)
lb1No.grid(row=10,column=0,sticky=W)
lb1Student_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="161500054",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_No_1.grid(row=10,column=1,sticky=W)
lb1Student_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Ajeet yadav",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=10,column=2,sticky=W)
lb1Student_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="CSE",
                      padx=2,pady=2,bd=2,fg="black",width=12)
lb1Student_Code.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value11,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=10,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=8)





root.mainloop()
