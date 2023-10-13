n=input("enter a scentence with repeated letters:")
k="$"
res=n[0]+n[1:].replace(n[0],k)
print(res)
