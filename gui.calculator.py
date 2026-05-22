import tkinter as tk

def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 + num2

    label_result.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Calculator")

tk.Label(window, text="First Number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Second Number").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Add", command=calculate).pack()

label_result = tk.Label(window, text="Result:")
label_result.pack()

window.mainloop()