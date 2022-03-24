'''
    data of temperature
'''

import numpy as np

X_RAW = np.arange(1, 11, 1)
X_RAW = X_RAW.reshape(10,1)
X_ADD = np.ones((10,1))

HIGH_TEMP = np.array([13,17,12,12,11,12,18,17,17,20])
HIGH_TEMP = HIGH_TEMP.reshape(10,1)
LOW_TEMP = np.array([-3,-2,-2,-3,-3,-3,-1,1,2,6])
LOW_TEMP = LOW_TEMP.reshape(10,1)

BAD_HIGH_TEMP = np.array([13,17,12,12,11,12,18,1,17,20])
BAD_HIGH_TEMP = BAD_HIGH_TEMP.reshape(10,1)