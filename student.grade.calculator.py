from tkinter import *

def calculate_grade():
    try:
        marks = float(entry.get())

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        result.config(text=f"Grade: {grade}")

    except:
        result.config(text="Enter valid marks!")

root = Tk()
root.title("Student Grade Calculator")
root.geometry("300x200")

Label(root, text="Enter Marks (0-100):").pack(pady=10)

entry = Entry(root)
entry.pack()

Button(root, text="Calculate Grade", command=calculate_grade).pack(pady=10)

result = Label(root, text="")
result.pack()

root.mainloop()