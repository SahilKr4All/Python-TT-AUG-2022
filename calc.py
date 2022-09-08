def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x = float(input("enter no1:"))
y = float(input("enter no2:"))
choice = input("Enter operation :")
d = {"+":add,"-":sub,"*":mul,"/":div}
res= d.get(choice)(x,y)
print(res)
