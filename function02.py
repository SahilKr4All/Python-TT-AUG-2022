def f1():
    print("I am inside f1")
    def f2():
        print("I am inside f2")
    return f2

f2 = f1()
f2()
