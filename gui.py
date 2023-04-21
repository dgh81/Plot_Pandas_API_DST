from api import subjects
from api import get_subject

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
        pg1content = Page_1_Content(p1)
        p1.pack(pady=100, fill='both', expand=True) # Vis side 1:
        self.add_page(p1)

        p2 = Page(self, "page 2")
        pg2content = Page_2_Content(p2)
        self.add_page(p2)

        # Footer:
        style = ttk.Style()
        style.configure('FrameFooter.TFrame', background="yellow")
        footer = Footer(self)

        footer.pack(side=tk.BOTTOM, pady=10, fill='both', expand=True)

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
        self.title = ttk.Label(self, text=title_text, background="pink").pack(expand=True, fill='both')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background="red")
        self.style.configure('Frame1.TFrame', background="blue")
        self.style.configure('Frame2.TFrame', background="orange")
        self.style.configure('Frame3.TFrame', background="green")
        # self.style.configure('FrameFooter.TFrame', background="yellow")

class Footer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.footerFrame = ttk.Frame(self, style='FrameFooter.TFrame')
        btn_back = tk.Button(self.footerFrame, text="Back", font=("Bold", 12), command = parent.move_back_page)
        btn_next = tk.Button(self.footerFrame, text="Next", font=("Bold", 12), command = parent.move_next_page)
        btn_back.pack(side=tk.LEFT, padx=20)
        btn_next.pack(side=tk.RIGHT, padx=20)
        self.footerFrame.pack(expand=True, fill='both')



class Page_1_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Label: Vælg datasæt", background="purple").pack(side=tk.TOP, padx=10, fill='both', expand=True)
        
        # LEVEL 1 FRAME:
        frame_1 = self.create_level_1_frame()
        self.buttons = {}
        for index, sub in enumerate(subjects):
            btn_text = sub['description']          
            sub_button = tk.Button(frame_1, text=btn_text, command=lambda callback=sub, callback2=index: self.level_1_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.buttons[index] = sub_button
        
        # LEVEL 2 AND 3 FRAME:
        self.create_level_2_frame()
        self.create_level_3_frame()

        self.pack(fill='both', expand=True)

    def create_level_1_frame(self):
        frame_1 = ttk.Frame(self, style='Frame1.TFrame')
        frame_1.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        frame_1.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(len(subjects)))
        frame_1.rowconfigure(subjects_tuple, weight=1)
        return frame_1

    def create_level_2_frame(self):        
        self.frame_2 = ttk.Frame(self, style='Frame2.TFrame')
        self.frame_2.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_2.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_2.rowconfigure(subjects_tuple, weight=1)

    def create_level_3_frame(self):
        self.frame_3 = ttk.Frame(self, style='Frame3.TFrame')
        self.frame_3.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_3.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_3.rowconfigure(subjects_tuple, weight=1)

    def clear_level_1_button_colors(self, index):
        # Button color reset and set clicked:
        for i in range(len(self.buttons)):
            print(self.buttons[i]['bg'])
            self.buttons[i].configure(bg='SystemButtonFace')
        self.buttons[index].configure(bg='teal')
    
    def clear_level_2_and_3_buttons(self):
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

    def create_level_2_buttons(self, sub, index):
        subs = get_subject(sub['id'])
        for level_2_subjects in subs:
            for index, level_2_subject in enumerate(level_2_subjects['subjects']):
                btn_text = level_2_subject['description']
                sub_button = tk.Button(self.frame_2, text=btn_text, command=lambda callback=level_2_subject: self.level_2_click(callback))
                sub_button.grid(row=index, column=0, sticky='nsew')

    def level_1_click(self, sub, index):
        self.clear_level_1_button_colors(index)
        self.clear_level_2_and_3_buttons()
        self.create_level_2_buttons(sub,index)

    def clear_level_3_buttons(self):
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
            except:
                pass

    def create_level_3_buttons(self, level_2_sub):
        level_3_subjects = get_subject(level_2_sub['id'])
        print(level_3_subjects)
        if len(level_3_subjects[0]['subjects']) == 0:
            print("empty!","Using level 2 code:",level_3_subjects[0]['id'])
        for index, level_3_subject in enumerate(level_3_subjects[0]['subjects']):
            btn_text = level_3_subject['description']
            sub_button = tk.Button(self.frame_3, text=btn_text, command=lambda callback=level_3_subject: self.temp(callback))
            sub_button.grid(row=index, column=0, sticky='nsew')

    def level_2_click(self, level_2_sub):
        self.clear_level_3_buttons()
        self.create_level_3_buttons(level_2_sub)

    def temp(self, level_3_sub):
        print(level_3_sub['id'])


class Page_2_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="test2", background="orange").pack(side=tk.TOP, padx=10, fill='both', expand=True)
        self.pack()


App(title='Project', geometry=(1200,600))