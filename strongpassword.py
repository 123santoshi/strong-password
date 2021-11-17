password=input("enter the password===")
small="abcdefghijklmnopqrstuvwxyz"
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums="0123456789"
spl="!@#$%"
l=[0,0,0,0]
if(len(password)<=6 or len(password)>=15):
    print("password lenght must be greather than 6 and less than 15")
else:
  for i in password:
    if i in small:
      l[0]=1
    elif i in capital:
      l[1]=1
    elif i in nums:
      l[2]=1
    elif i in spl:
      l[3]=1
  if(sum(l)==4):
    print("{0} is correct password".format(password))
  else:
    print("{0} is incorrect password".format(password))
   
    


