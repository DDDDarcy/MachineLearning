# MachineLearning

This is demo of  kNN algorithm, 


import numpy as np 
from math import sqrt
from collections import Counter

def kNN_classify(k,X_train,y_train,x):
    assert 1<=k <= X_train.shape[0],"K must be valid"
    assert X_train.shape[0] == y_train.shape[0],\
        "    "
    assert X_train.shape[1] == x.shape[0],\
        " 1"
    distances = [sqrt(np.sum((x_t-x)**2)) for x_t in X_train]
    nearest = np.argsort(distances)
    topK_y = [y_train[i] for i in nearest[:k]]
   
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]
