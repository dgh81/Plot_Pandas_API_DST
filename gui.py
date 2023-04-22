from api import subjects
from api import get_subject
from api import get_table_name
#from api import get_table_metadata
from api import get_table_data
from api import get_table_metadata_fields
from api import get_table_metadata_field_types
# import tkinter as tk
# from tkinter import ttk

import customtkinter as tk
from tkinter import ttk
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

class App(tk.CTk):
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
        # style.configure('FrameFooter.TFrame', background="yellow")
        style.configure('FrameFooter.TFrame')
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
        self.style.configure('TFrame')
        self.style.configure('Frame1.TFrame')
        self.style.configure('Frame2.TFrame')
        self.style.configure('Frame3.TFrame')
        # self.style.configure('FrameFooter.TFrame', background="yellow")

class Footer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.footerFrame = ttk.Frame(self, style='FrameFooter.TFrame')
        btn_back = tk.CTkButton(self.footerFrame, text="Back", font=("Bold", 12), command = parent.move_back_page)
        btn_next = tk.CTkButton(self.footerFrame, text="Next", font=("Bold", 12), command = parent.move_next_page)
        btn_back.pack(side=tk.LEFT, padx=20)
        btn_next.pack(side=tk.RIGHT, padx=20)
        self.footerFrame.pack(expand=True, fill='both')



class Page_1_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Label: Vælg datasæt", background="purple").pack(side=tk.TOP, padx=10, fill='both', expand=True)
        
        # LEVEL 1 FRAME:
        frame_1 = self.create_level_1_frame()
        self.level_1_buttons = {}
        for index, sub in enumerate(subjects):
            btn_text = sub['description']          
            sub_button = tk.CTkButton(frame_1, text=btn_text, command=lambda callback=sub, callback2=index: self.level_1_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_1_buttons[index] = sub_button
        
        # LEVEL 2 AND 3 FRAME:
        self.level_2_buttons = {}
        self.create_level_2_frame()
        self.level_3_buttons = {}
        self.create_level_3_frame()
        self.level_4_buttons = {}
        self.create_level_4_frame()

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
    
    def create_level_4_frame(self):
        self.frame_4 = ttk.Frame(self, style='Frame3.TFrame')
        self.frame_4.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_4.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_4.rowconfigure(subjects_tuple, weight=1)

    def set_level_1_button_colors(self, index):
        print(tk.get_appearance_mode())
        print(tk.ThemeManager._currently_loaded_theme)
        
        # Button color reset and set clicked:
        # print('original_fg_color',original_fg_color)
        for i in range(len(self.level_1_buttons)):
            # print(self.level_1_buttons[i].cget('fg_color')[0])
            # print(self.level_1_buttons[i].cget('fg_color')[1])
            self.level_1_buttons[i].configure(fg_color='#3a7ebf')
        self.level_1_buttons[index].configure(fg_color='#1f538d')
    
    #TODO Split i to funks:
    def clear_level_2_and_3_buttons(self):
        for i in range(20):
            try:
                self.frame_2.grid_slaves()[0].destroy()
                self.level_2_buttons.clear()
                # self.frame_2.grid_slaves()[0].pack_forget()
            except:
                pass
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
                # self.frame_3.grid_slaves()[0].pack_forget()
            except:
                pass

    def create_level_2_buttons(self, sub, index):
        subs = get_subject(sub['id'])
        for level_2_subjects in subs:
            for index, level_2_subject in enumerate(level_2_subjects['subjects']):
                btn_text = level_2_subject['description']
                sub_button = tk.CTkButton(self.frame_2, text=btn_text, command=lambda callback=level_2_subject, callback2=index: self.level_2_click(callback, callback2))
                sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
                self.level_2_buttons[index] = sub_button


    def level_1_click(self, sub, index):
        self.set_level_1_button_colors(index)
        # self.set_level_3_button_colors(index)
        self.clear_level_2_and_3_buttons()
        self.create_level_2_buttons(sub,index)

    def clear_level_3_buttons(self):
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
                #self.frame_3.grid_slaves()[0].pack_forget()
            except:
                print("fail")
                pass

    def create_level_3_buttons(self, level_2_sub):
        level_3_subjects = get_subject(level_2_sub['id'])
        print(level_3_subjects)
        if len(level_3_subjects[0]['subjects']) == 0:
            print("empty!","Using level 2 code:",level_3_subjects[0]['id'])
        for index, level_3_subject in enumerate(level_3_subjects[0]['subjects']):
            btn_text = level_3_subject['description']
            sub_button = tk.CTkButton(self.frame_3, text=btn_text, command=lambda callback=level_3_subject, callback2=index: self.level_3_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_3_buttons[index] = sub_button
    
    def set_level_2_button_colors(self, index):
        # Button color reset and set clicked:
        print(index)
        # print('fg:', self.level_2_buttons[index].cget('fg_color')[0])
        # x = self.level_2_buttons[index].cget('fg_color')[0]
        for i in range(len(self.level_2_buttons)):
            self.level_2_buttons[i].configure(fg_color='#3a7ebf')
        self.level_2_buttons[index].configure(fg_color='red')

    def level_2_click(self, level_2_sub, index):
        self.set_level_2_button_colors(index)
        self.clear_level_3_buttons()
        self.create_level_3_buttons(level_2_sub)

    def set_level_3_button_colors(self, index):
        # Button color reset and set clicked:
        print(index)
        for i in range(len(self.level_3_buttons)):
            self.level_3_buttons[i].configure(fg_color='#3a7ebf') # invis:'SystemButtonFace'
        self.level_3_buttons[index].configure(fg_color='orange')

    def level_3_click(self, level_3_sub, index):
        id = str(level_3_sub['id'])
        print(id)
        self.set_level_3_button_colors(index)
        table_name = get_table_name(id)
        print("table name:", table_name)
        print('get_table_metadata_fields(table_name)',get_table_metadata_fields(table_name))
        count_field_types = len(get_table_metadata_fields(table_name))
        self.create_level_4_buttons(get_table_metadata_fields(table_name), table_name)
        #TODO: Dette skal være et loop i level_4_click:
        for i in range(count_field_types):
            print('get_table_metadata_field_types(table_name)',get_table_metadata_field_types(table_name, i))
    
    def create_level_4_buttons(self, metadata_fields, table_name):
        print('metadata_fields',metadata_fields)
        for index, level_4_subject in enumerate(metadata_fields):
            
            print('level_4_subject',level_4_subject)
            btn_text = metadata_fields[index]
            sub_button = tk.CTkButton(self.frame_4, text=btn_text, command=lambda callback=btn_text, callback2=index, callback3=table_name: self.level_4_click(callback, callback2, callback3))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_4_buttons[index] = sub_button
        
    def level_4_click(self, btn_text, index, table_name):
        print("text", btn_text, 'index',index)
        #TODO: Viser data, pt for hardcodet tabel.. skal med tiden flyttes til Next-knappen...
        get_table_data(table_name)

# erhverv, industri, industriens salg af varer
#BRANCHE07, OMSTYPE, Tid

class Page_2_Content(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="test2", background="orange").pack(side=tk.TOP, padx=10, fill='both', expand=True)
        self.pack()


App(title='Project', geometry=(1600,800))