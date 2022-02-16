__author__ = "Mohamed B Traore"


from functools import partial
from tkinter import *
import glob as gl
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk,Image

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
## SMOTE
import imblearn as imb
from imblearn.over_sampling import SMOTE
from collections import Counter
## Partie machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

#========================================================================
class Myapp :
    #---------------------------------------------------------------------------------------
    def __init__ (self,master):
        self.master = master
        self.bottom = Frame (self.master,width=720,height=300)
        self.bottom.grid(column=0,row=1,sticky='nsew')

        self.top = Frame (self.master,width=720,height=100,padx=20, pady=20, highlightbackground="gray", highlightthickness=2)
        self.top.grid(column=0,row=0,sticky='nsew')
        

        self.left = Frame (self.master,width=720)
        self.left.grid(column=0,row=2,sticky='nsew')

        self.right = Frame (self.master,width=720)
        self.right.grid(column=0,row=3,sticky='nsew')
 
        self.CreatWid()


    def clearFrame(self):
       for widget in self.bottom.winfo_children():
           widget.destroy()
           
         
      
    def predire(self):

        self.clearFrame()

        self.income_form = Entry(self.bottom);
        self.income_t = "Revenu annuel"
        self.income = Label (self.bottom, text = self.income_t,font=("verdana",11)) ;
        self.income.place(x=120,y=30)
        self.income_form.place(x=280,y=30)

        self.age_t = "Age"
        self.age = Label (self.bottom, text = self.age_t,font=("verdana",11)) ;
        self.age_form = Entry(self.bottom)
        self.age.place(x=120,y=80)
        self.age_form.place(x=280,y=80)
   

        self.loan_t = "Crédit à rembourser"
        self.loan = Label (self.bottom, text = self.loan_t,font=("verdana",11)) ; 
        self.loan_form = Entry(self.bottom)
        self.loan.place(x=120,y=130)
        self.loan_form.place(x=280,y=130)

        def Model(income,age,loan):
            data = pd.read_csv("data/original.csv") # the path should be adapted based on the project
            data.dropna(inplace=True)
            X = data.drop(["clientid","default"], axis=1)
            y=data["default"]

            oversample = SMOTE()
            X,y = oversample.fit_resample(X, y)

            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
            model = LogisticRegression(random_state = 37, max_iter=1000)
            model.fit(X_train, y_train)
            p = np.array([[income,age,loan]])
            return model.predict(p)


            

        def val():
            income_test = self.income_form.get()
            age_test = self.age_form.get()
            loan_test = self.loan_form.get()
            x=Model(int(income_test),int(age_test),int(loan_test))
            self.reponse_v_t = "Ce client est solvable "
            self.reponse_v = Label (self.bottom, text = self.reponse_v_t,font=("verdana",10),fg="red") ; 
            self.reponse_f_t = "Ce client n'est pas solvable "
            self.reponse_f = Label (self.bottom, text = self.reponse_f_t,font=("verdana",10),fg="red") ; 
            print(x)
            if(x==0):
                print(True)
                self.reponse_v.place(x=200,y=220)
            else:
                print(False)
                self.reponse_f.place(x=200,y=220)
            

        def renitialiser():
            self.loan_form.delete(0,END)
            self.age_form.delete(0,END)
            self.income_form.delete(0,END)
            self.reponse_v.destroy()
            self.reponse_f.destroy()
            
        self.resultat = Button (self.bottom, text = "Résultat", command = val)
        self.Back = Button (self.bottom, text = "Réinitialiser", command = renitialiser); 
        self.resultat.place(x=120,y=180)
        self.Back.place(x=220,y=180)

        self.loan_t = "Resultat : "
        self.loan = Label (self.bottom, text = self.loan_t,font=("verdana",10)) ; 
        self.loan.place(x=120,y=220)
        
        
    
        
        



        
   
   #def visualiser(self):
   #   self.clearFrame()
   #   self.image1=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
   #   self.image1_img = PhotoImage(file = "assets/plot1.png")
   #   self.image1_image = Label (self.bottom, image = self.image1_img)

   #   self.image2=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
   #   self.image2_img = PhotoImage(file = "assets/default.png")
   #   self.image2_image = Label (self.bottom, image = self.image2_img)

   #   self.image3=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
   #   self.image3_img = PhotoImage(file = "assets/default.png")
   #   self.image3_image = Label (self.bottom, image = self.image3_img)

   #   self.image4=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
   #   self.image4_img = PhotoImage(file = "assets/default.png")
   #   self.image4_image = Label (self.bottom, image = self.image4_img)

   #   self.image1.place(x=100,y=65)
   #   self.image1_image.place(x=500,y=60)
   #   self.image2.place(x=100,y=135)
   #   self.image2_image.place(x=500,y=120)
   #   self.image3.place(x=100,y=195)
   #   self.image3_image.place(x=500,y=180)
   #   self.image4.place(x=100,y=255)
   #   self.image4_image.place(x=500,y=240)
  
    def about(self):
       self.clearFrame()
       self.Mohamed=Label(self.bottom,text="Mohamed Bourema Traore",font=("verdana",10),fg="black")
       self.Mohamed_img = PhotoImage(file = "assets/momo.png")
       self.Mohamed_image = Label (self.bottom, image = self.Mohamed_img)

       self.Ouhmidou=Label(self.bottom,text="Ouhmidou Souha",font=("verdana",10),fg="black")
       self.Ouhmidou_img = PhotoImage(file = "assets/Souha.png")
       self.Ouhmidou_image = Label (self.bottom, image = self.Ouhmidou_img)

       self.Moulad=Label(self.bottom,text="Moulad Chaïmaâ",font=("verdana",10),fg="black")
       self.Moulad_img = PhotoImage(file = "assets/Moulad.png")
       self.Moulad_image = Label (self.bottom, image = self.Moulad_img)

       self.Hakkou=Label(self.bottom,text="Hakkou El Mehdi",font=("verdana",10),fg="black")
       self.Hakkou_img = PhotoImage(file = "assets/Mehdi.png")
       self.Hakkou_image = Label (self.bottom, image = self.Hakkou_img)

       Presentatiion = Label(self.bottom,font=("verdana",11),text="Les étudiants ayant réalisés ce travail sont :")
       description = Label(self.bottom,font=("verdana",11),text="Ce travail a été par 4 élèves ingenieurs de la filière IDF, dans le cadre du projet du module : \nRéseaux de Neurones")
       self.Mohamed.place(x=520,y=270)
       self.Mohamed_image.place(x=520,y=90)
       self.Ouhmidou.place(x=370,y=270)
       self.Ouhmidou_image.place(x=370,y=90)
       self.Moulad.place(x=220,y=270)
       self.Moulad_image.place(x=220,y=90)
       self.Hakkou.place(x=70,y=270)
       self.Hakkou_image.place(x=70,y=90)
       description.place(x=50,y=10)
       Presentatiion.place(x=50,y=50)

    def help(self):
        self.clearFrame()
        Presentatiion = Label(self.bottom,font=("verdana",11),text="\n\n\tCette application permet de prédire la solvabilité d'un emprunteur qui est une préoccupation des  sociétés financières. Elle  se base sur les réseaux de  neurones  plus précisement sur la \"Logistic Regression\". Elle fonctionne  de la manière suivante :  Nous\ndevons  fournir  les  informations  suivantes: le  revenu annuel du  client, son âge  et  le\nmontant  de ses  emprunts non remboursés. En  se basant sur ces données, le modèle\nva prédire si le client est solvable ou non.",justify = LEFT,wraplength=715)
        Presentatiion.place(x=0,y=0)
         

    def CreatWid(self):
    
         self.bienvenue=Label(self.top,text="Prédiction de risque crédit",font=("verdana",12),fg="black")
        # self.description=Label(self.top,text=" Cette application est associé à un modèle un algorithme qui predit la solavabilité d'un client",font=("verdana",11),fg="black")
         self.predire = Button(self.top,text="Predire", command = self.predire)
         #self.visualiser = Button(self.top,text="Visualiser", command = self.visualiser)
         self.about = Button (self.top, text = "Créateurs", command = self.about)
         self.help = Button (self.top, text = "À propos", command = self.help)
         self.bienvenue.place(x=170,y=0)
        # self.description.place(x=20,y=20)
         self.predire.place(x=220,y=50)
        # self.visualiser.place(x=290,y=50)
         self.about.place(x=290,y=50)
         self.help.place(x=375,y=50)
         


if __name__ == "__main__":
    root = Tk()
    root.title("Gestion de risque crédit")
    root.geometry("720x400")
    root.title("Application")
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)
    app = Myapp (root)
    root.mainloop()
    