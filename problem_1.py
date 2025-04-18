class Calculator:
    def __init__(self,a:float,b:float,operation:str):
        self.a = a
        self.b = b
        self.operation = operation
    
    def calculate(self):
        if self.operation == "add":
            return self.a + self.b 
        elif self.operation == "sub":
            return self.a - self.b 
        elif self.operation == "mul":
            return self.a * self.b 
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return f"Error:{self.operation} Invalid Operations"

a = float(input("Enter first number: "))
b = float(input("Enter Second Number: "))
operation = input("Enter the operation to perform(add/sub/mul/div)")

cal = Calculator(a,b,operation)

result = int(cal.calculate())

print("Result",result)
        