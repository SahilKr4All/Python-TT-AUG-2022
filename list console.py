Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list - python's mutable(edit,deletion) data collection
list = [1,2,3,"mansi",234.32423,True,None]
l=[1,2,3,4,5,6]
#indexing
l[0]
1
l[-1]
6
x = [1,2,3,4,[5,6,7,8,[9,10,11,[12,13,[14,15,16,17]]]]]
x[4][4][3][2][1]
15
#slicing
x = [1,2,3,4,5,6,7]
x[::-1]
[7, 6, 5, 4, 3, 2, 1]
x[:5]
[1, 2, 3, 4, 5]
#Functions in List
x = []
x.append(12)
x
[12]
x.append(1)
x
[12, 1]
x.append(3)
x
[12, 1, 3]
x.insert(0,1000)
x
[1000, 12, 1, 3]
x.insert(0,124)
x
[124, 1000, 12, 1, 3]
#Deletion in List
x.pop()#last value
3
x
[124, 1000, 12, 1]
x.pop(0)
124
x
[1000, 12, 1]
x.remove(12)
x
[1000, 1]
del x[0]
