import customtkinter as tk
from Api import get_table_data
from Api import get_table_name
from Api import get_subject
from Api import get_table_metadata_fields
from Api import get_table_metadata_field_types
import Custom_listbox
from User_selections import User_selections
from Plot import plot_results
from Animation import start_submit_thread

global_table_name = ''
global_final_table_id = None
global_meta_fields = []

global_user_selections = None

class Page_1(tk.CTkFrame):
    def __init__(self, parent, subjects):
        super().__init__(parent)
        self.subjects = subjects

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
        subjects_tuple = tuple(range(len(self.subjects)))
        self.frame_1.rowconfigure(subjects_tuple, weight=1)


    def create_level_2_frame(self):        
        self.frame_2 = tk.CTkFrame(self)
        self.frame_2.pack(side='left', fill="both", expand=True, padx=10, pady=10)
        self.frame_2.columnconfigure(0, weight=1)
        #TODO: Overvej bedre måde end harcoded 20 herunder?. (Tror det er fint, de bliver jo slettet og sat senere, dette er blot opsætning...)
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
        # Button color reset and set clicked:
        for i in range(len(self.level_1_buttons)):
            self.level_1_buttons[i].configure(fg_color='#242424') #3a7ebf
        self.level_1_buttons[index].configure(fg_color='#1f538d') #1f538d
        global global_table_name #TODO: rename til noget a la 'level_1_table_name'. Tjek hvor den bruges og send som parameter istedet!
        global_table_name = self.level_1_buttons[index].cget("text")
        # print('global_table_name',global_table_name)

    def level_1_click(self, sub, index):
        self.set_level_1_button_colors(index)
        self.clear_selections(self.frame_2, self.level_2_buttons)
        self.clear_selections(self.frame_3, self.level_3_buttons)
        self.clear_selections(self.frame_4, self.level_4_buttons)
        self.create_level_2_buttons(sub,index)
    
    def set_level_2_button_colors(self, index):
        # Button color reset and set clicked:
        for i in range(len(self.level_2_buttons)):
            self.level_2_buttons[i].configure(fg_color='#242424')
        self.level_2_buttons[index].configure(fg_color='#1f538d')

    def create_level_2_buttons(self, sub, index):
        subs = get_subject(sub['id'])
        for level_2_subjects in subs:
            for index, level_2_subject in enumerate(level_2_subjects['subjects']):
                btn_text = level_2_subject['description']
                sub_button = tk.CTkButton(self.frame_2, text=btn_text, command=lambda callback=level_2_subject, callback2=index: self.level_2_click(callback, callback2))
                sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
                self.level_2_buttons[index] = sub_button

    def level_2_click(self, level_2_sub, index):
        self.set_level_2_button_colors(index)
        self.clear_selections(self.frame_3, self.level_3_buttons)
        self.clear_selections(self.frame_4, self.level_4_buttons)
        self.create_level_3_buttons(level_2_sub)

    def create_level_3_buttons(self, level_2_sub):
        level_3_subjects = get_subject(level_2_sub['id'])
        if len(level_3_subjects[0]['subjects']) == 0:
            print("empty!","Using level 2 code:",level_3_subjects[0]['id']) # TODO BUG: Filtrer tomme fra eller hva?
        for index, level_3_subject in enumerate(level_3_subjects[0]['subjects']):
            btn_text = level_3_subject['description']
            sub_button = tk.CTkButton(self.frame_3, text=btn_text, command=lambda callback=level_3_subject, callback2=index: self.level_3_click(callback, callback2))
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_3_buttons[index] = sub_button

    def set_level_3_button_colors(self, index):
        for i in range(len(self.level_3_buttons)):
            self.level_3_buttons[i].configure(fg_color='#242424') # invis:'SystemButtonFace'
        self.level_3_buttons[index].configure(fg_color='#1f538d')
    
    def clear_selections(self, frame, buttons):
        for i in range(len(frame.grid_slaves())):
            try:
                frame.grid_slaves()[0].destroy()
                buttons.clear()
            except:
                pass

    def level_3_click(self, level_3_sub, index):
        id = str(level_3_sub['id'])
        global global_final_table_id
        global_final_table_id = id

        self.set_level_3_button_colors(index)
        
        level_3_table_name = get_table_name(id)

        global global_meta_fields #TODO: Overvej en anden måde end global = User_selections...
        global_meta_fields = get_table_metadata_fields(level_3_table_name)
        self.clear_selections(self.frame_4, self.level_4_buttons)
        self.create_level_4_buttons(level_3_table_name)

    def create_level_4_buttons(self, table_name):
        metadata_fields = get_table_metadata_fields(table_name)
        print('metadata_fields',metadata_fields)
        for index, level_4_subject in enumerate(metadata_fields):
            btn_text = metadata_fields[index]
            sub_button = tk.CTkLabel(self.frame_4, text=btn_text)
            sub_button.grid(row=index, column=0, sticky='nsew', padx=2, pady=2)
            self.level_4_buttons[index] = sub_button

