import tkinter as tk
from tkinter import messagebox

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

class CalculatorDesign:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="beige")
        accent_color = "dark red"
        fg_color = "white"
        self.title_label = tk.Label(
            root,
            text = "Simple Calculator",
            font = ("Helvetica", 19, "bold"),
            bg = "beige",
            fg = accent_color
        )
        self.title_label.pack(pady=(20, 10))
        tk.Label(root, text="Enter first number:", bg="beige").pack(pady=(10, 0))
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)
        tk.Label(root, text="Enter second number:", bg="beige").pack(pady=(10, 0))
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)
        tk.Label(root, text="Choose operation", bg="beige").pack(pady=(15, 5))
        btn_frame = tk.Frame(root, bg="beige")
        btn_frame.pack()
        tk.Button(btn_frame, text="+", width=6, height=2, bg=accent_color, fg=fg_color, font=("Arial", 10, "bold"), command=lambda: self.perform_calculation('1')).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="-", width=6, height=2, bg=accent_color, fg=fg_color, font=("Arial", 10, "bold"), command=lambda: self.perform_calculation('2')).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="*", width=6, height=2, bg=accent_color, fg=fg_color, font=("Arial", 10, "bold"), command=lambda: self.perform_calculation('3')).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="/", width=6, height=2, bg=accent_color, fg=fg_color, font=("Arial", 10, "bold"), command=lambda: self.perform_calculation('4')).grid(row=1, column=1, padx=5, pady=5)
        self.result_label = tk.Label(root, text="The result is:", bg="beige", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=25)

    def perform_calculation(self, choice):
        try:
            numb1 = float(self.entry1.get())
            numb2 = float(self.entry2.get())
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

            self.result_label.config(text=f"The result is: {result}")

        except ValueError:
            messagebox.showerror("Error" "Please enter a numeric value.")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))

if __name__=="__main__":
    root = tk.Tk()
    app = CalculatorDesign(root)
    root.mainloop()