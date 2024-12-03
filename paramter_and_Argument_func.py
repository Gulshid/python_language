#function of parameter          
def Hello(a,b):                                   #parameter is the variable while argument is constant value

    mul=a*b
    print("The multiplication of two value is ",mul)


a=int(input("Enter the value for a :"))
b=int(input("Enter the value for b :"))
print(Hello(a,b))


#function of Argument
def Hello(x,y):
    mul=x*y
    print("The multiplication of two value is ",mul)

print(Hello(3,4))