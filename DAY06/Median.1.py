import numpy as np
marks=np.array([[2,3,4],[5,6,7],[9,0,1]])
print(marks)
print(np.median(marks))
row=np.median(marks,axis=1)
print(row)
col=np.median(marks,axis=0)
print(col)