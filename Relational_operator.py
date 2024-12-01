#All Relational Operator(>,<,>=,<=,==,!=)
print("Enter the value for a and b to operate all the Relational operator")
a=float(input("Enter the value for a:"))
b=float(input("Enter the value for a:"))
#operator (>)
if (a>b):{
        print("The value of ",a," is greater than ",b)
}
#operator (<)
elif (a<b):{
    print("The value of ",a," is less than ",b)
}
#operator (>=)
elif(a>=b):{
    print("The value of ",a," is greater or equaL to ",b)
}
#operator (<=)
elif(a<=b):{
    print("The value of ",a," is less or equal to ",b)
}
#operator (==)
elif(a==b):{
    print("The value of ",a," is equal to  ",b)
}
#operator (!=)
elif(a!=b):{
    print("The value of ",a," is not equal to ",b)
}

else: {
    print("Neither any operation are perform...")
}
   

