class Car:
    def __init__(self,made,color,model,year):
        self.made=made
        self.color=color
        self.model=model
        self.year=year

car =Car("hodna","red","civic",2020)
print(car)

print(car.color)
print(car.year)
print(car.model)
print(car.made)
