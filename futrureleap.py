currentyear=int(input("Enter the current year:"))
finalyear=int(input("enter the final year:"))
year=currentyear
for year in range(currentyear,finalyear+1,1):
    if(year%4==0 and year%100!=0)or(year%100==0 and year%400==0):
        
        print("the leap years is",year)
else:
    print("itis not a leap year",year)
