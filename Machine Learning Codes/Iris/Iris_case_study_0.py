
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier():

    Dataset =load_iris()   #............Load data

    Data = Dataset.data
    Target = Dataset.target

    # ....Manipulate the data
    Data_train , data_test , Target_train , Target_test = train_test_split(Data,Target, test_size= 0.5)

    Classifier = KNeighborsClassifier()

    Classifier.fit(Data_train,Target_train)     #............train the data

    predictions = Classifier.predict(data_test) #...........test the data

    Accuracy = accuracy_score(Target_test,predictions)   

    return Accuracy

def main():

    Ret = MarvellousKNeighborsClassifier()

    print("Accuracy of Iris dataset with KNN is :",Ret * 100)
    

if __name__ =="__main__":
    main()


