list=["jhon","pinky","anu","arun","arjun","anju","ammu"]
count=0
print(list)
a=input("Enter the letter to find the occurance\n")
for n in list:
    for f in n:
        if f==a:
            count=count+1
print("number of ",a,"is:",count)
