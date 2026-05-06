color = "\033[36m"
reset = "\033[0m"

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
        print(f"{color}\n======== Simple Calculator ========{reset}")
        print(f"{color}1. Addition (+){color}")
        print(f"{color}2. Subtraction (-){reset}")
        print(f"{color}3. Multiplication (*){reset}")
        print(f"{color}4. Division (/){reset}")
        print(f"{color}==================================={reset}")

        try:
            choice = input(f"{color}Choose an operation [1/2/3/4]: {reset}")
            numb1 = float(input(f"{color}Enter first number: {reset}"))
            numb2 = float(input(f"{color}Enter second number: {reset}"))

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
                print(f"{color}Invalid Choice.{reset}")
                continue

            print(f"{color}The result is: {result}{reset}")

        except ValueError:
                print(f"{color}Error: Please enter a numeric value.{reset}")
        except ZeroDivisionError as e:
                print(f"{color}Error: {e}{reset}")

        try_again = input(f"{color}Want to try again? (yes/no):{reset}").lower()
        if try_again != 'yes':
            print(f"{color}Thank you!{reset}")
            break

if __name__ == "__main__":
            calculation()




