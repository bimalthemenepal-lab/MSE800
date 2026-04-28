# Basic Calculator 
def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def display_results(calc):                        #takes a Calculator object as an argument and displays the results of the calculations
    print(f"\n\n--- Results ---")
    print(f"Addition:       {calc.add()}")
    print(f"Subtraction:    {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    print(f"Division:       {calc.divide()}")

def run_again():
    choice = input("\nDo you want to calculate again? (yes/no): ")
    return choice.lower() == "yes"

class Calculator:          #defining a class called Calculator
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Cannot divide by zero"
        return self.a / self.b

print("basic calculator")

while True:
    a, b = get_numbers()         
    calc = Calculator(a, b)      
    display_results(calc)        

    if not run_again():          
        print("Goodbye!")
        break
    