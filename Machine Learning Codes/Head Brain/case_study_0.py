import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def HeadBrainPredictor():
    data = pd.read_csv("MarvellousHeadBrain.csv")

    print("size of data set ",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    ret = LinearRegression

    ret = ret.fit(X,Y)

    Y_pred = ret.predict(X)

    r2 = ret.score(X,Y)

    print(r2)

def main():

    print("Supervised machine learning")
    print("linear regression on head brain size data set")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()
