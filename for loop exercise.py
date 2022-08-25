#find the sum of first 10 natural numbers
'''
result = 0
for i in range(1,11):
    result+=i

print(result)
'''
'''
#find the sum of digits of numbers
x = int(input("Enter a Number :"))
result = 0
for i in range(len(str(x))):
    rem = x%10
    result+=rem
    x = x//10
print(result)
'''
'''
Home work
1. find the reverse of the number (123-321)
2.check whether no is armstrong or not
'''

'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''

'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print(" "*(5-i)+"*"*i)
'''
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''
'''
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
'''
'''
1
12
123
1234
12345
'''
'''
for i in range(1,6):
    for j in range(i):
        print(j+1,end="")
    print()
'''
'''
1
22
333
4444
55555
'''
'''

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
'''
'''
1
23
456
78910
'''
'''
x=1
for i in range(1,6):
    for j in range(i):
        print(x,end="")
        x+=1
    print()

'''

'''

*****
*   *
*   *
*   *
*****

*   *
*   *
*****
*   *
*   *

*   *
**  *
* * *
*  **
*   *
'''
