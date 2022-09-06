Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets - python's unordered data collection
#sets - set cannot contain duplicate values
x = {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5}
x
{1, 2, 3, 4, 5}
x.add(100)
x
{1, 2, 3, 4, 5, 100}
x.remove(100)
x = {1,2,3,4}
y = {3,4,5,6}
x.union(y)#all but without repetition
{1, 2, 3, 4, 5, 6}
x.intersection(y)
{3, 4}
x.difference(y)
{1, 2}
y - x
{5, 6}
y.difference(x)
{5, 6}
x
{1, 2, 3, 4}
y
{3, 4, 5, 6}
x.update(y)
x
{1, 2, 3, 4, 5, 6}
x.intersection_update(y)
x
{3, 4, 5, 6}
x.difference_update(y)
x
set()
