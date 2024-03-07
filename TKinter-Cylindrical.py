from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
import playsound

#Create GUI Window with Title
gui = Tk()
gui.title("Cylindrical Calculator")
gui.resizable(True,False)
gui.config(bg="pink")     

def f_k():
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_F.mp3")

def rst():
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_rst.mp3")

def i_k():
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_I.mp3")


## Frame
FI = LabelFrame(gui,text="Link Lengths and Joint Variables",font=("Comic Sans MS",20))
FI.grid(row=0,column=0)

#Link Lengths
a1 = Label(FI,text=("a1 = "),font=(10))
a1_E = Entry(FI,width=5,font=(10))
cm1 = Label(FI,text=("cm"),font=(10))

a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2 = Label(FI,text=("a2 = "),font=(10))
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text=("cm"),font=(10))

a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3 = Label(FI,text=("a3 = "),font=(10))
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text=("cm"),font=(10))

a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

t1 = Label(FI,text=("t1 = "),font=(10))
t1_E = Entry(FI,width=5,font=(10))
deg1 = Label(FI,text=("cm"),font=(10))

t1.grid(row=0,column=3,padx=(40,0))
t1_E.grid(row=0,column=4)
deg1.grid(row=0,column=5)

d2 = Label(FI,text=("t2 = "),font=(10))
d2_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text=("deg"),font=(10))

d2.grid(row=1,column=3,padx=(40,0))
d2_E.grid(row=1,column=4)
cm4.grid(row=1,column=5)

d3 = Label(FI,text=("t3 = "),font=(10))
d3_E = Entry(FI,width=5,font=(10))
cm5 = Label(FI,text=("deg"),font=(10))

d3.grid(row=2,column=3,padx=(40,0))
d3_E.grid(row=2,column=4)
cm5.grid(row=2,column=5)

#Button Frames
BF = LabelFrame(gui,text="Forward and Inverse Kinematics",font=("Comic Sans MS",20))
BF.grid(row=1,column=0)

#Buttons
FK = Button(BF,text="Forward",font=(10),bg="black", fg="white", command=f_k)
rst = Button(BF,text="RESET",font=(10),bg="white", fg="black", command=rst)
IK = Button(BF,text="Inverse",font=(10),bg="hot pink", fg="white", command=i_k)

FK.grid(row=0,column=0,padx=(40,0))
rst.grid(row=0,column=1)
IK.grid(row=0,column=2,padx=(0,40))

##Position Vector
PV = LabelFrame(gui,text="Position Vector",font=("Comic Sans MS",20))
PV.grid(row=2,column=0)

X = Label(PV,text=("X = "),font=(10))
X_E = Entry(PV,width=5,font=(10))
cm8 = Label(PV,text=("cm"),font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm8.grid(row=0,column=2)

Y = Label(PV,text=("Y = "),font=(10))
Y_E = Entry(PV,width=5,font=(10))
cm9 = Label(PV,text=("cm"),font=(10))

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm9.grid(row=1,column=2)

Z = Label(PV,text=("Z = "),font=(10))
Z_E = Entry(PV,width=5,font=(10))
cm10 = Label(PV,text=("cm"),font=(10))

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm10.grid(row=2,column=2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

gui.mainloop()