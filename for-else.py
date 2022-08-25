x = int(input("Enter No:"))
for i in range(2,x):
    if x%i==0:
        print("Not a Prime No")
        break
else:
    print("Prime")
