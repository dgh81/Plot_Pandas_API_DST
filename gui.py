from api import subjects
import tkinter as tk
from tkinter import ttk

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
        p1.pack(pady=100) # Vis side 1:
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
            page.pack(pady=100)

    def move_back_page(self):
        if not self.count_pages == 0:
            for page in self.pages:
                page.pack_forget()
            self.count_pages -= 1
            page = self.pages[self.count_pages]
            page.pack(pady=100)

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
        ttk.Label(self, text="test1", background="purple").pack(side=tk.LEFT, padx=10)

        fm = ttk.Frame(self)
        fm.pack()
        self.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(len(subjects)))
        self.rowconfigure(subjects_tuple, weight=1)

        for index, sub in enumerate(subjects):
            t = sub['description']          
            sub_button = ttk.Button(fm, text=t, command=lambda callback=sub: select_subject(callback))
            sub_button.grid(row=index, column=0, sticky='nsew')

        self.pack()

class Page_2_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="test2", background="orange").pack(side=tk.LEFT, padx=10)
        self.pack()

def select_subject(sub):
    print(sub)
    print(sub['id'])
    # print(sub["subjects"])



App(title='Project', geometry=(600,600))