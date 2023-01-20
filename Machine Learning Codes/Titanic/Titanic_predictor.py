import math 
import numpy as np 
import pandas as pd
import seaborn as sns 
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure , show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def Titaniclogistic():

    titanic_data = pd.read_csv('MarvellousTitanicDataset.csv')
    print("first five entries in dataset:")
    print(titanic_data.head())

    print("number of passangers are "+str(len(titanic_data)))

    print("visualisation :Survived and non survived passangers")
    figure()
    target = "Survived"

    countplot(data =titanic_data,x = target,hue = "Sex").set_title("marvellous infosystem:Survived and non survived passangers based on gender")
    show()

    print("visualisation :Survived and non survived passangers based on the passangers class")
    figure()
    target = "Survived"

    countplot(data = titanic_data,x=target,hue="Pclass").set_title("marvellous infosystem :Survived and survived passagers based on the pasanger class")
    show()

    print("visualisation :Survived and non survived passangers based on age")
    figure()
    titanic_data["Age"].plot.hist().set_title("marvellous infosystem :Survived and non survived passangers based on  age")
    show()

    print("visualization :Survived and non survied passangers based on the fare")
    figure()
    titanic_data['Fare'].plot.hist().set_title("marvellous infosystem:Survived and non survived passangers based on fare")
    show()

    titanic_data.drop("zero",axis= 1, inplace=True)

    print("first five from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first= True)
    print(Sex.head(5))

    print("values of Pclass column after removing one field")
    Pclass= pd.get_dummies(titanic_data["Pclass"],drop_first =True)
    print(Pclass.head(5))

    print("values of data set after concatenaing new columns")
    titanic_data = pd.concat([titanic_data ,Sex,Pclass],axis=1)
    print(titanic_data.head(5))

    print("values of dataset after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis=1,inplace= True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived",axis=1)
    y = titanic_data["Survived"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)

    model = LogisticRegression()

    model.fit(x_train,y_train)
    prediction =model.predict(x_test)

    print("classification report of logistic regression ")
    print(classification_report(y_test,prediction))

    print("confusion matrics of logistic regression is")
    print(confusion_matrix(y_test,prediction))

    print("Accuracy score of logistic regression is:")
    print(accuracy_score(y_test,prediction))



def main():
    print("supervised machine learning..")

    print("logistic regression on titanic data set...")

    Titaniclogistic()


if __name__ =="__main__":
    main()