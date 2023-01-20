from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def svms():
    #load datasets
    cancer = datasets.load_breast_cancer()

    #print the names of the 13 features
    print("Labels of the ccancer dataset:",cancer.feature_names)

    #print the label type of cancer ('malignemt 'benign')
    print("Labels of the cancer datasets:",cancer.target_names)

    #print data(feature)shape
    print("shape of dataset is:",cancer.data.shape)

    #print tge cancer data features top 5 records
    print(cancer.data[0:5])

    #print the cancer lable (0:malignent ,1:benign)
    print("Target of dataset;",cancer.target)

    #split dataset into training set and testing set
    x_train ,X_test , y_train, y_test =train_test_split(cancer.data,cancer.target,test_size = 0.3,random_state =109)

    #create a svm classifier
    model = svm.SVC(kernel = 'linear')

    #train the model using training data
    model.fit(x_train,y_train)

    #predict the responce for the test dataset
    y_pred = model.predict(X_test)

    #model accuracy :how often is the classifier correct
    print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred)*100)


def main():
    print("support vector machine algorithm")

    svms()

if __name__ =="__main__":
    main()