import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        # tearoff=0: "Fjern dashed line at top" ???
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        #or:
        # self.filemenu.add_command(label='Close', command=exit)

        self.menubar.add_separator()
        self.filemenu.add_command(label='Close without question', command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show msg', command=self.show_msg)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='Message', font=('Ariel', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Ariel', 16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        # opret var til at holde 0 eller 1 alt efter checkbox markeret eller ej:
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text='Show msg', font=('Ariel', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show msg', font=('Ariel', 18), command=self.show_msg)

        self.button.pack()

        # clear textbox:
        self.clearbtn = tk.Button(self.root, text='Clear textbox', font=('Ariel', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        # hvad sker der når man trykker på x i vinduet:
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)


        self.root.mainloop()

    def show_msg(self):
        print('Hello World')
        if self.check_state.get() == 0:
            # 1.o tk.END = fra start til slut:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))
            print(self.check_state.get())

    # event har disse properties: <KeyPress event send_event=True state=Mod1 keysym=a keycode=65 char='a' x=474 y=49>
    # brug 'state' for key combos: https://www.youtube.com/watch?v=ibf5cx221hk&ab_channel=NeuralNine 29:45

    def shortcut(self, event):
        print(event)
        if (event.keysym == 'a'):
            print("Du tastede et 'a'")

    def on_closing(self):
        print('Closing window...')
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        pass

MyGUI()