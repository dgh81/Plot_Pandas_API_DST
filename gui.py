from api import subjects
from api import get_subject
from api import get_table_name
#from api import get_table_metadata
from api import get_table_data
from api import get_table_metadata_fields
from api import get_table_metadata_field_types

import custom_listbox
# import tkinter as tk
# from tkinter import ttk

import customtkinter as tk
from tkinter import ttk
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

global_table_name = ''
final_table_id = None
meta_fields = []
# global_selected_level_2_ID = ''

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
        p1.pack(pady=10, fill='both', expand=True) # Vis side 1:
        self.add_page(p1)

        p2 = Page(self, "page 2")
        # pg2content = Page_2_Content(p2)
        self.add_page(p2)

        # Footer:
        footer = Footer(self)

        footer.pack(side=tk.BOTTOM, pady=20, padx=20, fill='both')

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
            page.pack(pady=10, fill='both', expand=True)
            print('meta_fields',meta_fields)
            # OBS ! init her betyder at page 2 reloades når man gør frem og tilbage?!
            p2 = Page_2_Content(page)
            # p2.__init__(self)

    def move_back_page(self):
        if not self.count_pages == 0:
            for page in self.pages:
                page.pack_forget()
            self.count_pages -= 1
            page = self.pages[self.count_pages]
            page.pack(pady=10, fill='both', expand=True)

class Page(tk.CTkFrame):
    def __init__(self, parent, title_text):
        super().__init__(parent)
        self.pageHeader = "test"
        self.title = tk.CTkLabel(self, text=title_text).pack(fill='both')
        self.configure(fg_color='teal')

