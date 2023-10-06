num=int(input("enter the number of element in the list:"))
i=0
list=[]
while i<num:
    z=int(input("enter a number"))
    if z>100:
        list.append("over")
    else:
        list.append(z)
    i=i+1
    print(list)
