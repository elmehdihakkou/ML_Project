"""
COMMENT WHAT YOU WANT
"""

# Importation des librairies

## Initiales
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

# Lecture ddu dataset dans la variable data
data = pd.read_csv("data/original.csv") # the path should be adapted based on the project

"""
La partie de la visualisation dépend forcémenet de la nature de l'interface graphique
"""
# ============================
# = Problème Imbalanced Data =
# ============================ 

# Vu le problème de diséquilibre de notre data on va procéder par la méthode SMOTE afin de la règler

# Pour utiliser la fonction de suréchantillonage notre data ne doit pas contenir de NaN Values
data.dropna(inplace=True)
X = data.drop(["clientid","default"], axis=1)
y=data["default"]

# Importation de la fonction SMOTE
oversample = SMOTE()
X,y = oversample.fit_resample(X, y)


# ============================
# = Partie Machine Learning  =
# ============================ 

#Ici nous divisons notre data sur une base d'apprentissage(80%) et une base d'entraînement (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

#On crée le modèle:
model = LogisticRegression(random_state = 37, max_iter=1000)
#On entraîne le modèle:
model.fit(X_train, y_train)

print("La précision du modèle est de : ", model.score(X_test, y_test)*100,"%")

def getmyPredction(income, age, loan):
    p = np.array([[income,age,loan]])
    return model.predict(p)

income_test = input("Fill in your income: ")
age_test = input("Fill in your age: ")
loan_test = input("Fill in your loan: ")

print(getmyPredction(income_test, age_test, loan_test))