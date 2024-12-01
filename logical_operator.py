#Logical Operator(not,and ,or)
print("Enter the value for x and y to perform all logical operator:")
x=float(input("Enter the value for x:"))
y=float(input("Enter the value for y:"))
if(x>y and x==y):
    {
        print("The value of  ",x," is greater and equal to ",y)
    }
elif (x<y and x==y):
    {
        print("the value of ",x," is less and equal to ",y)
    }
elif (x<y or x==y):
   {
      print("the value of ",x," is less or equal to ",y)
   }
elif (x>y or x==y):
    {
        print("the value of ",x," is greater or equal to ",y)
    }
elif (x!=y ):
    {
        print("the value of ",x," is not  equal to ",y)
    }   
elif (x==y):
    {
        print("the value of ",x," is  equal to ",y)
    }
    


