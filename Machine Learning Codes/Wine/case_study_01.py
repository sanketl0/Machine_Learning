from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def winepredictor():
    #load dataset
    wine = datasets.load_wine()

    #print the names of the features
    print(wine.target_names)

    #print the label species(class_0,class_1, class_2)
    print(wine.target_names)

    #print the wine data (top 5 records)
    print(wine.data[0:5])

    #print the wine label (0:class_0, 1:class_1, 2:class_3)
    print(wine.target)

    #split dataset into training set and test set
    X_train, X_test ,y_train, y_test = train_test_split(wine.data,wine.target,test_size=0.3)

    #create KNN classifier
    Knn = KNeighborsClassifier(n_neighbors=3)

    #train the model using the training set
    Knn.fit(X_train,y_train)

    # predict the responce for test dataset
    y_pred = Knn.predict(X_test)

    #model accuracy how often is the classifier correct?
    print("Accuracy :",metrics.accuracy_score(y_test,y_pred))

def main():

    print("Machine learning Application:")

    print("Wine predictor application using k nearest knighbor algorithm")

    winepredictor()

if __name__ =="__main__":
    main()


