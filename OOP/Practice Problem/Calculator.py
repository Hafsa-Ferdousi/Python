class Calculator:

    def add(self,a,b):
        return a+b

    def subtract(self, a, b):
        return a - b


c=Calculator()
a=int(input("enter the num1: "))
b=int(input("Enter the num2: "))

print("Summation",c.add(a,b))
print("subtraction",c.subtract(a,b))


