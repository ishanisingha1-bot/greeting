from tkinter import *
root = Tk()
root.title("Workshop Greeting")
root.geometry("300x180")
def greet():
    name = entry_name.get()
    if name:
        label_message.config(text=f"Hi {name}, welcome to the workshop!")
Label(root, text="Enter your name:").pack(pady=5)
entry_name = Entry(root)
entry_name.pack(pady=5)
Button(root, text="Submit", command=greet).pack(pady=5)
label_message = Label(root, text="", font=("Arial", 10, "bold"))
label_message.pack(pady=10)

root.mainloop()