class Footer(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.footerFrame = tk.CTkFrame(self)
        btn_back = tk.CTkButton(self.footerFrame, text="Back", font=("Bold", 12), command = parent.move_back_page)
        btn_next = tk.CTkButton(self.footerFrame, text="Next", font=("Bold", 12), command = parent.move_next_page)
        btn_back.pack(side=tk.LEFT, padx=20)
        btn_next.pack(side=tk.RIGHT, padx=20)
        self.footerFrame.pack(expand=True, fill='both')



class Page_1_Content(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.CTkLabel(parent, text="Label: Vælg datasæt").pack(side=tk.TOP, padx=10)
        self.configure(fg_color='orange')
        # LEVEL 1 FRAME:
        self.create_level_1_frame()
        self.level_1_buttons = {}
        for index, sub in enumerate(subjects):
            btn_text = sub['description']          
            sub_button = tk.CTkButton(self.frame_1, text=btn_text, command=lambda callback=sub, callback2=index: self.level_1_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_1_buttons[index] = sub_button
        
        # LEVEL 2 AND 3 FRAME:
        self.level_2_buttons = {}
        self.create_level_2_frame()
        self.level_3_buttons = {}
        self.create_level_3_frame()
        self.level_4_buttons = {}
        self.create_level_4_frame()
        #TODO: Skal fjernes når page 2 er klar:
        self.create_level_5_frame()

        self.pack(fill='both', expand=True)

    def create_level_1_frame(self):
        self.frame_1 = tk.CTkFrame(self)
        self.frame_1.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_1.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(len(subjects)))
        self.frame_1.rowconfigure(subjects_tuple, weight=1)
        #return frame_1

    def create_level_2_frame(self):        
        self.frame_2 = tk.CTkFrame(self)
        self.frame_2.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_2.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_2.rowconfigure(subjects_tuple, weight=1)

    def create_level_3_frame(self):
        self.frame_3 = tk.CTkFrame(self)
        self.frame_3.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_3.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_3.rowconfigure(subjects_tuple, weight=1)
    
    def create_level_4_frame(self):
        self.frame_4 = tk.CTkFrame(self)
        self.frame_4.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_4.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_4.rowconfigure(subjects_tuple, weight=1)

    def create_level_5_frame(self):
        self.frame_5 = tk.CTkFrame(self)
        self.frame_5.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_5.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(20))
        self.frame_5.rowconfigure(subjects_tuple, weight=1)

    def set_level_1_button_colors(self, index):
        print(tk.get_appearance_mode())
        print(tk.ThemeManager._currently_loaded_theme)
        
        # Button color reset and set clicked:
        for i in range(len(self.level_1_buttons)):
            self.level_1_buttons[i].configure(fg_color='#242424') #3a7ebf
        self.level_1_buttons[index].configure(fg_color='#1f538d') #1f538d
        global global_table_name
        global_table_name = self.level_1_buttons[index].cget("text")
        print('global_table_name',global_table_name)

    def clear_level_3_buttons(self):
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
            except:
                print("fail")
                pass

    def level_1_click(self, sub, index):
        self.set_level_1_button_colors(index)
        self.clear_level_2_and_3_buttons()
        self.create_level_2_buttons(sub,index)


    
    def set_level_2_button_colors(self, index):
        # Button color reset and set clicked:
        for i in range(len(self.level_2_buttons)):
            self.level_2_buttons[i].configure(fg_color='#242424')
        self.level_2_buttons[index].configure(fg_color='#1f538d')

    #TODO Split i to funks:
    def clear_level_2_and_3_buttons(self):
        for i in range(20):
            try:
                self.frame_2.grid_slaves()[0].destroy()
                self.level_2_buttons.clear()
            except:
                pass
        for i in range(20):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
            except:
                pass

    def create_level_2_buttons(self, sub, index):
        subs = get_subject(sub['id'])
        for level_2_subjects in subs:
            for index, level_2_subject in enumerate(level_2_subjects['subjects']):
                btn_text = level_2_subject['description']
                selected_level_2_ID = level_2_subject['id']
                sub_button = tk.CTkButton(self.frame_2, text=btn_text, command=lambda callback=level_2_subject, callback2=index, callback3=selected_level_2_ID: self.level_2_click(callback, callback2, callback3))
                sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
                self.level_2_buttons[index] = sub_button

    def level_2_click(self, level_2_sub, index, selected_level_2_ID):
        self.set_level_2_button_colors(index)
        self.clear_level_3_buttons()
        self.create_level_3_buttons(level_2_sub)
        # print('selected_level_2_ID',selected_level_2_ID)

    def create_level_3_buttons(self, level_2_sub):
        level_3_subjects = get_subject(level_2_sub['id'])
        # print(level_3_subjects)
        if len(level_3_subjects[0]['subjects']) == 0:
            print("empty!","Using level 2 code:",level_3_subjects[0]['id'])
        for index, level_3_subject in enumerate(level_3_subjects[0]['subjects']):
            btn_text = level_3_subject['description']
            selected_level_3_ID = level_3_subject['id']
            sub_button = tk.CTkButton(self.frame_3, text=btn_text, command=lambda callback=level_3_subject, callback2=index, callback3=selected_level_3_ID: self.level_3_click(callback, callback2, callback3))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_3_buttons[index] = sub_button

    def set_level_3_button_colors(self, index):
        # Button color reset and set clicked:
        # print(index)
        for i in range(len(self.level_3_buttons)):
            self.level_3_buttons[i].configure(fg_color='#242424') # invis:'SystemButtonFace'
        self.level_3_buttons[index].configure(fg_color='#1f538d')

    #TODO: Behøver ikke selected_level_3_ID, selected_level_2_ID, bare det sidste valgte table's id...
    def level_3_click(self, level_3_sub, index, selected_level_3_ID):
        
        id = str(level_3_sub['id'])
        # print(id)
        global final_table_id
        final_table_id = id

        self.set_level_3_button_colors(index)
        #TODO: Brug global_table_name?
        table_name = get_table_name(id)
        # print("table name:", table_name)
        # print('get_table_metadata_fields(table_name)',get_table_metadata_fields(table_name))
        global meta_fields
        meta_fields = get_table_metadata_fields(table_name)
        count_field_types = len(get_table_metadata_fields(table_name))
        self.create_level_4_buttons(get_table_metadata_fields(table_name), table_name)
        #TODO: Dette skal være et loop i level_4_click:
        for i in range(count_field_types):
            print('get_table_metadata_field_types(table_name)',get_table_metadata_field_types(table_name, i))
        print('final_table_id',final_table_id)
    
    def create_level_4_buttons(self, metadata_fields, table_name):
        print('metadata_fields',metadata_fields)
        for index, level_4_subject in enumerate(metadata_fields):
            # print('level_4_subject',level_4_subject)
            btn_text = metadata_fields[index]
            sub_button = tk.CTkButton(self.frame_4, text=btn_text, command=lambda callback=btn_text, callback2=index, callback3=table_name: self.level_4_click(callback, callback2, callback3))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_4_buttons[index] = sub_button
        
    def level_4_click(self, btn_text, index, table_name):
        # print("text", btn_text, 'index',index)
        btns = get_table_metadata_field_types(table_name, index)
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        try:
            self.scrollable_checkbox_frame.pack_forget()
        except:
            pass
        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = custom_listbox.ScrollableCheckBoxFrame(master=self.frame_5, width=200, command=self.checkbox_frame_event,
                                                                item_list=[f"{btn['text']}" for btn in btns])
        self.scrollable_checkbox_frame.pack(fill='both', expand=True) #.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")


class Page_2_Content(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # lbl = tk.CTkLabel(self, text="test2")
        # lbl.pack(side=tk.TOP, padx=10, fill='both')
        
        # btn = tk.CTkButton(self, text="test", command=lambda callback=lbl: self.clickme(callback))
        # btn.pack()

        self.frames = []
        # self.create_level_1_frame()
        # self.create_level_2_frame()
        # self.create_level_3_frame()

        # for i, btn in enumerate(btns):
        #     print(btn)
            # list = ttk.OptionMenu(self.frame_5, text=btn_text).pack()
            # sub_button = tk.CTkButton(self.frame_5, text=btn['text'], command=lambda callback=btn_text, callback2=index, callback3=table_name: self.level_5_click(callback, callback2, callback3))
            # sub_button.grid(row=i, column=0, sticky='nsew', padx=2, pady=2)
        
        
        #TODO page_2_content burde have en self.page_list hvor pages dynamisk oprettet...
        # I stedet for at kalde på create_level_1_frame, etc...
        # meta_fields herunder indeholder antallet af loops...

        btns = meta_fields # get_table_metadata_field_types(final_table_id, 1)
        print('meta_fields',meta_fields)
        
        self.create_frames(btns)

        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        try:
            self.scrollable_checkbox_frame2.pack_forget()
        except:
            pass
        # create scrollable checkbox frame
        # self.scrollable_checkbox_frame2 = custom_listbox.ScrollableCheckBoxFrame(master=self.frame_1, width=200, command=self.checkbox_frame_event,
        #                                                         item_list=[f"test{btn}" for btn in btns])
        # self.scrollable_checkbox_frame2.pack(fill='both', expand=True)

        self.listboxes = []
        #TODO: Der skal laves et slags loop hvor scrollCheckBoxes tilføjes tilf self.listboxes
        #Når der altid kaldes på self.scrollable_checkbox_frame2, virker kun den sidste overskrevne liste
        for index,fr in enumerate(self.frames):
            scrollable_checkbox_frame = custom_listbox.ScrollableCheckBoxFrame(master=fr, width=2, command=lambda callback=index: self.checkbox_frame_event(callback),
                                                                item_list=[f"temp{index}" for btn in btns])
            self.listboxes.append(scrollable_checkbox_frame)
            scrollable_checkbox_frame.pack(side='left', fill='both', expand=True)

        self.pack(fill='both', expand=True)

    def checkbox_frame_event(self, index):
        print(f"checkbox frame modified: {self.listboxes[index].get_checked_items()}")

    def create_frames(self, btns):
        print('btns',btns)
        for index, btn in enumerate(btns):
            print(index, btn)
            fr = tk.CTkFrame(self)
            self.frames.append(fr)
            fr.pack(side='left', fill="both", expand=True, padx=10, pady=10)
            fr.columnconfigure(0, weight=1)
            subjects_tuple = tuple(range(20))
            fr.rowconfigure(subjects_tuple, weight=1)
            lbl = tk.CTkLabel(fr, text=f"{btn}")
            lbl.pack(side=tk.TOP, padx=2, fill='both')

    def clickme(self, lbl):
        print("clickme")
        lbl.configure(text=final_table_id, fg_color="grey")
        print(final_table_id)
        

App(title='Project', geometry=(1500,800))