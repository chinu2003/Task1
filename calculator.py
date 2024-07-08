import tkinter as tk

# Function to update the expression in the entry box
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the entry box
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the result
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("error")
        expression = ""

# Main program starts here
if __name__ == "__main__":
    # Setting up the main window
    window = tk.Tk()
    window.geometry("312x374")  # Adjust height 
    window.resizable(0, 0)
    window.title("Calculator")

    # Global variables
    expression = ""
    input_text = tk.StringVar()

    # Creating the entry box
    input_frame = tk.Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    input_frame.pack(side=tk.TOP)
    
    input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)

    # Creating the buttons
    btns_frame = tk.Frame(window, width=312, height=272.5, bg="black")
    btns_frame.pack()

    # First row
    clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="red", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3)
    divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3)

    # Second row
    seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0)
    eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1)
    nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2)
    multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3)

    # Third row
    four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0)
    five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1)
    six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2)
    subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3)

    # Fourth row
    one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0)
    two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1)
    three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2)
    add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3)

    # Fifth row
    zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
    point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2)
    equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=3)

    
    design_message = tk.Label(window, text="Designed by Chinmay", font=('arial', 12), bg="black", fg="white")
    design_message.pack(side=tk.BOTTOM, fill=tk.X)

    window.mainloop()
