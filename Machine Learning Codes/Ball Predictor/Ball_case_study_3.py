
from sklearn import tree

def Ballpredictor():
    
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,0],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    Labels= [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Labels)

    print(obj.predict([[97,0]]))

def main():

    print("----------------Ball predictor case study--------------------")

    Ballpredictor()

if __name__ == "__main__":
    main()





