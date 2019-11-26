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

S12Lb = Label(root, justify = LEFT, text="Sys BP", fg="black", bg="gray")
S12Lb.grid(row=11, column=3, pady=10, sticky=W)

S13Lb = Label(root, justify = LEFT, text="Total Cholestrol", fg="black", bg="gray")
S13Lb.grid(row=12, column=3, pady=10, sticky=W)

S14Lb = Label(root, justify = LEFT,  text="Dia BP", fg="black", bg="gray")
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


S1En = OptionMenu(root, Age, *lst)
S1En.grid(row=7, column=1)
#S1En.pack()
S1En.config(font=('calibri',(10)),bg='gray',width=12)
S1En['menu'].config(font=('calibri',(10)),bg='gray')

S2En = OptionMenu(root, BMI, *lst)
S2En.grid(row=8, column=1)
#S2En.pack()
S2En.config(font=('calibri',(10)),bg='gray',width=12)
S2En['menu'].config(font=('calibri',(10)),bg='gray')

S3En = OptionMenu(root, Gender, *lst)
S3En.grid(row=9, column=1)
#S3En.pack()
S3En.config(font=('calibri',(10)),bg='gray',width=12)
S3En['menu'].config(font=('calibri',(10)),bg='gray')

S4En = OptionMenu(root, smoker, *lst)
S4En.grid(row=10, column=1)
#S4En.pack()
S4En.config(font=('calibri',(10)),bg='gray',width=12)
S4En['menu'].config(font=('calibri',(10)),bg='gray')

S5En = OptionMenu(root, cigsPerDay, *lst)
S5En.grid(row=11, column=1)
#S5En.pack()
S5En.config(font=('calibri',(10)),bg='gray',width=12)
S5En['menu'].config(font=('calibri',(10)),bg='gray')

S6En = OptionMenu(root, BPMeds, *lst)
S6En.grid(row=12, column=1)
#S6En.pack()
S6En.config(font=('calibri',(10)),bg='gray',width=12)
S6En['menu'].config(font=('calibri',(10)),bg='gray')

S7En = OptionMenu(root, diabetes, *lst)
S7En.grid(row=13, column=1)
#S7En.pack()
S7En.config(font=('calibri',(10)),bg='gray',width=12)
S7En['menu'].config(font=('calibri',(10)),bg='gray')

S8En = OptionMenu(root, prevalentStroke, *lst)
S8En.grid(row=7, column=4)
#S8En.pack()
S8En.config(font=('calibri',(10)),bg='gray',width=12)
S8En['menu'].config(font=('calibri',(10)),bg='gray')

S9En = OptionMenu(root, prevalentHyp, *lst)
S9En.grid(row=8, column=4)
#S9En.pack()
S9En.config(font=('calibri',(10)),bg='gray',width=12)
S9En['menu'].config(font=('calibri',(10)),bg='gray')

S10En = OptionMenu(root, heartRate, *lst)
S10En.grid(row=9, column=4)
#S10En.pack()
S10En.config(font=('calibri',(10)),bg='gray',width=12)
S10En['menu'].config(font=('calibri',(10)),bg='gray')

S11En = OptionMenu(root, glucose, *lst)
S11En.grid(row=10, column=4)
#S11En.pack()
S11En.config(font=('calibri',(10)),bg='gray',width=12)
S11En['menu'].config(font=('calibri',(10)),bg='gray')

S12En = OptionMenu(root, sysBP, *lst)
S12En.grid(row=11, column=4)
#S12En.pack()
S12En.config(font=('calibri',(10)),bg='gray',width=12)
S12En['menu'].config(font=('calibri',(10)),bg='gray')

S13En = OptionMenu(root, totChol, *lst)
S13En.grid(row=12, column=4)
#S13En.pack()
S13En.config(font=('calibri',(10)),bg='gray',width=12)
S13En['menu'].config(font=('calibri',(10)),bg='gray')

S14En = OptionMenu(root, diaBP, *lst)
S14En.grid(row=13, column=4)
#S14En.pack()
S14En.config(font=('calibri',(10)),bg='gray',width=12)
S14En['menu'].config(font=('calibri',(10)),bg='gray')

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