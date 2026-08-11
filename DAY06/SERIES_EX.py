import pandas as pd
s1=pd.Series([10,20,30])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

import pandas as pd
import numpy as np
x=[1,2,3,4,5]
y=pd.Series(x)
print(y)

x=np.array([10,20,30,40,50])
y=pd.Series(x)
print(y)

x={'a':10,'b':20,'c':30,'d':40,'e':50}
y=pd.Series(x)
print(y)

z={'name':'Alice', 'age':25, 'city':'New York'}
y=pd.Series(z)
print(y)

marks=[28,45,78]
x=pd.Series(marks,index=["maths","science","english"])
print(x)
print(x.tolist())

marks = [28, 45, 78]

x = pd.Series(marks, index=["maths", "science", "english"])

print(x["maths"])
print(x["science"])
print(x["english"])
print(x[x>40])

score=pd.Series([10,20])
passed=score[score>10]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

import pandas as pd
names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))