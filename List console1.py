Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
list1 = [1,2,3,4,5,6]
list1.append(1000)
list1
[1, 2, 3, 4, 5, 6, 1000]
list1.insert(2,"mansi")
list1
[1, 2, 'mansi', 3, 4, 5, 6, 1000]
list1.pop()#it will remove the last value
1000
list1
[1, 2, 'mansi', 3, 4, 5, 6]
list1.pop(2)
'mansi'
list1
[1, 2, 3, 4, 5, 6]
list1.remove(2)
list1
[1, 3, 4, 5, 6]
#list comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [-100,20,90,87,10000]
x.sort()
x
[-100, 20, 87, 90, 10000]
x.sort(reverse=True)
x
[10000, 90, 87, 20, -100]
min(x)
-100
max(x)
10000
x = [1,2]
x*2
[1, 2, 1, 2]
x*3
[1, 2, 1, 2, 1, 2]
x = [1,2]
y = [3,4]
x.extend(y)
x
[1, 2, 3, 4]
x
[1, 2, 3, 4]
y
[3, 4]
x+y
[1, 2, 3, 4, 3, 4]
#deep copy vs shallow
x = [1,2,3,4,5]
y = x
x
[1, 2, 3, 4, 5]
y
[1, 2, 3, 4, 5]
x.pop()
5
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]
id(x)
2460194175680
id(y)
2460194175680
x
[1, 2, 3, 4]
y = x.copy()
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]
id(x)
2460194175680
id(y)
2460194181824
x.pop()
4
y
[1, 2, 3, 4]
x
[1, 2, 3]
x = [1,2,3,[4,5,6,7]]
y = x.copy()
id(x)
2460194247360
id(y)
2460163148864
id(x[3])
2460194187328
id(y[3])
2460194187328
#shallow copy
#deep copy
from copy import deepcopy
y = deepcopy(x)
x
[1, 2, 3, [4, 5, 6, 7]]
y
[1, 2, 3, [4, 5, 6, 7]]
id(x)
2460194247360
id(y)
2460194177088
id(x[3])
2460194187328
id(y[3])
2460194181824
x[3].pop()
7
x
[1, 2, 3, [4, 5, 6]]
y
[1, 2, 3, [4, 5, 6, 7]]
