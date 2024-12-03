#OOP(Object Oriented Programming)
#class with object class name A
class A:
    #This is the body of class A
    x=10 
    y=20
    c=float(input("Enter the value for c:"))
    d=float(input("Enter the value for d:"))
    a="Hello! This is OOP of python language..."
    b="This is Class A"
    print("The addition of two value is ",x+y)
    print("The multiplication of tow floating value is:",c*d)
#a1 is the object of class A which call    
a1=A()
print(a1.a)