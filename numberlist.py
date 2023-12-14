start=int(input("enter the first number of your list:"))
last=int(input("enterthe last number of your list:"))
num=start
for num in range(start,last+1,1):
    print("your list is :",num)
for num in range(start,last+1,1):
       if(num>0):
           print("the list of positive number is",num)


