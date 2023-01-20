# import required library
from sklearn import tree


#load the given dataset
#Rough= 1
#smooth = 0

#cricket =2
#Tennis = 1

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,0],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

Labels= [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]


#Decide machine learning algorithms
obj = tree.DecisionTreeClassifier()

#perform training of model
obj = obj.fit(Features,Labels)


#perform the testing
print(obj.predict([[97,0],[35,1]]))









