from api import subjects
from api import get_subject
from api import get_table_name
#from api import get_table_metadata
from api import get_table_data
from api import get_table_metadata_fields
from api import get_table_metadata_field_types
from Plot import plot_results

import custom_listbox
import tkinter as t
# from tkinter import ttk

import customtkinter as tk
from tkinter import ttk
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

global_table_name = ''
final_table_id = None
meta_fields = []
global myApp
myApp = None
us = None

listboxes_has_been_created = False

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
        p1 = Page_1(self)
        p1.pack(pady=10, fill='both', expand=True) # Vis side 1:
        self.add_page(p1)
        
        p2 = Page_2(self)
        self.add_page(p2)

        p3 = Page_3(self)
        self.add_page(p3)



        # Footer:
        footer = Footer(self)
        footer.pack(side=tk.BOTTOM, pady=20, padx=20, fill='both')

        # Run app
        self.mainloop()

    def add_page(self, page):
        self.pages.append(page)

    def load_page(self):
        if self.count_pages == 0:
            p1 = Page_1(self)
            self.pages.append(p1)
            p1.pack(pady=10, fill='both', expand=True)
        if self.count_pages == 1:
            p2 = Page_2(self)
            self.pages.append(p2)
            print('self.pages in load_page2:',self.pages)
            p2.pack(pady=10, fill='both', expand=True)
        if self.count_pages == 2:
            p3 = Page_3(self)
            self.pages.append(p3)
            print('self.pages in load_page3:',self.pages)
            p3.pack(pady=10, fill='both', expand=True)
    
    def move_next_page(self):
        if not self.count_pages > len(self.pages) - 2:
            for page in self.pages:
                print("forgetting:",page)
                page.pack_forget()
            self.count_pages += 1
            page = self.pages[self.count_pages]
            self.pages.remove(page)
            self.load_page()

    def move_back_page(self):
        if not self.count_pages == 0:
            for page in self.pages:
                print("forgetting:",page)
                page.pack_forget()
            # count_pages er faktisk mere page_index...
            self.count_pages -= 1
            page = self.pages[self.count_pages]
            # mpage = self.pages[self.count_pages+1]
            self.pages.remove(page)
            # self.pages.remove(mpage)
            self.load_page()

