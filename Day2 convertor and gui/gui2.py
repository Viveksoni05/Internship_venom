#simply GUI app using tkinter
import tkinter as tk

root = tk.Tk()
root.title("Simply GUI App")
root.geometry("500x400")

welcome = tk.Label(root, text="Welcome to My GUI App!", font=("Arial", 20))
welcome.pack(pady=10)

Name = tk.Label(root, text="Enter your name:", font=("Arial", 12))
Name.pack(pady=10)

entry1 = tk.Entry(root, width=30, font=("Arial", 12), bg="white", fg="black", borderwidth=2)
entry1.pack(pady=10)





def on_click():
    text = entry1.get()
    label.config(text="hello, "+text+"!")


button = tk.Button(root, text="Greet Me",command=on_click, bg="white", fg="red", font=("Arial", 12), borderwidth=2, relief="groove" , width=10 , )
button.pack(pady=10)


button2 = tk.Button(root, text="Reset", command=lambda: [entry1.delete(0, tk.END), label.config(text="")],bg="white", fg="red", font=("Arial", 12), borderwidth=2, relief="groove",width=10)
button2.pack(pady=10)
label = tk.Label(root, text="Hello, Thinker!", font=("Arial", 14), fg="green")
label.pack(pady=10)




root.mainloop()



