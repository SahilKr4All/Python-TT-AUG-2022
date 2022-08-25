Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1,11):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in range(1,11,2):
    print(i)

1
3
5
7
9
for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in range(5):
    print(i)

0
1
2
3
4
#break -statement
for i in range(1,1000):
    if i>5:
        break
    print(i)

1
2
3
4
5
#continue Statement
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

1
2
4
5
7
8
10
11
13
14
16
17
19
20
