#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
import threading
import serial
import os



def sel1():
    global sel1_state
    if(sel1_state==0):
        try:
            port.write("A".encode('ascii'))
            timer1=threading.Timer(int(spin.get()),timer1_end)            
            timer1.start()
            bsel1.configure(bg = "brown",fg="white")
            bsel1.configure(activebackground = "brown",activeforeground="white")            
            sel1_state=1;
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")

        
def sel2():
    global sel2_state
    if(sel2_state==0):
        try:
            port.write("B".encode('ascii'))
            timer2=threading.Timer(int(spin.get()),timer2_end)
            timer2.start()
            bsel2.configure(bg = "brown",fg="white")
            bsel2.configure(activebackground = "brown",activeforeground="white")                                
            sel2_state=1
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")
 

def sel3():
    global sel3_state
    if(sel3_state==0):
        try:
            port.write("C".encode('ascii'))
            timer3=threading.Timer(int(spin.get()),timer3_end)
            timer3.start()
            bsel3.configure(bg = "brown",fg="white")
            bsel3.configure(activebackground = "brown",activeforeground="white")                        
            sel3_state=1
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")

    
def sel4():
    global sel4_state
    if(sel4_state==0):
        try:
            port.write("D".encode('ascii'))
            timer4=threading.Timer(int(spin.get()),timer4_end)
            timer4.start()
            bsel4.configure(bg = "brown",fg="white")
            bsel4.configure(activebackground = "brown",activeforeground="white")                    
            sel4_state=1
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")

def motor1():
    global motor1_state
    if(motor1_state==0):
        try:
            port.write("E".encode('ascii'))
            bmotor1.configure(bg = "brown",fg="white")
            bmotor1.configure(activebackground = "brown",activeforeground="white")            
            motor1_state=1
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")
    else:
        try:
            port.write("e".encode('ascii'))            
            bmotor1.configure(bg = "azure2",fg="black")
            bmotor1.configure(activebackground = "azure2",activeforeground="black")            
            motor1_state=0
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")
        

    
def motor2():
    global motor2_state
    if(motor2_state==0):
        try:
            port.write("F".encode('ascii'))
            bmotor2.configure(bg = "brown",fg="white")
            bmotor2.configure(activebackground = "brown",activeforeground="white")        
            motor2_state=1
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")
    else:
        try:
            port.write("f".encode('ascii'))
            bmotor2.configure(bg = "azure2",fg="black")
            bmotor2.configure(activebackground = "azure2",activeforeground="black")            
            motor2_state=0
        except:
            tk.messagebox.showinfo("Error!", "Serial Port Error!")
    
def timer1_end():
    global sel1_state
    try:
        port.write("a".encode('ascii'))
        sel1_state=0
        bsel1.configure(bg = "azure2",fg="black")
        bsel1.configure(activebackground = "azure2",activeforeground="black")
    except:
        tk.messagebox.showinfo("Error!", "Serial Port Error!")
    
    
def timer2_end():
    global sel2_state
    try:
        port.write("b".encode('ascii'))
        sel2_state=0
        bsel2.configure(bg = "azure2",fg="black")
        bsel2.configure(activebackground = "azure2",activeforeground="black")
    except:
        tk.messagebox.showinfo("Error!", "Serial Port Error!")
    
def timer3_end():
    global sel3_state
    try:
        port.write("c".encode('ascii'))
        sel3_state=0
        bsel3.configure(bg = "azure2",fg="black")
        bsel3.configure(activebackground = "azure2",activeforeground="black")
    except:
        tk.messagebox.showinfo("Error!", "Serial Port Error!")
    
    
def timer4_end():
    global sel4_state
    try:
        port.write("d".encode('ascii'))
        sel4_state=0
        bsel4.configure(bg = "azure2",fg="black")
        bsel4.configure(activebackground = "azure2",activeforeground="black")
    except:
        tk.messagebox.showinfo("Error!", "Serial Port Error!")
    
    






root=tk.Tk()
root.title('Hello')
sel2= tk.Tk()
root.attributes('-fullscreen',True)
root.geometry("480x320")
root.configure(bg='white')

sel1_state=0
sel2_state=0
sel3_state=0
sel4_state=0
motor1_state=0
motor2_state=0

try:
    port=serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)
except:
    tk.messagebox.showinfo("Error!", "Serial Port Error!")
#port.open()

timer2=threading.Timer(1,timer2_end)
timer3=threading.Timer(1,timer3_end)
timer4=threading.Timer(1,timer4_end)



#backimage = tk.PhotoImage(file="1.png")
#label1=tk.Label(root,image=backimage)
#label1.pack()

bsel1=tk.Button(root,text ="Selnoid1",height=5,width=8,command=sel1,font=('helvetica', 14),bg = "azure2")
bsel2=tk.Button(root,text ="Selnoid2",height=5,width=8,command=sel2,font=('helvetica', 14),bg = "azure2")
bsel3=tk.Button(root,text ="Selnoid3",height=5,width=8,command=sel3,font=('helvetica', 14),bg = "azure2")
bsel4=tk.Button(root,text ="Selnoid4",height=5,width=8,command=sel4,font=('helvetica', 14),bg = "azure2")
bsel1.place(x=5, y=10)
bsel2.place(x=125, y=10)
bsel3.place(x=245, y=10)
bsel4.place(x=365, y=10)

bmotor1=tk.Button(root,text ="Motor1",height=5,width=8,command=motor1,font=('helvetica', 14),bg = "azure2")
bmotor2=tk.Button(root,text ="Motor2",height=5,width=8,command=motor2,font=('helvetica', 14),bg = "azure2")
bmotor1.place(x=20, y=150)
bmotor2.place(x=350, y=150)


spin=tk.Spinbox(root, from_=1, to=20,width=3,font=('helvetica', 30),state= "readonly",bg="white")
spin.place(x=190, y=200)

label=tk.Label(root,text="Timer:",width=6,font=('helvetica', 16),bg="white")
label.place(x=195, y=165)

root.mainloop()

