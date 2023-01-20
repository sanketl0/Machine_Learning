#Assigning feature and label variable

#first Feature

weather = ['sunny','sunny','overcast','Rainy','Rainy','Rainy','Overcast','sunny','sunny','Rainy','sunny','overcast','overcast','Rainy']

#second feature

temp = ['Hot','Hot','Hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','Hot','mild']


#label or targert variables.............

play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

#imporrt label encoder

from sklearn import preprocessing

Ret = preprocessing.LabelEncoder()

#converting string labels into numbers
weather_encoded = Ret.fit_transform(weather)
print(weather_encoded)

temp_encoded = Ret.fit_transform(temp)
print(temp_encoded)

label = Ret.fit_transform(play)
print(label)

#combining weather and temp into single list of tuple

features = list(zip(weather_encoded,temp_encoded))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 3)

#train the model using the training data

model.fit(features,label)

predicted= model.predict([[0,2]])
print(predicted)

if predicted:
    print("You can play")

else:
    print("You can't play")

