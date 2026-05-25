import tkinter as tk

file_name = "students.txt"

def save_record():
    name = entry_name.get()
    marks = entry_marks.get()

    with open(file_name, "a") as f:
        f.write(f"{name} - {marks}\n")

    status.config(text="Record Saved!")

def view_records():
    try:
        with open(file_name, "r") as f:
            data = f.read()

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, data)

    except FileNotFoundError:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "No records found")

window = tk.Tk()
window.title("Student Record Manager")

tk.Label(window, text="Student Name").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Marks").pack()
entry_marks = tk.Entry(window)
entry_marks.pack()

tk.Button(window, text="Save Record", command=save_record).pack()
tk.Button(window, text="View Records", command=view_records).pack()

status = tk.Label(window, text="")
status.pack()

text_box = tk.Text(window, height=10, width=30)
text_box.pack()

window.mainloop()