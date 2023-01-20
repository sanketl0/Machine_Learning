import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 

def headbrainpredictor():
    data = pd.read_csv('MarvellousHeadBrain.csv')

    print("size of dataset:",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    denomenator = 0

    for i in range(n):
        numerator+= (X[i]-mean_x)*(Y[i]- mean_y)
        denomenator+= (X[i]-mean_x)**2

    m = numerator/denomenator
    c =mean_y -(m * mean_x)

    print("Slpoe of Regression line is ",m)
    print("Y intercept of Regrssion line is",c)

    max_x = np.max(X)-100
    min_x= np.min(X)-100

    x = np.linspace(min_x,max_x,n)

    y = c + m * X

    plt.plot(X,Y,color ='#58b970',label = 'Regrssion Line')
    plt.scatter(X,Y,color ='#ef5423',label ='scatter plot')

    plt.xlabel('Head size in cm3')
    plt.ylabel('Brain weight in gram')

    plt.legend()
    plt.savefig('new.jpg')
    plt.show

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t +=(Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1-(ss_r/ss_t)
    print(r2)

def main():
    print("supervised machine learning:")
    print("Linear Regression on Head and Brain size data set:")

    headbrainpredictor()

if __name__ =="__main__":
    main()


