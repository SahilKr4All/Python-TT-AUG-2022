def Calc(x,y,choice):
    return eval(x+choice+y)

x = input("enter no1:")
y = input("enter no2:")
choice = input("Enter operation :")
if choice in ("+","-","*","/"):
    Calc(x,y,choice)
else:
    print("Invalid Choice")

print(Calc(x,y,choice))
