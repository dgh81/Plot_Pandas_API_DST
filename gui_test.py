import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Vaskehallen.dk")

# parent = root
label = tk.Label(root, text="Hello World", font=('Ariel',18))
# placering brug, pack, grid eller place:
label.pack(padx=20, pady=20)

# input textbox. Height er i antal linjer:
textbox = tk.Text(root, height=3, font=('Ariel, 16'))
textbox.pack()

# embossed 1 line textfield:
myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

btn = tk.Button(root, text="Click me", font=('Ariel', 18))
btn.pack(padx=10, pady=10)

#LÆS DOKUMENTATION TIL TK

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Ariel', 18))
#sticky = stretch til west og east..:
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Ariel', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Ariel', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text='4', font=('Ariel', 18))
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='5', font=('Ariel', 18))
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='6', font=('Ariel', 18))
btn3.grid(row=1, column=2, sticky=tk.W+tk.E)

# fill = stretch på x aksen:
buttonframe.pack(fill='x')

anotherButton = tk.Button(root, text='TEST')
anotherButton.place(x=500, y=400, height=40, width=80)


root.mainloop()

