import tkinter as tk
from tkinter import *

LARGE_FONT= ("Verdana", 12)

def yes():
    print("hello Word")



class MainPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        # entry variables
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, justify='left', text="\t           HOME: \n Evaluating Risk of Coronary Heart Disease", fg="black", bg="gray")
        label.config(font=("Elephant", 25))
        label.grid(row = 30, column = 10, pady=200,padx=350)
        
        

        button = tk.Button(self, justify = 'center',text="General Models",
                            command=lambda: controller.show_frame(PageOne))
        button.config(font=("Elephant", 20))
        button.grid(row = 35, column = 10, pady=0,padx=100)

        button2 = tk.Button(self, justify = 'center', text="Custom Prolog Query",
                            command=lambda: controller.show_frame(PageTwo))
        button2.config(font=("Elephant", 20))
        button2.grid(row = 40, column = 10, pady=0,padx=100)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.geometry("1200x1200")
        label = tk.Label(self, justify="center", text="Evaluating Risk of Coronary Heart Disease", fg="black", bg="gray")
        label.config(font=("Elephant", 25))
        label.grid(row = 0, column = 0, pady=10,padx=10)

        Age = tk.StringVar()
        Age.set(None)
        BMI = tk.StringVar()
        BMI.set(None)
        Gender = tk.StringVar()
        Gender.set("male")

        smoker = tk.StringVar()
        smoker.set("Yes")

        cigsPerDay = tk.StringVar()
        cigsPerDay.set(0)

        BPMeds = tk.StringVar()
        BPMeds.set("No")

        diabetes = tk.StringVar()
        diabetes.set("No")

        prevalentStroke = tk.StringVar()
        prevalentStroke.set("No")

        prevalentHyp = tk.StringVar()
        prevalentHyp.set("No")

        heartRate = tk.StringVar()
        heartRate.set(None)

        glucose = tk.StringVar()
        glucose.set(None)

        sysBP = tk.StringVar()
        sysBP.set(None)

        totChol = tk.StringVar()
        totChol.set(None)

        diaBP = tk.StringVar()
        diaBP.set(None)

        S1Lb = Label(self, text="Age", fg="black", bg="gray")
        S1Lb.grid(row=7, column=0, padx = 10, pady=10, sticky=W)

        S2Lb = Label(self, text="BMI", fg="black", bg="gray")
        S2Lb.grid(row=8, column=0, padx = 10,pady=10, sticky=W)

        S3Lb = Label(self, text="Gender", fg="black", bg="gray")
        S3Lb.grid(row=9, column=0, padx = 10,pady=10, sticky=W)

        S4Lb = Label(self, text="Are you a smoker?", fg="black", bg="gray")
        S4Lb.grid(row=10, column=0,padx = 10, pady=10, sticky=W)

        S5Lb = Label(self, text="Cigerates consumed per day:", fg="black", bg="gray")
        S5Lb.grid(row=11, column=0,padx = 10, pady=10, sticky=W)


        S6Lb = Label(self, text="Are you taking BM Meds?", fg="black", bg="gray")
        S6Lb.grid(row=12, column=0,padx = 10, pady=10, sticky=W)

        S7Lb = Label(self, text="Are you diabetic?", fg="black", bg="gray")
        S7Lb.grid(row=13, column=0,padx = 10, pady=10, sticky=W)


        S8Lb = Label(self, justify = LEFT,  text="Prevalent Stroke?", fg="black", bg="gray")
        S8Lb.grid(row=7, column=3, pady=10, sticky=W)

        S9Lb = Label(self, justify = LEFT, text="Prevalent Hypertension?", fg="black", bg="gray")
        S9Lb.grid(row=8, column=3, pady=10, sticky=W)

        S10Lb = Label(self, justify = LEFT, text="Heart Rate", fg="black", bg="gray")
        S10Lb.grid(row=9, column=3, pady=10, sticky=W)

        S11Lb = Label(self, justify = LEFT,  text="Glucose", fg="black", bg="gray")
        S11Lb.grid(row=10,  column=3, pady=10, sticky=W)

        S12Lb = Label(self, justify = LEFT, text="Systolic BP", fg="black", bg="gray")
        S12Lb.grid(row=11, column=3, pady=10, sticky=W)

        S13Lb = Label(self, justify = LEFT, text="Total Cholestrol", fg="black", bg="gray")
        S13Lb.grid(row=12, column=3, pady=10, sticky=W)

        S14Lb = Label(self, justify = LEFT,  text="Diabolic BP", fg="black", bg="gray")
        S14Lb.grid(row=13, column=3, pady=10, sticky=W)

        accuracy = Label(self, justify = LEFT, text="Accuracy", fg="red", bg="gray")
        accuracy.config(font=("Elephant", 30))
        accuracy.grid(row=19, column=0, columnspan=2, padx=20)

        plLb = Label(self, text="Prolog", fg="black", bg="gray")
        plLb.grid(row=21, column=0, pady=10,sticky=W)

        bnlb = Label(self, text="Bayesian Network", fg="black", bg="gray")
        bnlb.grid(row=23, column=0, pady=10, sticky=W)

        nnLb = Label(self, text="Neural Network", fg="black", bg="gray")
        nnLb.grid(row=25, column=0, pady=10, sticky=W)

        nbLb = Label(self, text="Naive Bayes", fg="black", bg="gray")
        nbLb.grid(row=27, column=0, pady=10, sticky=W)

        t1 = Text(self, height=1, width=20,bg="gray",fg="black")
        t1.grid(row=21, column=1, padx=0)

        t2 = Text(self, height=1, width=20,bg="gray",fg="black")
        t2.grid(row=23, column=1 , padx=0)

        t3 = Text(self, height=1, width=20,bg="gray",fg="black")
        t3.grid(row=25, column=1 , padx=0)

        t4 = Text(self, height=1, width=20,bg="gray",fg="black")
        t4.grid(row=27, column=1 , padx=0)


        lst = sorted(["Yes", "No"])


        S1 = OptionMenu(self, Age, *lst)
        S1.grid(row=7, column=1)
        #S1.pack()
        S1.config(font=('calibri',(10)),bg='gray',width=12)
        S1['menu'].config(font=('calibri',(10)),bg='gray')

        S2 = OptionMenu(self, BMI, *lst)
        S2.grid(row=8, column=1)
        #S2.pack()
        S2.config(font=('calibri',(10)),bg='gray',width=12)
        S2['menu'].config(font=('calibri',(10)),bg='gray')

        S3 = OptionMenu(self, Gender, *lst)
        S3.grid(row=9, column=1)
        #S3.pack()
        S3.config(font=('calibri',(10)),bg='gray',width=12)
        S3['menu'].config(font=('calibri',(10)),bg='gray')

        S4 = OptionMenu(self, smoker, *lst)
        S4.grid(row=10, column=1)
        #S4.pack()
        S4.config(font=('calibri',(10)),bg='gray',width=12)
        S4['menu'].config(font=('calibri',(10)),bg='gray')

        S5 = OptionMenu(self, cigsPerDay, *lst)
        S5.grid(row=11, column=1)
        #S5.pack()
        S5.config(font=('calibri',(10)),bg='gray',width=12)
        S5['menu'].config(font=('calibri',(10)),bg='gray')

        S6 = OptionMenu(self, BPMeds, *lst)
        S6.grid(row=12, column=1)
        #S6.pack()
        S6.config(font=('calibri',(10)),bg='gray',width=12)
        S6['menu'].config(font=('calibri',(10)),bg='gray')

        S7 = OptionMenu(self, diabetes, *lst)
        S7.grid(row=13, column=1)
        #S7.pack()
        S7.config(font=('calibri',(10)),bg='gray',width=12)
        S7['menu'].config(font=('calibri',(10)),bg='gray')

        S8 = OptionMenu(self, prevalentStroke, *lst)
        S8.grid(row=7, column=4)
        #S8En.pack()
        S8.config(font=('calibri',(10)),bg='gray',width=12)
        S8['menu'].config(font=('calibri',(10)),bg='gray')

        S9 = OptionMenu(self, prevalentHyp, *lst)
        S9.grid(row=8, column=4)
        #S9.pack()
        S9.config(font=('calibri',(10)),bg='gray',width=12)
        S9['menu'].config(font=('calibri',(10)),bg='gray')

        S10 = OptionMenu(self, heartRate, *lst)
        S10.grid(row=9, column=4)
        #S10.pack()
        S10.config(font=('calibri',(10)),bg='gray',width=12)
        S10['menu'].config(font=('calibri',(10)),bg='gray')

        S11 = OptionMenu(self, glucose, *lst)
        S11.grid(row=10, column=4)
        #S11.pack()
        S11.config(font=('calibri',(10)),bg='gray',width=12)
        S11['menu'].config(font=('calibri',(10)),bg='gray')

        S12 = OptionMenu(self, sysBP, *lst)
        S12.grid(row=11, column=4)
        #S12.pack()
        S12.config(font=('calibri',(10)),bg='gray',width=12)
        S12['menu'].config(font=('calibri',(10)),bg='gray')

        S13 = OptionMenu(self, totChol, *lst)
        S13.grid(row=12, column=4)
        #S13.pack()
        S13.config(font=('calibri',(10)),bg='gray',width=12)
        S13['menu'].config(font=('calibri',(10)),bg='gray')

        S14 = OptionMenu(self, diaBP, *lst)
        S14.grid(row=13, column=4)
        #S14.pack()
        S14.config(font=('calibri',(10)),bg='gray',width=12)
        S14['menu'].config(font=('calibri',(10)),bg='gray')

        

        pred = Label(self, text="Prediction", fg="red", bg="gray")
        pred.config(font=("Elephant", 30))
        pred.grid(row=19, column=3, columnspan=2, padx=35)

        pl = Button(self, justify = LEFT, text="Prolog Prediction", command=yes, bg="gray",fg="black")
        pl.grid(row=21, column=3,padx=10, sticky = W)

        bn = Button(self, justify = LEFT, text="Bayesian Network Prediction", command=yes, bg="gray",fg="black")
        bn.grid(row=23, column=3,padx=10, sticky = W)

        nn = Button(self, justify = LEFT, text="Neural Network Prediction", command=yes, bg="gray",fg="black")
        nn.grid(row=25, column=3,padx=10, sticky = W)

        nb = Button(self, justify = LEFT, text="Naive Bayes Prediction", command=yes, bg="gray",fg="black")
        nb.grid(row=27, column=3,padx=10, sticky = W)



        #textfileds
        t5 = Text(self, height=1, width=20,bg="gray",fg="black")
        t5.grid(row=21, column=4, padx=10)

        t6 = Text(self, height=1, width=20,bg="gray",fg="black")
        t6.grid(row=23, column=4, padx=10)

        t7 = Text(self, height=1, width=20,bg="gray",fg="black")
        t7.grid(row=25, column=4, padx=10)

        t8 = Text(self, height=1, width=20,bg="gray",fg="black")
        t8.grid(row=27, column=4, padx=10)



        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.config(font=("Elephant", 20))
        button1.grid(row = 30, column = 2, padx = 0)
        button2 = tk.Button(self, text="Custom Prolog Query",
                            command=lambda: controller.show_frame(PageTwo))
        button2.config(font=("Elephant", 20))
        button2.grid(row = 34, column = 2, padx = 0)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Custom Prolog Query", font=LARGE_FONT)
        label.config(font=("Elephant", 25))
        label.grid(row = 30, column = 10, pady=200,padx=450)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.config(font=("Elephant", 20))
        
        button1.grid(row = 35, column = 10, pady=0,padx=150)

        button2 = tk.Button(self, text="General Models",
                            command=lambda: controller.show_frame(PageOne))
        button2.config(font=("Elephant", 20))
        button2.grid(row = 40, column = 10, pady=0,padx=150)
        


app = MainPage()
app.mainloop()