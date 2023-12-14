class Car:
 def __init__(self,color,price,kilo):
  self.color=color
  self.price=price
  self.kilo=kilo
 def show(self):
  print("This is a Car")

  
car1=Car("green",50000,6.8)
car2=Car("black",20000,9.63)
car1.show()

if(car1.price>car2.price):
    print("car1 price is the highest")
else:
    print("car2 price is the greatest")

    