class Page_2(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.listbox_frames = []
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        print("Page_2_Content running")

        lbl = tk.CTkLabel(self, text="test2")
        lbl.pack(side=tk.TOP, padx=10, fill='both')
        lbl.configure(text=global_final_table_id, fg_color="grey")

        try:
            table_name = get_table_name(global_final_table_id)
            # print('table_name:',table_name)
            listbox_content = []

            for index in range(len(global_meta_fields)):
                scrollable_checkbox_frame = Custom_listbox.ScrollableCheckBoxFrame(master=self, width=2, command=lambda callback=index: self.checkbox_frame_event(callback), item_list=[])
                self.listbox_frames.append(scrollable_checkbox_frame)
                scrollable_checkbox_frame.pack(side='left', fill='both', expand=True)

            for index,listbox_frame in enumerate(self.listbox_frames):
                num_meta_fields = len(get_table_metadata_field_types(table_name, index))
                # print(num_meta_fields)

                listbox_content.append(get_table_metadata_field_types(table_name, index))
                for i in range(num_meta_fields):
                    item = listbox_content[index][i]['text']
                    id = listbox_content[index][i]['id']
                    listbox_frame.add_item(item,id)
        
        except:
            pass

    def checkbox_frame_event(self, index):
        print(f"checkbox frame modified: frame: {self.listbox_frames[index]} items:{self.listbox_frames[index].get_checked_items_id()}")
        #TODO : fix det her, global og ny klasse på samme tid var ik meningen... Vi skulle have haft fjernet globals.
        # Lav singleton klasse eller er det endu mere kludret end at bevare globals? https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
        global global_user_selections
        global_user_selections = User_selections(self)
        for i in range(len(self.listbox_frames)):
            global_user_selections.add_to_list(self.listbox_frames[i].get_checked_items_id())

class Page_3(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #TODO Dette skal ikke bruges, sæt ind i try: hvis det en dag skal...:
        # lbl = tk.CTkLabel(self, text=f"{final_table_id}{us.sel} - metafields: {meta_fields} global_table_name: {global_table_name} final_table_id: {final_table_id}")
        # lbl.pack(side=tk.TOP, padx=10, fill='both')
        
        print("Page_3_Content running")
        
        # btn = tk.CTkButton(parent, text="plot me!").pack(side=tk.LEFT, fill='both')
        print('user_selections:', global_user_selections)
        if global_user_selections is not None:
            #Create json based on selections
            payload = self.modify_json_payload()
            print('payload',payload)
            #API Kald
            results = get_table_data(payload)
            print('results:',results)

            #Plot
            plot_results(results)

            self.modify_json_payload()

            video_btn = tk.CTkButton(parent, text="video me!", command=start_submit_thread).pack(side=tk.LEFT, fill='both')
    
    def modify_json_payload(self):
        #TODO Find bedre løsning end try?
        try: # try er lavet for page 2 og 3, for at undgå fejl under første opstart, hvor variable ikke er blevet sat.
            fieldlist = []

            #Byg JSON
            # TODO: Lidt rodet det her + bedre navne?
            #TODO: læs om funktionen DictReader, måske den kan bruges her?
            print('self.meta_fields',global_meta_fields)
            for field_index,field in enumerate(global_meta_fields):
                itemlist = []
                itemdict = {}
                for selected_id in global_user_selections.sel[field_index]:
                    itemlist.append(str(selected_id))
                    itemdict['code'] = field
                    itemdict['values'] = itemlist
                fieldlist.append(itemdict)
            # print('fieldlist:',fieldlist)
            payload = self.payload()
            payload['table'] = get_table_name(global_final_table_id)
            # payload['format'] = "CSV"
            payload['format'] = "BULK"
            payload['variables'] = fieldlist
            print('payload',payload)

            return payload

        except:
            pass

    # payload template
    def payload(self):
        _payload = {
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
        return _payload