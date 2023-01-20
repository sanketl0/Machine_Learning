import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


def Playpredictor(path):
    data = pd.read_csv(path,index_col = 0)
    print("Size of Actual dataset",len(data))

    features_name = ['Whether','Temperature']
    print("Name of features",features_name)

    Whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    Ret = preprocessing.LabelEncoder()

    weather_encoded = Ret.fit_transform(Whether)
    print(weather_encoded)

    temp_encoded = Ret.fit_transform(Temperature)
    print(temp_encoded)

    label = Ret.fit_transform(play)
    print("labels are:",'\n',label)

    feature = list(zip(weather_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(feature,label)
    predicted = model.predict([[0,2]])
    print("predicted result by algorithm",'\n' ,predicted)

    if predicted:
        print("You can play")
    else:
        print("You Can't Play")


def main():

    print("Machine learning case study ....")
    print("KNN algorithm are used in ")

    try:
        
        Playpredictor("PlayPredictor.csv")

    except Exception as e:
        print("Error:",e)

        
if __name__ =="__main__":
    main()
