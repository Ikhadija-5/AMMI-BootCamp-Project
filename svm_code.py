# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EOlV6revKEaKoCQqkSRnsioJ4nhx7cIo
"""

import numpy as np
from sklearn import metrics

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None


    def fit(self, X, y):
        ##
          #fuction for training
        ##
        n_samples, n_features = X.shape
        #insure data in correct form
        y_ = np.where(y <= 0, -1, 1)
        #how to initialize the wights (width=n_features as the input has):
        self.w = np.zeros(n_features)
        #initialize bias
        self.b = 0

        #training loop:
        for iteration in range(self.n_iters):
            #Loop through X (input) i.e. SGD
            for idx, x_i in enumerate(X):
                #update rule:
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (
                        2 * self.lambda_param * self.w - np.dot(x_i, y_[idx])
                    )
                    self.b -= self.lr * y_[idx]
            
            #training accuarcy:
            if(iteration %100==0):
              print(metrics.accuracy_score(y, self.predict(X)))

    def predict(self, X):
        ##
          #fuction for prediction
        ##
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)

# Testing
if __name__ == "__main__":
    # Imports
    from sklearn import datasets
    import matplotlib.pyplot as plt


    clf = SVM(learning_rate=0.001, lambda_param=0.01, n_iters=1000)
    clf.fit(x_train_text2, y_train_text)


    def visualize_svm():
        ##
          #fuction for result visualize
        ##
        def get_hyperplane_value(x, w, b, offset):
            return (-w[0] * x + b + offset) / w[1]

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.scatter(X[:, 0], X[:, 1], marker="o", c=y)

        x0_1 = np.amin(X[:, 0])
        x0_2 = np.amax(X[:, 0])

        x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
        x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

        x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
        x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

        x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
        x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

        ax.plot([x0_1, x0_2], [x1_1, x1_2], "y--")
        ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], "r")
        ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], "k")

        x1_min = np.amin(X[:, 1])
        x1_max = np.amax(X[:, 1])
        ax.set_ylim([x1_min - 3, x1_max + 3])

        plt.show()

    visualize_svm()