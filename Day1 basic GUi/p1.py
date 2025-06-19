#simply GUI app using tkinter
import tkinter as tk

root = tk.Tk()
root.title("Simply GUI App")
root.geometry("300x200")
root.config(bg="light blue")
label = tk.Label(root, text="Hello, Thinker!", font=("Arial", 14), bg="light blue", fg="black")
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12), bg="white", fg="black", borderwidth=2, relief="groove")
entry.pack(pady=10)

def on_click():
    text = entry.get()
    label.config(text="hello, "+text)


button = tk.Button(root, text="click me",command=on_click, bg="light green", fg="black", font=("Arial", 12))
button.pack(pady=10)
button2 = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", font=("Arial", 12))
button2.pack(pady=10)




root.mainloop()



