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
root.configure(background='gray')
root.geometry("1000x1000")
                                    # Heading
TOP = Label(root, justify=LEFT, text="Evaluating Risk of CHD", fg="black", bg="gray")
TOP.config(font=("Elephant", 50))
TOP.grid(row=1, column=0, columnspan=4, padx=150)

# entry variables
Age = StringVar()
Age.set(None)
BMI = StringVar()
BMI.set(None)
Gender = StringVar()
Gender.set("male")

smoker = StringVar()
smoker.set("Yes")

cigsPerDay = StringVar()
cigsPerDay.set(0)

BPMeds = StringVar()
BPMeds.set("No")

diabetes = StringVar()
diabetes.set("No")

prevalentStroke = StringVar()
prevalentStroke.set("No")

prevalentHyp = StringVar()
prevalentHyp.set("No")

heartRate = StringVar()
heartRate.set(None)

glucose = StringVar()
glucose.set(None)

sysBP = StringVar()
sysBP.set(None)

totChol = StringVar()
totChol.set(None)

diaBP = StringVar()
diaBP.set(None)



S1Lb = Label(root, text="Age", fg="black", bg="gray")
S1Lb.grid(row=7, column=0, padx = 10, pady=10, sticky=W)

S2Lb = Label(root, text="BMI", fg="black", bg="gray")
S2Lb.grid(row=8, column=0, padx = 10,pady=10, sticky=W)

S3Lb = Label(root, text="Gender", fg="black", bg="gray")
S3Lb.grid(row=9, column=0, padx = 10,pady=10, sticky=W)

S4Lb = Label(root, text="Are you a smoker?", fg="black", bg="gray")
S4Lb.grid(row=10, column=0,padx = 10, pady=10, sticky=W)

S5Lb = Label(root, text="Cigerates consumed per day:", fg="black", bg="gray")
S5Lb.grid(row=11, column=0,padx = 10, pady=10, sticky=W)


S6Lb = Label(root, text="Are you taking BM Meds?", fg="black", bg="gray")
S6Lb.grid(row=12, column=0,padx = 10, pady=10, sticky=W)

S7Lb = Label(root, text="Are you diabetic?", fg="black", bg="gray")
S7Lb.grid(row=13, column=0,padx = 10, pady=10, sticky=W)


S8Lb = Label(root, justify = LEFT,  text="Prevalent Stroke?", fg="black", bg="gray")
S8Lb.grid(row=7, column=3, pady=10, sticky=W)

S9Lb = Label(root, justify = LEFT, text="Prevalent Hypertension?", fg="black", bg="gray")
S9Lb.grid(row=8, column=3, pady=10, sticky=W)

S10Lb = Label(root, justify = LEFT, text="Heart Rate", fg="black", bg="gray")
S10Lb.grid(row=9, column=3, pady=10, sticky=W)

S11Lb = Label(root, justify = LEFT,  text="Glucose", fg="black", bg="gray")
S11Lb.grid(row=10,  column=3, pady=10, sticky=W)

S12Lb = Label(root, justify = LEFT, text="Systolic BP", fg="black", bg="gray")
S12Lb.grid(row=11, column=3, pady=10, sticky=W)

S13Lb = Label(root, justify = LEFT, text="Total Cholestrol", fg="black", bg="gray")
S13Lb.grid(row=12, column=3, pady=10, sticky=W)

S14Lb = Label(root, justify = LEFT,  text="Diabolic BP", fg="black", bg="gray")
S14Lb.grid(row=13, column=3, pady=10, sticky=W)

accuracy = Label(root, justify = LEFT, text="Accuracy", fg="red", bg="gray")
accuracy.config(font=("Elephant", 30))
accuracy.grid(row=19, column=0, columnspan=2, padx=20)

plLb = Label(root, text="Prolog", fg="black", bg="gray")
plLb.grid(row=21, column=0, pady=10,sticky=W)

bnlb = Label(root, text="Bayesian Network", fg="black", bg="gray")
bnlb.grid(row=23, column=0, pady=10, sticky=W)

nnLb = Label(root, text="Neural Network", fg="black", bg="gray")
nnLb.grid(row=25, column=0, pady=10, sticky=W)

nbLb = Label(root, text="Naive Bayes", fg="black", bg="gray")
nbLb.grid(row=27, column=0, pady=10, sticky=W)

t1 = Text(root, height=1, width=20,bg="gray",fg="black")
t1.grid(row=21, column=1, padx=0)

t2 = Text(root, height=1, width=20,bg="gray",fg="black")
t2.grid(row=23, column=1 , padx=0)

t3 = Text(root, height=1, width=20,bg="gray",fg="black")
t3.grid(row=25, column=1 , padx=0)

t4 = Text(root, height=1, width=20,bg="gray",fg="black")
t4.grid(row=27, column=1 , padx=0)


lst = sorted(["Yes", "No"])


