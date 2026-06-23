from tkinter import *

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Invalid Expression")

root = Tk()
root.title("Simple Calculator")
root.geometry("300x200")

Label(root, text="Enter Expression:").pack(pady=5)

entry = Entry(root, width=25)
entry.pack(pady=5)

Button(root, text="Calculate", command=calculate).pack(pady=5)

output = Label(root, text="Result:")
output.pack(pady=10)

root.mainloop()