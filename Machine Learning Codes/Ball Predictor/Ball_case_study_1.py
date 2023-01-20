# import required library
from sklearn import tree


#load the given dataset
Features = [[35,"Rough"],[47,"Rough"],[90,"smooth"],[48,"Rough"],[90,"smooth"],[35,"smooth"],[92,"smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"smooth"],[43,"Rough"],[110,"smooth"],[35,"Rough"],[95,"smooth"]]

Labels= ["tennis","Tennis","cricket","Tennis","cricket","tennis","cricket","Tennis","Tennis","Tennis","cricket","Tennis","cricket","Tennis","cricket"]


#Decide machine learning algorithms
obj = tree.DecisionTreeClassifier()

#perform training of model
obj = obj.fit(Features,Labels)


#perform the testing
print(obj.predict([[97,"smooth"]]))









