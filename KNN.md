# KNN algorithm


* python

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
				
						
train datasets

		X_train = 
		array([[8.92860151, 3.31979805],
       [8.21229123, 0.41696626],
       [1.0765668 , 5.95052064],
       [5.29817362, 4.18807429],
       [3.35407849, 6.22519432],
       [4.38141426, 7.35882106],
       [5.18036412, 5.788586  ],
       [6.45355096, 9.90224271],
       [8.19858197, 4.13200935],
       [8.76267655, 8.23759433]])
			 
			 y_train = array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
			 
			 
Test datasets
		
		xx = np.random.random((10,2))*10 
		xx
			 
			 array([[7.83256671, 6.07996321],
       [0.41748876, 5.61275132],
       [6.68137735, 9.38392607],
       [7.86005859, 7.50430472],
       [4.97050976, 0.42732502],
       [8.16867496, 0.13623744],
       [5.50041186, 5.66796771],
       [1.12918335, 0.6277624 ],
       [5.74724225, 4.85485266],
       [3.01422097, 0.39795558]])
Predict
		 
		 [kNN_classify(6,X_train,y_train,xt) for xt in xx]
		 [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
		 
		 
 
