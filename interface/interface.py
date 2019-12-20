# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:54:04 2019

@author: owner
"""

from tkinter import *


'''
class option_menu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='gray',width=12)
        self['menu'].config(font=('calibri',(10)),bg='gray')
'''


root = Tk()

root.geometry("1000x800")
root.title('CHD Risk Evaluation Interface')
root.configure(background='#99ccff')

TOP = Label(root, justify=LEFT, text="Evaluating Risk of CHD.....", fg="#003566", bg="#99ccff", padx = 0)
TOP.config(font=("Monotype Corsiva", 35))
TOP.grid(row=0, column=0, columnspan=3, padx=0, pady=30)


# entry variables
Age = IntVar()
Age.set(0)

BMI = DoubleVar()
BMI.set(None)

Gender = StringVar()
Gender.set("Male")

smoker = StringVar()
smoker.set("Yes")

cigsPerDay = IntVar()
cigsPerDay.set(0)

BPMeds = StringVar()
BPMeds.set("No")

diabetes = StringVar()
diabetes.set("No")

prevalentStroke = StringVar()
prevalentStroke.set("No")

prevalentHyp = StringVar()
prevalentHyp.set("No")

heartRate = DoubleVar()
heartRate.set(0)

glucose = DoubleVar()
glucose.set(0)

sysBP = DoubleVar()
sysBP.set(0)

totChol = DoubleVar()
totChol.set(0)

diaBP = DoubleVar()
diaBP.set(0)



S1Lb = Label(root, text="Age",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S1Lb.grid(row=7, column=0, padx = 60, pady=10, sticky=W)

S2Lb = Label(root, text="BMI",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S2Lb.grid(row=8, column=0, padx = 60,pady=10, sticky=W)

S3Lb = Label(root, text="Gender", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S3Lb.grid(row=9, column=0, padx = 60,pady=10, sticky=W)

S4Lb = Label(root, text="Are you a smoker?", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S4Lb.grid(row=10, column=0,padx = 60, pady=10, sticky=W)

S5Lb = Label(root, text="Cigerates consumed per day", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S5Lb.grid(row=11, column=0,padx = 60, pady=10, sticky=W)


S6Lb = Label(root, text="Are you taking BM Meds?", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S6Lb.grid(row=12, column=0,padx = 60, pady=10, sticky=W)

S7Lb = Label(root, text="Are you diabetic?", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S7Lb.grid(row=13, column=0,padx = 60, pady=10, sticky=W)


S8Lb = Label(root, justify = LEFT,  text="Prevalent Stroke?",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S8Lb.grid(row=7, column=3, pady=10, padx = 25, sticky=W)

S9Lb = Label(root, justify = LEFT, text="Prevalent Hypertension?",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S9Lb.grid(row=8, column=3, pady=10,  padx = 25,sticky=W)

S10Lb = Label(root, justify = LEFT, text="Heart Rate",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S10Lb.grid(row=9, column=3, pady=10, padx = 25, sticky=W)

S11Lb = Label(root, justify = LEFT,  text="Glucose",font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S11Lb.grid(row=10,  column=3, pady=10, padx = 25, sticky=W)

S12Lb = Label(root, justify = LEFT, text="Systolic BP", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S12Lb.grid(row=11, column=3, pady=10,  padx = 25,sticky=W)

S13Lb = Label(root, justify = LEFT, text="Total Cholestrol", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S13Lb.grid(row=12, column=3, pady=10,  padx = 25,sticky=W)

S14Lb = Label(root, justify = LEFT,  text="Diabolic BP", font=("Comic Sans MS", 12), fg="#003566", bg="#99ccff")
S14Lb.grid(row=13, column=3, pady=10,  padx = 25,sticky=W)

accuracy = Label(root, justify = LEFT, text="Accuracy", fg="#003566", bg="#99ccff")
accuracy.config(font=("Monotype Corsiva", 30))
accuracy.grid(row=19, column=0, columnspan=2, padx=20)

plLb = Label(root, font=("Comic Sans MS", 12), padx = 60, text="Prolog", fg="#003566", bg="#99ccff")
plLb.grid(row=21, column=0, pady=10,sticky=W)

bnlb = Label(root, font=("Comic Sans MS", 12), padx= 60, text="Bayesian Network",fg="#003566", bg="#99ccff")
bnlb.grid(row=23, column=0, pady=10, sticky=W)

nnLb = Label(root,font=("Comic Sans MS", 12), padx = 60, text="Neural Network", fg="#003566", bg="#99ccff")
nnLb.grid(row=25, column=0, pady=10, sticky=W)

nbLb = Label(root, font=("Comic Sans MS", 12), padx = 60, text="Prolog (Decision Tree)", fg="#003566", bg="#99ccff")
nbLb.grid(row=27, column=0, pady=10, sticky=W)

t1 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t1.grid(row=21, column=1, padx=0)

t2 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t2.grid(row=23, column=1 , padx=0)

t3 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t3.grid(row=25, column=1 , padx=0)

t4 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t4.grid(row=27, column=1 , padx=0)


#age box
t5 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t5.grid(row=7, column=1 , padx=0)
#BMI
t6 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t6.grid(row=8, column=1 , padx=0)
#CigsPerDat
t7 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t7.grid(row=11, column=1 , padx=0)

#heart
t8 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t8.grid(row=9, column=4 , padx=0)

#glucose
t9 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t9.grid(row=10, column=4 , padx=0)
#sys
t10 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t10.grid(row=11, column=4 , padx=0)
#total
t11 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t11.grid(row=12, column=4 , padx=0)
#diA
t11 = Text(root, height=1, width=16,bg="#001a33",fg="#cce6ff")
t11.grid(row=13, column=4 , padx=0)


lst = sorted(["Yes", "No"])
lst1 = sorted(["Male", "Female", "Other"])


'''S1 = OptionMenu(root, Age, *lst)
S1.grid(row=7, column=1)
#S1.pack()
S1.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S1['menu'].config(font=('calibri',(10)),bg='#4da9ff')'''

'''S2 = OptionMenu(root, BMI, *lst)
S2.grid(row=8, column=1)
#S2.pack()
S2.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S2['menu'].config(font=('calibri',(10)),bg='#4da9ff')'''

S3 = OptionMenu(root, Gender, *lst1)
S3.grid(row=9, column=1)
#S3.pack()
S3.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S3['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S4 = OptionMenu(root, smoker, *lst)
S4.grid(row=10, column=1)
#S4.pack()
S4.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S4['menu'].config(font=('calibri',(10)),bg='#4da9ff')

'''S5 = OptionMenu(root, cigsPerDay, *lst)
S5.grid(row=11, column=1)
#S5.pack()
S5.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S5['menu'].config(font=('calibri',(10)),bg='#4da9ff')'''

S6 = OptionMenu(root, BPMeds, *lst)
S6.grid(row=12, column=1)
#S6.pack()
S6.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S6['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S7 = OptionMenu(root, diabetes, *lst)
S7.grid(row=13, column=1)
#S7.pack()
S7.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S7['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S8 = OptionMenu(root, prevalentStroke, *lst)
S8.grid(row=7, column=4)
#S8En.pack()
S8.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S8['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S9 = OptionMenu(root, prevalentHyp, *lst)
S9.grid(row=8, column=4)
#S9.pack()
S9.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S9['menu'].config(font=('calibri',(10)),bg='#4da9ff')

'''S10 = OptionMenu(root, heartRate, *lst)
S10.grid(row=9, column=4)
#S10.pack()
S10.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S10['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S11 = OptionMenu(root, glucose, *lst)
S11.grid(row=10, column=4)
#S11.pack()
S11.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S11['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S12 = OptionMenu(root, sysBP, *lst)
S12.grid(row=11, column=4)
#S12.pack()
S12.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S12['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S13 = OptionMenu(root, totChol, *lst)
S13.grid(row=12, column=4)
#S13.pack()
S13.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S13['menu'].config(font=('calibri',(10)),bg='#4da9ff')

S14 = OptionMenu(root, diaBP, *lst)
S14.grid(row=13, column=4)
#S14.pack()
S14.config(font=('calibri',(10)),bg="#001a33",fg="#cce6ff",width=12)
S14['menu'].config(font=('calibri',(10)),bg='#4da9ff')'''

def yes():
    print("hello Word")

pred = Label(root, text="Prediction", fg="#003566", bg="#99ccff")
pred.config(font=("Monotype Corsiva", 30))
pred.grid(row=19, column=3, columnspan=2, padx=35)

pl = Button(root, justify = LEFT, text="Prolog Prediction", command=yes, bg="#001a33",fg="#cce6ff")
pl.grid(row=21, column=3,padx=30, sticky = W)

bn = Button(root, justify = LEFT, text="Bayesian Network Prediction", command=yes, bg="#001a33",fg="#cce6ff")
bn.grid(row=23, column=3,padx=30, sticky = W)

nn = Button(root, justify = LEFT, text="Neural Network Prediction", command=yes, bg="#001a33",fg="#cce6ff")
nn.grid(row=25, column=3,padx=30, sticky = W)

nb = Button(root, justify = LEFT, text="Prolog (Decision Tree)", command=yes, bg="#001a33",fg="#cce6ff")
nb.grid(row=27, column=3,padx=30, sticky = W)



#textfileds
t5 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t5.grid(row=21, column=4, padx=10)

t6 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t6.grid(row=23, column=4, padx=10)

t7 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t7.grid(row=25, column=4, padx=10)

t8 = Text(root, height=1, width=20,bg="#001a33",fg="#cce6ff")
t8.grid(row=27, column=4, padx=10)




root.mainloop()
