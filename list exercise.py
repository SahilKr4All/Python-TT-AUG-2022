
x = [12,-100,-1000,34,45,32,98]
largest = x[0]
slargest = x[0]
for i in x:
    if i > largest:
        slargest = largest
        largest = i
    elif i > slargest:
        slargest = i

print(largest)

'''
x = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(x)):
    print(x[i])

for i in x:
    print(i)

x = [1,2,3,4,5,6,7,8,9,10]
choice = int(input("Enter a number :"))

if choice in x:
    print("FOund")
else:
    print("Not FOund")
'''
    
