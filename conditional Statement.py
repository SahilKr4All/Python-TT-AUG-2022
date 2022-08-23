'''
x = int(input("Enter No 1:"))
y = int(input("Enter No 2:"))
z = int(input("Enter No 3:"))

if x>y and x>z:
    print(f"{x} is largest")
elif  y>z:
    print(f"{y} is largest")
else:
    print(f"{z} is largest")
'''

x = int(input("Enter Side 1:"))
y = int(input("Enter Side 2:"))
z = int(input("Enter Side 3:"))
if x+y>z and x+z>y and z+y>x:
    if x==y and y==z:
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Traingle")
    
