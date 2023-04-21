from api import subjects
from api import get_subject

import tkinter as tk
from tkinter import ttk
import functools

test = False

class App(tk.Tk):
    def __init__(self, title, geometry):
        # App setup
        super().__init__()
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.minsize(geometry[0], geometry[1])
        
        self.count_pages = 0
        
        # Pages setup:
        self.pages = []
        p1 = Page(self, "page 1")
        Page_1_Content(p1)
        p1.pack(pady=100, fill='both', expand=True) # Vis side 1:
        self.add_page(p1)

        p2 = Page(self, "page 2")
        Page_2_Content(p2)
        self.add_page(p2)

        # Footer:
        footer = Footer(self)
        footer.pack(side=tk.BOTTOM, pady=10)

        # Run app
        self.mainloop()

    def add_page(self, page):
        self.pages.append(page)
    
    def move_next_page(self):
        if not self.count_pages > len(self.pages) - 2:
            for page in self.pages:
                page.pack_forget()
            self.count_pages += 1
            page = self.pages[self.count_pages]
            page.pack(pady=100, fill='both', expand=True)

    def move_back_page(self):
        if not self.count_pages == 0:
            for page in self.pages:
                page.pack_forget()
            self.count_pages -= 1
            page = self.pages[self.count_pages]
            page.pack(pady=100, fill='both', expand=True)

class Page(ttk.Frame):
    def __init__(self, parent, title_text):
        super().__init__(parent)
        self.pageHeader = "test"
        #Title
        self.title = ttk.Label(self, text=title_text, background="white").pack(expand=True, fill='both')

class Footer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Button(self, text="Back", font=("Bold", 12), command = parent.move_back_page).pack(side=tk.LEFT, padx=10)
        tk.Button(self, text="Next", font=("Bold", 12), command = parent.move_next_page).pack(side=tk.RIGHT, padx=10)

class Page_1_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="page 1", background="purple").pack(side=tk.TOP, padx=10, fill='both', expand=True)

        # Styles
        style = ttk.Style()
        style.configure('TFrame', background="red")
        style.configure('Frame1.TFrame', background="blue")
        style.configure('Frame2.TFrame', background="orange")
        style.configure('Frame3.TFrame', background="green")

        # LEVEL 1:
        self.frame_1 = ttk.Frame(self, style='Frame1.TFrame')
        self.frame_1.pack(side='left', fill="both", expand=True)
        self.frame_1.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(len(subjects)))
        self.frame_1.rowconfigure(subjects_tuple, weight=1)

        # LEVEL 2:
        self.frame_2 = ttk.Frame(self, style='Frame2.TFrame')
        self.frame_2.pack(side='left', fill="both", expand=True)
        self.frame_2.columnconfigure(0, weight=1)
        # subjects_tuple = tuple(range(len(subjects)))
        subjects_tuple = tuple(range(20))
        self.frame_2.rowconfigure(subjects_tuple, weight=1)

        # LEVEL 3:
        self.frame_3 = ttk.Frame(self, style='Frame3.TFrame')
        self.frame_3.pack(side='left', fill="both", expand=True)
        self.frame_3.columnconfigure(0, weight=1)
        # subjects_tuple = tuple(range(len(subjects)))
        subjects_tuple = tuple(range(20))
        self.frame_3.rowconfigure(subjects_tuple, weight=1)

        self.buttons = {}

        for index, sub in enumerate(subjects):
            t = sub['description']          
            sub_button = tk.Button(self.frame_1, text=t, command=lambda callback=sub, callback2=index: self.populate_level_2_subjects(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.buttons[index] = sub_button

        
        
        self.pack(fill='both', expand=True)

    def populate_level_2_subjects(self, sub, index):
        # Button color reset and set clicked:
        for i in range(len(self.buttons)):
            print(self.buttons[i]['bg'])
            self.buttons[i].configure(bg='SystemButtonFace')
        self.buttons[index].configure(bg='teal')

        for i in range(20):
            try:
                self.frame_2.grid_slaves()[0].destroy()
            except:
                pass
        
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
            except:
                pass


        # print(sub['description'])
        # print(sub['id'])
        subs = get_subject(sub['id'])
        # print(subs)
        for level_2_subjects in subs:
            # print('i:', level_2_subjects)
            for index, level_2_subject in enumerate(level_2_subjects['subjects']):
                # print("x:", level_2_subject['id'])
                # t = level_2_subject['id']
                t = level_2_subject['description']
                # print(t)
                sub_button = tk.Button(self.frame_2, text=t, command=lambda callback=level_2_subject: self.populate_level_3_subjects(callback))
                sub_button.grid(row=index, column=0, sticky='nsew')
        test = True

    def populate_level_3_subjects(self, level_2_sub):
        
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
            except:
                pass


        # print("test", level_2_sub)
        subs = get_subject(level_2_sub['id'])
        # print(subs)

        for level_3_subjects in subs:
            # print('i:', level_3_subjects)
            for index, level_3_subject in enumerate(level_3_subjects['subjects']):
                # print("x:", level_3_subject['id'])
                # t = level_3_subject['id']
                t = level_3_subject['description']
                # print(t)
                sub_button = tk.Button(self.frame_3, text=t, command=lambda callback=level_3_subject: self.temp(callback))
                sub_button.grid(row=index, column=0, sticky='nsew')

    def temp(self, level_3_sub):
        print(level_3_sub['id'])

class Page_2_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="test2", background="orange").pack(side=tk.LEFT, padx=10)
        self.pack()





App(title='Project', geometry=(1200,600))