
from sklearn.datasets import load_iris

iris = load_iris()

print("Features names of iris Datasets:")
print(iris.feature_names)

print("Targest names of iris datasets: ")
print(iris.target_names)

print("First n elements from iris datasets:")
for i in range(len(iris.target)):
    print("ID: %d, Label :%s ,Feature :%s" % (i,iris.data[i],iris.target[i]))
