str="python"
print("the original string is :",str)
reverse_string=""
count=len(str)
while(count>0):
    reverse_string=reverse_string+str[count-1]
    count=count-1
print("the reverse string is:",reverse_string)
