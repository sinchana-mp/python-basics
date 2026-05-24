import tkinter as tk

def convert():
    celsius = float(entry.get())

    fahrenheit = (celsius * 9/5) + 32

    result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")

window = tk.Tk()
window.title("Temperature Converter")

tk.Label(window, text="Enter Celsius").pack()

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Convert", command=convert).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()