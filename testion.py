'''WHAT IS PYTHON
Python is a highlevel language, general purpose and very popular programming language. Pyhton programming language latest version 3 and it is used in web development, machine learning applications, along with all cutting edge tech in the software industry like:
Google, Amazon, Facebook, Instagram, Dropbox, Uber...etc

The biggest strength of Python is a huge collection of standard libraries that can be used for the following purposes:
*Machine learning
*GUI Application (like Kivy, Tkinter, PyQt etc)
*Web frameworks like Django(used by youtube and instagram)
*Image Processing (like OpenCV, Pillow)
*Web Scraping(like Scapy, BeautifulSoup, Selenium)
*Test Frameworks
*Multimedia
*Scientific Computing
*Text Processing and much more...
'''

'''PYTHON COMMENTS and Rules for all programming:
Rule 1: Coments should not duplicate code.
Rule 2: Good comments to excuse unclear code.
Rule 3: If you cant write a clear comment there should be a problem with the code. 
Rule 4: Comment should disples confusion not cause it
Rule 5: Explain unidiomatic code in comments
Rule 6: Provide links to the original source of copied code
Rule 7:Include links to external references where they will be helpful
Rule 8: Add comments when fixing bugs
Rule 9: Use comments to mark incomplete implementations

'''
#The following will processed
"""fdsgfdsgfdsgfsgfds"""
'''PYTHON COMMENTS'''

print('Khadeem Bernard is best')

"""VARIABLES: Variables do not need to be declared with any particular type and can even change type after they have been set. Just start with a initial value or not"""
bane = True
bat = 5
bar = ""
bell = 52.5
"""VARIABLE Names: A variable can have a short name like x or y but a more descriptive name like age, carname, or total_volume. Rules for Python variables:
***A variable name must start with a letter or the underscore character
***A variable cannot start with a number
***A variable name can only contain alpha numeric characters A-Z a-z 0-9 _
***A variable name is case sensitive to age and Age are two different variables
***A variable name cannot be any of the python key words VARIABLE, CREATION, DEF, MULTI, print etc...

MULTI VARIABLE CREATION
"""
f_name,l_name,age = "Khadeem", "Benard", 21
initial_value =start = i = 0
print(age)
print(initial_value)

''''CASTING VARIABLES: If you want to specifdt the data type of a vairbale this can be done with casting

PYTHON DATATYPES: Python has the following data types built-in by default in these categories:

Text Type: str-String
Numeric Types: int-integer, float, complex
Sequence Types: list, tuple,range
Mapping Types: dict
Set Types: set, frozenset
Boolean Types: bool
None Type: NoneType
'''
a,b,c = 221,-5,15
if a<b:
    print("That is correct")
    b=500
print("All done")
x = 3
y = str(x)
z="A Thing"
finding = z.find('Thing')
print(finding)
print(x * 5)
print(x,y,z)
print("My age was once " + str(x))

'''Python Indentation:
Indentation refers to the spaces at the beginning of code line.

Where in other programming languages the indentation in code is for readability only the indetation in Python is very important.

Python uses indentation to indicate a block of code'''

'''PYTHON STRING MANIPULATION:
String Slicing: returns a piece of a string that is dictated by inputs
Ex.'''
test = "This is a test string in Python"
print(test[0])
print(test[15:35])

'''String Methods to Use:'''
print(test.upper())
print(test.lower())
print(test.strip().upper())

'''Concatenate a string'''
print(test + "hello")

name = 'take 5'
amount = 5
cost = 10
statements = "I had my favorite candy {0}, I bought a total of {1} for ${2} dollars"
print(statements.format(name,amount,cost))

print("")

'''BOOLEANS AND CODING:
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
SOOOOO  (), [], {}, "", the number 0, and the value None and of course False = False'''
print(bool(455))
print(bool(0))
print(bool("HELLO CLARISE"))
print(bool(""))
kennyIsAlive = False


'''Python Operators:
Operators are used to perform operations on variables and values
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators


Python Arithmetic Operators
Operator	Name	        Example	
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	        Multiplication	x * y	
/	        Division	    x / y	
%	        Modulus	        x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y

Python Assignment Operators:
Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3


Operator	Description	Try it
()	        Parentheses	
**	        Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	    Addition and subtraction	
<<  >>	    Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
not	        Logical NOT	
and	        AND	
or	        OR
'''


# Object Oriented Operations
#Class Definition: a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
class Person:
    # __init__ is a python CONTRUCTOR for classes that is used to INITIALIZE attributes of a boject as soon as the object is formed
    #self is a default parameter/argument that represents the INSTANTIATED object of the class
    # Definition of INSTANTIATE: the creation of an object (or an “instance” of a given class) in an object-oriented programming (OOP) language
    def __init__(self,first,middle, last,age):
        self.first = first
        self.middle = middle
        self.last = last
        self.age = age
    #The string method of the class that is used of the object is ever used in a print statement or situation
    def __str__(self):
        return  self.first + " " + self.middle + " " + self.last + " " + str(self.age)
    
    def initials(self):
        return self.first[0] +  self.middle[0] +  self.last[0]
    
    def ChangeAge(self,amount):
        self.age += amount

aPerson = Person('Bender','Bending','Rodriguez',4 )
print(aPerson)
aPerson.ChangeAge(2)
print(aPerson)
print(aPerson.initials())

class Shape:
    def __init__(self,xcor,ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)
    
    def move(self, x1,y1):
        self.x += x1
        self.y += y1
#Definition Inheritance:the procedure in which one class inherits the attributes and methods of another class. The class whose properties and methods are inherited is known as the parent class or superclass. And the class that inherits the properties from the parent class is the child class or derived class
class Rectangle(Shape):
    def __init__(self, xcor,ycor,width,height):
        #Use the Parent class constructor to set the x and y coordinates for all rectangle object
        Shape.__init__(self,xcor,ycor)
        self.width = width
        self.height = height 

    def __str__(self):
        retStr = Shape.__str__(self)
        retStr += ' width: ' + str(self.width) + ' height: ' + str(self.height)
        return retStr

rec = Rectangle(5,10,8,9)
print(rec)
rec.move(10,12)
print(rec) 


# Modules
import tempConvert
# OR
import ftoc from temp

temp = 102
newTemp = tempConvert.ftoc(temp)
print('The converted temp of ' + str(temp) +" : " + str(newTemp))
