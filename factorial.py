num=int(input("enter the numebr"))
factorial=1
if num<0:
    print("The factorial doesnot exist in negative numbers")
elif num==0:
    print("the factorial is zero")
else:
    n=range(1,num+1)
    for i in n:
        factorial=factorial*i
print("The factorial is :",factorial)
