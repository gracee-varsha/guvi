a = int(input("enter the value of a:" ))
b = int(input("enter the value of b:"))
c= a+b
print(c)
i=1
while(i>0):
  d= input("do you want to continue:")
  if(d=='yes'):
       a = int(input("enter the value of a:" ))
       b = int(input("enter the value of b:"))    
       c= a+b
       print(c)
  else:
    i=0
    print("exit")
