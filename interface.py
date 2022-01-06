__author__ = "Hicham S'hih"


from tkinter import *
import glob as gl
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk,Image

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
           
    def resultat(self):
        self.clearFrame()
        Presentatiion = Label(self.bottom,font=("verdana",11),text="Ce client est risqueux/non risqueux")
        Presentatiion.place(x=0,y=0)
      
         
      
    def predire(self):

        self.clearFrame()

        self.income_form = Entry(self.bottom)
        self.income_t = "Income"
        self.income = Label (self.bottom, text = self.income_t,font=("verdana",11)) ;
        self.income.place(x=120,y=30)
        self.income_form.place(x=220,y=30)

        self.age_t = "Age"
        self.age = Label (self.bottom, text = self.age_t,font=("verdana",11)) ;
        self.age_form = Entry(self.bottom);
        self.age.place(x=120,y=80)
        self.age_form.place(x=220,y=80)
   

        self.loan_t = "Loan"
        self.loan = Label (self.bottom, text = self.loan_t,font=("verdana",11)) ; 
        self.loan_form = Entry(self.bottom);
        self.loan.place(x=120,y=130)
        self.loan_form.place(x=220,y=130)

        self.resultat = Button (self.bottom, text = "Resultat", command = self.resultat)
        self.Back = Button (self.bottom, text = "Renitialiser", command = self.renitialiser); 
        self.resultat.place(x=120,y=180)
        self.Back.place(x=220,y=180)


        
    def renitialiser(self):
       
        self.clearFrame()

        self.income_form = Entry(self.bottom)
        self.income_t = "Income"
        self.income = Label (self.bottom, text = self.income_t,font=("verdana",11)) ;
        self.income.place(x=120,y=30)
        self.income_form.place(x=220,y=30)

        self.age_t = "Age"
        self.age = Label (self.bottom, text = self.age_t,font=("verdana",11)) ;
        self.age_form = Entry(self.bottom);
        self.age.place(x=120,y=80)
        self.age_form.place(x=220,y=80)
   

        self.loan_t = "Loan"
        self.loan = Label (self.bottom, text = self.loan_t,font=("verdana",11)) ; 
        self.loan_form = Entry(self.bottom);
        self.loan.place(x=120,y=130)
        self.loan_form.place(x=220,y=130)

        self.resultat = Button (self.bottom, text = "Resultat", command = self.resultat)
        self.Back = Button (self.bottom, text = "Renitialiser", command = self.renitialiser); 
        self.resultat.place(x=120,y=180)
        self.Back.place(x=220,y=180)

    
    def visualiser(self):
       self.clearFrame()
       self.image1=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
       self.image1_img = PhotoImage(file = "default.png")
       self.image1_image = Label (self.bottom, image = self.image1_img)

       self.image2=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
       self.image2_img = PhotoImage(file = "default.png")
       self.image2_image = Label (self.bottom, image = self.image2_img)

       self.image3=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
       self.image3_img = PhotoImage(file = "default.png")
       self.image3_image = Label (self.bottom, image = self.image3_img)

       self.image4=Label(self.bottom,text="description de l'image ",font=("verdana",10),fg="black")
       self.image4_img = PhotoImage(file = "default.png")
       self.image4_image = Label (self.bottom, image = self.image4_img)

       self.image1.place(x=100,y=65)
       self.image1_image.place(x=500,y=60)
       self.image2.place(x=100,y=135)
       self.image2_image.place(x=500,y=120)
       self.image3.place(x=100,y=195)
       self.image3_image.place(x=500,y=180)
       self.image4.place(x=100,y=255)
       self.image4_image.place(x=500,y=240)
  
    def about(self):
       self.clearFrame()
       self.Mohamed=Label(self.bottom,text="Mohamed Bourema Traore",font=("verdana",10),fg="black")
       self.Mohamed_img = PhotoImage(file = "momo.png")
       self.Mohamed_image = Label (self.bottom, image = self.Mohamed_img)

       self.Ouhmidou=Label(self.bottom,text="Ouhmidou Souha",font=("verdana",10),fg="black")
       self.Ouhmidou_img = PhotoImage(file = "momo.png")
       self.Ouhmidou_image = Label (self.bottom, image = self.Ouhmidou_img)

       self.Moulad=Label(self.bottom,text="Moulad Chaima",font=("verdana",10),fg="black")
       self.Moulad_img = PhotoImage(file = "momo.png")
       self.Moulad_image = Label (self.bottom, image = self.Moulad_img)

       self.Hakkou=Label(self.bottom,text="Hakkou El Mehdi",font=("verdana",10),fg="black")
       self.Hakkou_img = PhotoImage(file = "momo.png")
       self.Hakkou_image = Label (self.bottom, image = self.Hakkou_img)

       Presentatiion = Label(self.bottom,font=("verdana",11),text="Les étudiants ayant réalisés ce travail sont :")
       description = Label(self.bottom,font=("verdana",11),text="Ce travail est le fruit ")
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
        Presentatiion = Label(self.bottom,font=("verdana",11),text="Descpton de l'applcaton")
        Presentatiion.place(x=0,y=0)
         

    def CreatWid(self):
    
         self.bienvenue=Label(self.top,text="Bienvenue dans notre application",font=("verdana",12),fg="black")
        # self.description=Label(self.top,text=" Cette application est associé à un modèle un algorithme qui predit la solavabilité d'un client",font=("verdana",11),fg="black")
         self.predire = Button(self.top,text="Predire", command = self.predire)
         self.visualiser = Button(self.top,text="Visualiser", command = self.visualiser)
         self.about = Button (self.top, text = "About", command = self.about)
         self.help = Button (self.top, text = "Help", command = self.help)
         self.bienvenue.place(x=170,y=0)
        # self.description.place(x=20,y=20)
         self.predire.place(x=220,y=50)
         self.visualiser.place(x=290,y=50)
         self.about.place(x=370,y=50)
         self.help.place(x=440,y=50)
         


if __name__ == "__main__":
    root = Tk()
    root.title("Gestion Contacts")
    root.geometry("720x400")
    root.title("Application")
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)
    app = Myapp (root)
    root.mainloop()
    