S1 = OptionMenu(root, Age, *lst)
S1.grid(row=7, column=1)
#S1.pack()
S1.config(font=('calibri',(10)),bg='gray',width=12)
S1['menu'].config(font=('calibri',(10)),bg='gray')

S2 = OptionMenu(root, BMI, *lst)
S2.grid(row=8, column=1)
#S2.pack()
S2.config(font=('calibri',(10)),bg='gray',width=12)
S2['menu'].config(font=('calibri',(10)),bg='gray')

S3 = OptionMenu(root, Gender, *lst)
S3.grid(row=9, column=1)
#S3.pack()
S3.config(font=('calibri',(10)),bg='gray',width=12)
S3['menu'].config(font=('calibri',(10)),bg='gray')

S4 = OptionMenu(root, smoker, *lst)
S4.grid(row=10, column=1)
#S4.pack()
S4.config(font=('calibri',(10)),bg='gray',width=12)
S4['menu'].config(font=('calibri',(10)),bg='gray')

S5 = OptionMenu(root, cigsPerDay, *lst)
S5.grid(row=11, column=1)
#S5.pack()
S5.config(font=('calibri',(10)),bg='gray',width=12)
S5['menu'].config(font=('calibri',(10)),bg='gray')

S6 = OptionMenu(root, BPMeds, *lst)
S6.grid(row=12, column=1)
#S6.pack()
S6.config(font=('calibri',(10)),bg='gray',width=12)
S6['menu'].config(font=('calibri',(10)),bg='gray')

S7 = OptionMenu(root, diabetes, *lst)
S7.grid(row=13, column=1)
#S7.pack()
S7.config(font=('calibri',(10)),bg='gray',width=12)
S7['menu'].config(font=('calibri',(10)),bg='gray')

S8 = OptionMenu(root, prevalentStroke, *lst)
S8.grid(row=7, column=4)
#S8En.pack()
S8.config(font=('calibri',(10)),bg='gray',width=12)
S8['menu'].config(font=('calibri',(10)),bg='gray')

S9 = OptionMenu(root, prevalentHyp, *lst)
S9.grid(row=8, column=4)
#S9.pack()
S9.config(font=('calibri',(10)),bg='gray',width=12)
S9['menu'].config(font=('calibri',(10)),bg='gray')

S10 = OptionMenu(root, heartRate, *lst)
S10.grid(row=9, column=4)
#S10.pack()
S10.config(font=('calibri',(10)),bg='gray',width=12)
S10['menu'].config(font=('calibri',(10)),bg='gray')

S11 = OptionMenu(root, glucose, *lst)
S11.grid(row=10, column=4)
#S11.pack()
S11.config(font=('calibri',(10)),bg='gray',width=12)
S11['menu'].config(font=('calibri',(10)),bg='gray')

S12 = OptionMenu(root, sysBP, *lst)
S12.grid(row=11, column=4)
#S12.pack()
S12.config(font=('calibri',(10)),bg='gray',width=12)
S12['menu'].config(font=('calibri',(10)),bg='gray')

S13 = OptionMenu(root, totChol, *lst)
S13.grid(row=12, column=4)
#S13.pack()
S13.config(font=('calibri',(10)),bg='gray',width=12)
S13['menu'].config(font=('calibri',(10)),bg='gray')

S14 = OptionMenu(root, diaBP, *lst)
S14.grid(row=13, column=4)
#S14.pack()
S14.config(font=('calibri',(10)),bg='gray',width=12)
S14['menu'].config(font=('calibri',(10)),bg='gray')

def yes():
    print("hello Word")

pred = Label(root, text="Prediction", fg="red", bg="gray")
pred.config(font=("Elephant", 30))
pred.grid(row=19, column=3, columnspan=2, padx=35)

pl = Button(root, justify = LEFT, text="Prolog Prediction", command=yes, bg="gray",fg="black")
pl.grid(row=21, column=3,padx=10, sticky = W)

bn = Button(root, justify = LEFT, text="Bayesian Network Prediction", command=yes, bg="gray",fg="black")
bn.grid(row=23, column=3,padx=10, sticky = W)

nn = Button(root, justify = LEFT, text="Neural Network Prediction", command=yes, bg="gray",fg="black")
nn.grid(row=25, column=3,padx=10, sticky = W)

nb = Button(root, justify = LEFT, text="Naive Bayes Prediction", command=yes, bg="gray",fg="black")
nb.grid(row=27, column=3,padx=10, sticky = W)



#textfileds
t5 = Text(root, height=1, width=20,bg="gray",fg="black")
t5.grid(row=21, column=4, padx=10)

t6 = Text(root, height=1, width=20,bg="gray",fg="black")
t6.grid(row=23, column=4, padx=10)

t7 = Text(root, height=1, width=20,bg="gray",fg="black")
t7.grid(row=25, column=4, padx=10)

t8 = Text(root, height=1, width=20,bg="gray",fg="black")
t8.grid(row=27, column=4, padx=10)




root.mainloop()