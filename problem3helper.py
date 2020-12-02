import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    data = pd.read_csv(datapath)
    X = list(data['Total'])
    X = [i.replace(",", "") for i in X]
    for i in range(0, len(X)):
        X[i] = float(X[i])
    y = list(data['Precipitation'])
    for i in range(len(X)):
        if y[i] == 'T':
            y[i] = 0
    y[3] = 0.47
    for i in range(0, len(y)):
        y[i] = float(y[i])
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    for num in degrees:
        feature = feature_matrix(X, num)
        ls = least_squares(feature, y)
        paramFits.append(ls)
    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X = [[elem ** deg for deg in range(d, -1, -1)] for elem in x]
    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = (np.linalg.inv(X.T @ X) @ X.T @ y).tolist()
    return B


if __name__ == '__main__':
    datapath = "NYC_Bicycle_Counts_2016_Corrected.csv"
    #degrees = [2, 4]

    #paramFits = main(datapath, degrees)
    #print(paramFits)

    degrees = [3, 5, 13]
    paramFits = main(datapath, degrees)
    print(paramFits)

    # Step 3
    file_open = pd.read_csv(datapath)
    y = list(file_open['Precipitation'])
    for i in range(len(y)):
        if y[i] == 'T':
            y[i] = 0
    y[3] = 0.47
    for i in range(0, len(y)):
        y[i] = float(y[i])
    x = list(file_open['Total'])
    x = [i.replace(",", "") for i in x]
    for i in range(0, len(x)):
        x[i] = float(x[i])

    plt.scatter(x, y, c='black', marker='.',label='datapoints')

    x.sort()
    for coeff in paramFits:
        deg_num = len(coeff) - 1
        feat_mtrx = np.array(feature_matrix(x, deg_num))
        y_hat = feat_mtrx @ coeff
        plt.plot(x, y_hat, label= 'd = '+str(deg_num))
    plt.legend(fontsize=10)
    plt.ylabel('Precipitation rate')
    plt.xlabel('Number of Bicyclist')
    plt.title('Number of Bicyclist vs. Precipitation rate')
    plt.show()
