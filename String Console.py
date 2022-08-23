Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string
x = 'a'
x = 'hello'
x = "hello"
x = "Hello Welcome to "Python" Class"
SyntaxError: invalid syntax
x = 'Hello Welcome to "Python" Class'
x
'Hello Welcome to "Python" Class'
x = "Hello Welcome to \"Python\" Class"
x
'Hello Welcome to "Python" Class'
x  = '''On the Insert tab, the galleries include items that are designed to coordinate with the overall look of your document. You can use these galleries to insert tables, headers, footers, lists, cover pages, and other document building blocks. When you create pictures, charts, or diagrams, they also coordinate with your current document look.
You can easily change the formatting of selected text in the document text by choosing a look for the selected text from the Quick Styles gallery on the Home tab. You can also format text directly by using the other controls on the Home tab. Most controls offer a choice of using the look from the current theme or using a format that you specify directly.
To change the overall look of your document, choose new Theme elements on the Page Layout tab. To change the looks available in the Quick Style gallery, use the Change Current Quick Style Set command. Both the Themes gallery and the Quick Styles gallery provide reset commands so that you can always restore the look of your document to the original contained in your current template.'''
#''' ''' - multi line String
#indexing
x = "Python"
x[0]
'P'
x[3]
'h'
x[5]
'n'
x[-1]
'n'
x[-2]
'o'
x[-3]
'h'
#Slicing
x = "Hello Welcome to Python Class"
x[0:5]
'Hello'
x[0:5:1]
'Hello'
x[0:5:2]
'Hlo'
x
'Hello Welcome to Python Class'
x[:10]
'Hello Welc'
x[0:]
'Hello Welcome to Python Class'
x[:]
'Hello Welcome to Python Class'
x[::-1]
'ssalC nohtyP ot emocleW olleH'
#String's Built-in Functions
x
'Hello Welcome to Python Class'
x.lower()
'hello welcome to python class'
x.upper()
'HELLO WELCOME TO PYTHON CLASS'
x.capitalize()
'Hello welcome to python class'
x.title()
'Hello Welcome To Python Class'
#String - immutable -which cannot be changed
x
'Hello Welcome to Python Class'
x = x.title()
x
'Hello Welcome To Python Class'
x.swapcase()
'hELLO wELCOME tO pYTHON cLASS'
x
'Hello Welcome To Python Class'
x.find('o')
4
x.rfind(;o;)
SyntaxError: invalid syntax
x.rfind("o")
21
x.find('o',5)
10
x.find('o',11)
15
x[15]
'o'
x.index('o',11)
15
x.find("X")
-1
#-1 - means value not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'Hello Welcome To Python Class'
x.count('o')
4
x.count('s')
2
x
'Hello Welcome To Python Class'
x.replace("Python","C++")
'Hello Welcome To C++ Class'
x
'Hello Welcome To Python Class'
x
'Hello Welcome To Python Class'
x.split()
['Hello', 'Welcome', 'To', 'Python', 'Class']
x.split()[0]
'Hello'
x.split()[-1]
'Class'
x = "Python"
len(x)
6
x.center(4)
'Python'
x.center(7)
' Python'
x.center(8)
' Python '
x.center(21)
'        Python       '
x.center(21,"/")
'////////Python///////'
x = x.center(21,"/")
x.lstrip("/")
'Python///////'
x.rstrip('/')
'////////Python'
strip
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    strip
NameError: name 'strip' is not defined
x.strip('/')
'Python'
x
'////////Python///////'
len(x)
21
x.zfill(30)
'000000000////////Python///////'
x
'////////Python///////'
x.isalpha()
False
x.isalnum()
False
x = "234fsdfsdf"
x.isalnum()
True