class Footer(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.footerFrame = tk.CTkFrame(self)
        btn_back = tk.CTkButton(self.footerFrame, text="Back", font=("Bold", 12), command = parent.move_back_page)
        btn_next = tk.CTkButton(self.footerFrame, text="Next", font=("Bold", 12), command = parent.move_next_page)
        btn_back.pack(side=tk.LEFT, padx=20)
        btn_next.pack(side=tk.RIGHT, padx=20)
        self.footerFrame.pack(expand=True, fill='both')

class Page_1(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.CTkLabel(self, text="Label: Vælg datasæt").pack(side=tk.TOP, padx=10)
        # self.configure(fg_color='orange')
        # LEVEL 1 FRAME:
        self.create_level_1_frame()
        self.level_1_buttons = {}
        for index, sub in enumerate(subjects):
            btn_text = sub['description']          
            sub_button = tk.CTkButton(self.frame_1, text=btn_text, command=lambda callback=sub, callback2=index: self.level_1_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_1_buttons[index] = sub_button
        
        # LEVEL 2, 3 AND 4 FRAME:
        self.level_2_buttons = {}
        self.create_level_2_frame()
        self.level_3_buttons = {}
        self.create_level_3_frame()
        self.level_4_buttons = {}
        self.create_level_4_frame()


    def create_level_1_frame(self):
        self.frame_1 = tk.CTkFrame(self)
        self.frame_1.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_1.columnconfigure(0, weight=1)
        subjects_tuple = tuple(range(len(subjects)))
        self.frame_1.rowconfigure(subjects_tuple, weight=1)


    def create_level_2_frame(self):        
        self.frame_2 = tk.CTkFrame(self)
        self.frame_2.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_2.columnconfigure(0, weight=1)
        #TODO: Overvej bedre måde end harcoded 20 herunder?
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

    def set_level_1_button_colors(self, index):
        # print(tk.get_appearance_mode())
        # print(tk.ThemeManager._currently_loaded_theme)
        # Button color reset and set clicked:
        for i in range(len(self.level_1_buttons)):
            self.level_1_buttons[i].configure(fg_color='#242424') #3a7ebf
        self.level_1_buttons[index].configure(fg_color='#1f538d') #1f538d
        global global_table_name #TODO: rename til noget a la 'level_1_table_name'
        global_table_name = self.level_1_buttons[index].cget("text")
        print('global_table_name',global_table_name)

    def level_1_click(self, sub, index):
        self.set_level_1_button_colors(index)
        self.clear_level_2_and_3_buttons()
        self.create_level_2_buttons(sub,index)
    
    def set_level_2_button_colors(self, index):
        # Button color reset and set clicked:
        for i in range(len(self.level_2_buttons)):
            self.level_2_buttons[i].configure(fg_color='#242424')
        self.level_2_buttons[index].configure(fg_color='#1f538d')

    #TODO Split i 3 funks og implementér under de forskellige kliks level_1 etc..:
    #(pt cleares lvl 4 ikke ved tryk på level 2)
    def clear_level_2_and_3_buttons(self):
        #TODO: Mangler: Ved tryk på knapper i level 1 og 2, skal kolonne 3 og 4 cleares
        for i in range(len(self.frame_2.grid_slaves())):
            try:
                self.frame_2.grid_slaves()[0].destroy()
                self.level_2_buttons.clear()
            except:
                pass
        for i in range(len(self.frame_3.grid_slaves())):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
            except:
                pass
        for i in range(len(self.frame_4.grid_slaves())):
            try:
                self.frame_4.grid_slaves()[0].destroy()
                self.level_4_buttons.clear()
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

    def create_level_3_buttons(self, level_2_sub):
        level_3_subjects = get_subject(level_2_sub['id'])
        # print(level_3_subjects)
        if len(level_3_subjects[0]['subjects']) == 0:
            print("empty!","Using level 2 code:",level_3_subjects[0]['id']) # TODO: Filtrer tomme fra eller hva?
        for index, level_3_subject in enumerate(level_3_subjects[0]['subjects']):
            btn_text = level_3_subject['description']
            # selected_level_3_ID = level_3_subject['id']
            sub_button = tk.CTkButton(self.frame_3, text=btn_text, command=lambda callback=level_3_subject, callback2=index: self.level_3_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_3_buttons[index] = sub_button

    def set_level_3_button_colors(self, index):
        # Button color reset and set clicked:
        for i in range(len(self.level_3_buttons)):
            self.level_3_buttons[i].configure(fg_color='#242424') # invis:'SystemButtonFace'
        self.level_3_buttons[index].configure(fg_color='#1f538d')
    
    def clear_level_3_buttons(self):
        for i in range(len(self.frame_3.grid_slaves())):
            try:
                self.frame_3.grid_slaves()[0].destroy()
                self.level_3_buttons.clear()
            except:
                pass

    def clear_level_4_buttons(self):
        for i in range(20):
            try:
                self.frame_4.grid_slaves()[0].destroy()
                self.level_4_buttons.clear()
            except:
                pass
    
    def level_3_click(self, level_3_sub, index):

        id = str(level_3_sub['id'])
        global final_table_id
        final_table_id = id

        self.set_level_3_button_colors(index)
        #TODO: Brug global_table_name?
        table_name = get_table_name(id)

        global meta_fields
        meta_fields = get_table_metadata_fields(table_name)
        self.clear_level_4_buttons()
        self.create_level_4_buttons(get_table_metadata_fields(table_name), table_name)
    
    def create_level_4_buttons(self, metadata_fields, table_name): #TODO: ubrugte variable !!
        print('metadata_fields',metadata_fields)
        for index, level_4_subject in enumerate(metadata_fields):
            btn_text = metadata_fields[index]
            sub_button = tk.CTkLabel(self.frame_4, text=btn_text)
            # sub_button = tk.CTkButton(self.frame_4, text=btn_text, command=lambda callback=btn_text, callback2=index, callback3=table_name: self.level_4_click(callback, callback2, callback3))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_4_buttons[index] = sub_button

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")


class Page_2(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        print("Page_2_Content running")

        lbl = tk.CTkLabel(self, text="test2")
        lbl.pack(side=tk.TOP, padx=10, fill='both')

        self.listbox_frames = []

        lbl.configure(text=final_table_id, fg_color="grey")

        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        try:
            table_name = get_table_name(final_table_id)
            listbox_content = []

            for index in range(len(meta_fields)):
                scrollable_checkbox_frame = custom_listbox.ScrollableCheckBoxFrame(master=self, width=2, command=lambda callback=index: self.checkbox_frame_event(callback), item_list=[])
                self.listbox_frames.append(scrollable_checkbox_frame)
                scrollable_checkbox_frame.pack(side='left', fill='both', expand=True)

            for index,listbox_frame in enumerate(self.listbox_frames):
                num_fields = len(get_table_metadata_field_types(table_name, index))
                print(num_fields)

                listbox_content.append(get_table_metadata_field_types(table_name, index))
                for i in range(num_fields):
                    item = listbox_content[index][i]['text']
                    id = listbox_content[index][i]['id']
                    listbox_frame.add_item(item,id)
        
        except:
            pass

    def checkbox_frame_event(self, index):
        print(f"checkbox frame modified: frame: {self.listbox_frames[index]} items:{self.listbox_frames[index].get_checked_items_id()}")
        global us
        us = User_selections(self)
        for i in range(len(self.listbox_frames)):
            us.add_to_list(self.listbox_frames[i].get_checked_items_id())

class User_selections(): # Flyt til bedre sted i koden, evt til egen fil?
    def __init__(self, parent):
        self.parent = parent
        self.sel = []
    
    def add_to_list(self, item):
        self.sel.append(item)
        

class Page_3(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        print("Page_3_Content running")
        #TODO Find bedre løsning end try?
        try: # try er lavet for page 2 og 3, for at undgå fejl under første opstart, hvor variable ikke er blevet sat.
            lbl = tk.CTkLabel(self, text=f"{final_table_id}{us.sel} - metafields: {meta_fields} global_table_name: {global_table_name} final_table_id: {final_table_id}")
            lbl.pack(side=tk.TOP, padx=10, fill='both')
            fieldlist = []
            for field_index,field in enumerate(meta_fields):
                # fieldlist.append(field)
                itemlist = []
                itemdict = {}
                for selected_id in us.sel[field_index]:
                    itemlist.append(str(selected_id))
                    itemdict['code'] = field
                    itemdict['values'] = itemlist
                fieldlist.append(itemdict)
            print('fieldlist:',fieldlist)

            payload['table'] = get_table_name(final_table_id)
            payload['format'] = "CSV"
            payload['variables'] = fieldlist
            print('payload',payload)

            results = get_table_data(payload)

            plot_results(results)
            #TODO BUG: Hvis man trykker baglæns herfra, nulstilles x og y ikke ?! Fix

        except:
            pass
        
global payload
payload = {
   "table": "SKIB74",
   "format": "CSV",
   "variables": [
      {
         "code": "LANDGRP",
         "values": [
            "00"
         ]
      },
      {
         "code": "GODS",
         "values": [
            "100"
         ]
      },
      {
         "code": "Tid",
         "values": [
            "2000K1"
         ]
      }
   ]
}

# global myApp
myApp = App(title='Project', geometry=(1500,800))