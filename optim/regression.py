'''
    compute matrix
'''

import numpy as np

class OptimalSolution:
    '''
        compute w^*
    '''

    def __init__(self, X_raw, X_add, y, m):

        self.X_raw = X_raw
        self.X_add = X_add
        self.y = y
        self.m = m
        self.X = X_raw
        self.w = None


    def extension_X(self):

        X_mul = self.X_raw
        for dim in range(self.m - 1):
            X_mul = X_mul * self.X_raw
            self.X = np.concatenate((self.X, X_mul), axis=1)
        self.X = np.concatenate((self.X, self.X_add), axis=1)
        self.X = np.matrix(self.X)


    def get_w(self):

        self.w = np.dot(np.dot((np.dot(self.X.T, self.X)).I, self.X.T), self.y)


