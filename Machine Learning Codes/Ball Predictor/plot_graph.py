import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import tree

def Ball_predict(path):
    data = pd.read_csv(path,index_col=0)
    print("size of dataset is:",len(data))


    features_name = ['Weight','Pattern']
    print("Name of features :",features_name)

    Weight = data.Weight
    Pattern = data.Pattern
    Label = data.Label

    Ret = preprocessing.LabelEncoder()
    pattern_encoded = Ret.fit_transform(Pattern)
    print(pattern_encoded)

    label_encoded = Ret.fit_transform(Label)
    print(label_encoded)

    features = list(zip(Weight,pattern_encoded))

    model =tree.DecisionTreeClassifier()

    model = model.fit(features,label_encoded)

    ret = (model.predict([[35,1]]))
    print(ret)








    




def main():

    Ball_predict("BallPredictor.csv")

if __name__ =="__main__":
    main()


