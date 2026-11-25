import pandas as pd

x=pd.Series([34,34,56,78,99],
            index=["a",'b','c','d',"e"],name="Data")

'''
print(x)
print()
print(x.values)
print()
print(x.index)
print()
print(x.dtype)
print()
print(x.shape)
print()
print(x.size)
print()
print(x.count())
print()
print(x.ndim)
print()
print(x.name)
print()
print(x.is_unique)
print()
print(x.empty)
print()
print(x.hasnans)
print()
print(x.nbytes)
print()
print(x.head(2), "Head")
print()
print(x.tail(2), "Tail")
print()
print(x.sample())
print(x.unique())
print(x.nunique())
print(x.value_counts())'''

'''
y=pd.Series([100,50,25,15,100])
print(y.is_monotonic_increasing)

print(y.sort_values(ascending=True))
'''
print(x.astype(float))
print(x.astype(bool))
print(x.astype(complex))
print(x.astype(str))
print()
print(x.min())
print()
print(x.sum())
print()
print(x.mean())
print()
print(x.mode())
print()
print(x.median())
print()
"""
1) Values
2)Index
3)dtype
4)shape (Return type of shape property is tuple)
5)Size
6)ndim
7)name
8)empty
9)is_unique
10)hasnans
11)nbytes
12)head() syn-variablename.head() By default it will print first 5 rows or v_n.head(Number of rows) ([Top to Bottom])
13) tail() syn-variablename.tail() By default it will print last 5 rows or v_n.tail(Number of rows) ([Bottom to Top])
14) sample()
15)unique()
16)nunique()
17)value_counts()
18)Is_monotonic_increasing
19)Is_monotonic_decreasing
20)sort_values()
21) astype()
22) max()
23) min()
24) Sum()
25)
"""