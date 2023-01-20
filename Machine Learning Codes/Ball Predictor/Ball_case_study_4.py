
from sklearn import tree

def Ballpredictor(weight,surface):
    
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,0],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    Labels= [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Labels)

    ret = (obj.predict([[weight,surface]]))

    if ret == 1:
        print("Your object looks like Tennis Ball")
    else:
        print("Your object looks like Cricket Ball")

def main():
    
    print("----------------Ball predictor case study--------------------")

    print("please enter waight of your objects in grams:")
    weight  = int(input())

    print("please enter type of surface of your object (Rough/smooth):")
    surface =input()

    if surface.lower() == "rough":
        surface = 1

    elif surface.lower()=="smooth":
        surface = 0
        
    else:
        print("Invalid Datatype of surface...")
        exit()

    Ballpredictor(weight,surface)

if __name__ == "__main__":
    main()





