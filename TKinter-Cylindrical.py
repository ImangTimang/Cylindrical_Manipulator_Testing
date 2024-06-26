from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import Tk, Toplevel, Button
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use('TkAgg')
import playsound


#Create GUI Window with Title
gui = Tk()
gui.title("Cylindrical Calculator")
gui.resizable(True,False)
gui.config(bg="pink")   

## Forward Kinematics
def f_k():
    
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())

    ## FKin Calculator
    # joint variables: is mm if f, is degrees if theta
    t1 = float(t1_E.get())
    d2 = float(d2_E.get())
    d3 = float(d3_E.get())
    ##Plays Sound when button is pressed, Change Path File When Needed
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_F.mp3")

    # degree to radian
    t1 = (t1/180.0)*np.pi

    # Parametic Table (theta, alpha, r, d)
    PT = [[t1, (0.0/180.0)*np.pi, 0, a1],
      [(270.0/180.0)*np.pi, (270.0/180.0)*np.pi, 0, a2+d2],
      [(0.0/180.0)*np.pi, (0.0/180.0)*np.pi, 0, a3+d3]]


    # HTM formulae
    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    i   = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    H0_1 = np.matrix(H0_1)

    H1_2 = np.matrix(H1_2)
   
    H2_3 = np.matrix(H2_3)

    H0_2 = np.dot(H0_1,H1_2)
    H0_3 = np.dot(H0_2,H2_3)
    
    X0_3 = H0_3[0,3]
    X_E.delete(0,END)
    X_E.insert(0,np.around(X0_3,3))

    Y0_3 = H0_3[1,3]
    Y_E.delete(0,END)
    Y_E.insert(0,np.around(Y0_3,3))

    Z0_3 = H0_3[2,3]
    Z_E.delete(0,END)
    Z_E.insert(0,np.around(Z0_3,3))

    ##Model
    Cylindrical = DHRobot([
            RevoluteDH(a1,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
            PrismaticDH(0,0,(270.0/180.0)*np.pi,a2,qlim=[0,10]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a3,qlim=[0,10]),
        ]   , name="Cylindrical")

    print(Cylindrical)

    Cylindrical.teach(q=[t1,d2,d3],block=True)


    
    
def rst():
    
    a1_E.delete(0,END)
    a2_E.delete(0,END)
    a3_E.delete(0,END)

    t1_E.delete(0,END)
    d2_E.delete(0,END)
    d3_E.delete(0,END)

    X_E.delete(0,END)
    Y_E.delete(0,END)
    Z_E.delete(0,END)

    ##Plays Sound when button is pressed
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_rst.mp3")#Change Path File when needed


## Inverse Kinematics
def i_k():

    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())

    # Position Vector in mm
    x0_3 = float(X_E.get())
    y0_3 = float(Y_E.get())
    z0_3 = float(Z_E.get())
    
    #Change Path File when needed
    playsound.playsound("/home/imang/ROBO2/Cylindrical/Music/toyphone_I.mp3")
    #Inverse Kinematic Solutions using Graphical Method

    # Solution 1
    t1 = np.arctan(y0_3/x0_3)

    # Solution 2
    r = np.sqrt((x0_3**2)+(y0_3**2))

    # Solution 3
    d3 = r-a3

    # Solution 4
    d2 = z0_3-a1-a2

    t1_E.delete(0,END)
    t1_E.insert(0,np.around(t1*180/np.pi,3))

    d2_E.delete(0,END)
    d2_E.insert(0,np.around(d2,3))

    d3_E.delete(0,END)
    d3_E.insert(0,np.around(d3,3))

    ##Model
    Cylindrical = DHRobot([
            RevoluteDH(a1,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
            PrismaticDH(0,0,(270.0/180.0)*np.pi,a2,qlim=[0,10]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a3,qlim=[0,10]),
        ]   , name="Cylindrical")

    print(Cylindrical)

    Cylindrical.teach(q=[t1,d2,d3],block=True)
    

    
        
    
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
deg1 = Label(FI,text=("deg"),font=(10))

t1.grid(row=0,column=3,padx=(40,0))
t1_E.grid(row=0,column=4)
deg1.grid(row=0,column=5)

d2 = Label(FI,text=("d2 = "),font=(10))
d2_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text=("cm"),font=(10))

d2.grid(row=1,column=3,padx=(40,0))
d2_E.grid(row=1,column=4)
cm4.grid(row=1,column=5)

d3 = Label(FI,text=("d3 = "),font=(10))
d3_E = Entry(FI,width=5,font=(10))
cm5 = Label(FI,text=("cm"),font=(10))

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

img = PhotoImage(file="/home/imang/ROBO2/Cylindrical/Cylindrical.gif")
img = img.subsample(3,3)
#resized_image = img.resize(20, 20)
PI = Label(gui,image=img)
PI.grid(row=3,column=0)



gui.mainloop()