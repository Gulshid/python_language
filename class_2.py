class init:
  def __init__(self):
   self.x=int(input("Enter the value for x:"))
   self.t=float(input("Enter the value for t:"))
   print("The integer value fo x is :",self.x)
   print("The float value of y is :",self.t)
    
init_obj=init()

print(init_obj.__init__())