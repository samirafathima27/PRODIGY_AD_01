import tkinter as tk

# Function to update the expression in the entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main GUI code
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("500x700")

    expression = ""
    equation = tk.StringVar()

    entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons
    button1 = tk.Button(root, text='9', padx=20, pady=20, font=('Arial', 20), command=lambda: press(9))
    button1.grid(row=1, column=0)

    button2 = tk.Button(root, text='8', padx=20, pady=20, font=('Arial', 20), command=lambda: press(8))
    button2.grid(row=1, column=1)

    button3 = tk.Button(root, text='7', padx=20, pady=20, font=('Arial', 20), command=lambda: press(7))
    button3.grid(row=1, column=2)

    button4 = tk.Button(root, text='6', padx=20, pady=20, font=('Arial', 20), command=lambda: press(6))
    button4.grid(row=2, column=0)

    button5 = tk.Button(root, text='5', padx=20, pady=20, font=('Arial', 20), command=lambda: press(5))
    button5.grid(row=2, column=1)

    button6 = tk.Button(root, text='4', padx=20, pady=20, font=('Arial', 20), command=lambda: press(4))
    button6.grid(row=2, column=2)

    button7 = tk.Button(root, text='3', padx=20, pady=20, font=('Arial', 20), command=lambda: press(3))
    button7.grid(row=3, column=0)

    button8 = tk.Button(root, text='2', padx=20, pady=20, font=('Arial', 20), command=lambda: press(2))
    button8.grid(row=3, column=1)

    button9 = tk.Button(root, text='1', padx=20, pady=20, font=('Arial', 20), command=lambda: press(1))
    button9.grid(row=3, column=2)

    button0 = tk.Button(root, text='0', padx=20, pady=20, font=('Arial', 20), command=lambda: press(0))
    button0.grid(row=4, column=0)

    plus = tk.Button(root, text='+', padx=20, pady=20, font=('Arial', 18), command=lambda: press('+'))
    plus.grid(row=1, column=3)

    minus = tk.Button(root, text='-', padx=20, pady=20, font=('Arial', 18), command=lambda: press('-'))
    minus.grid(row=2, column=3)

    multiply = tk.Button(root, text='*', padx=20, pady=20, font=('Arial', 18), command=lambda: press('*'))
    multiply.grid(row=3, column=3)

    divide = tk.Button(root, text='/', padx=20, pady=20, font=('Arial', 18), command=lambda: press('/'))
    divide.grid(row=4, column=3)

    equal = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 18), command=equalpress)
    equal.grid(row=4, column=2)

    clear = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
    clear.grid(row=4, column=1)

    root.mainloop()
