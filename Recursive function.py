#recursive function
'''
def f1(x):
    #base case
    if x>10:
        return
    print(x)
    f1(x+1)
    print(x)

f1(1)
'''

def f1(a,b):
    #base case
    if b==0:
        return 1
    return a*f1(a,b-1)

print(f1(2,4))
