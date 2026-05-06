class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        pass

class Addition(Operation):
    def calculate(self):
        return self.num1 + self.num2

class Subtraction(Operation):
    def calculate(self):
        return self.num1 - self.num2

class Multiplication(Operation):
    def calculate(self):
        return self.num1 * self.num2

class Division(Operation):
    def calculate(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.num1 / self.num2

def calculation():
    while True:
        print("\n======== Simple Calculator ========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        try:
            choice = input("Choose an operation [1/2/3/4]: ")
            numb1 = float(input("Enter first number: "))
            numb2 = float(input("Enter second number: "))

            result = 0
            if choice == '1':
                op = Addition(numb1, numb2)
                result = op.calculate()
            elif choice == '2':
                op = Subtraction(numb1, numb2)
                result = op.calculate()
            elif choice == '3':
                op = Multiplication(numb1, numb2)
                result = op.calculate()
            elif choice == '4':
                op = Division(numb1, numb2)
                result = op.calculate()
            else:
                print("Invalid Choice.")
                continue

            print(f"The result is: {result}")

        except ValueError:
                print("Error: Please enter a numeric value.")
        except ZeroDivisionError as e:
                print("Error: {e}")

        try_again = input("Want to try again? (yes/no):").lower()
        if try_again != 'yes':
            print("Thank you!")
            break

if __name__ == "__main__":
            calculation()




