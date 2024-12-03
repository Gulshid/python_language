#declaration of function with name ,and parameter
#sum of two value in function
def add(x,y):
    #function body
    sum=x+y
    print("The sum of x a nd y two variable is :",sum)


#call the function
x=int(input("Enter the value for x:"))
y=int(input("Enter the value for y:"))
print(add(x,y))

#print the greetiing and name
def Name(name):
    print("Assalam-u-alikum! My name is ",name)

name=str(input("Enter Your Name:"))
print(Name(name))

#table using function
def table(which_table,that_num):
    i=1
    while(i<=that_num):

        print(which_table,"X",i,"=",which_table*i);
        i=i+1


which_table=int(input("Enter the table that you want:"))
that_num=int(input("Enter the number that you want multiply that table:"))
print(table(which_table,that_num))
