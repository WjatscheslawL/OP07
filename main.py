import tkinter as tk

def my_name():
    uname = entry.get()
    label.config(text=f"Привет  {uname} !!!")

root = tk.Tk()
root.title("Как тебя зовут?")
label = tk.Label(root, text="Напиши пожалуйста свое имя.")
entry = tk.Entry(root)
label.pack()
entry.pack()
button = tk.Button(root, text="Ввел?", command=my_name)
button.pack()

root.mainloop()