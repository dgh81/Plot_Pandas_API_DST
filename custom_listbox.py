########################## TEST TEST TEST ######################

import customtkinter as tk


class ScrollableCheckBoxFrame(tk.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            # my_item = item.split(",")[0]
            # print('my_item:',my_item)
            self.add_item(item)

    def add_item(self, item):
        #TEST: 
        # TODO: Gør denne del færdig: Id'er skal sættes og der skal laves funktion til at hente dem:
        # TODO: Nedenstående gør at kun id'er tilføjes til knapper:
        # checkbox = myCheckBox(self, text=item.split(",")[0], id="2")
        #TODO test om denne virker:
        checkbox = myCheckBox(self, text=item.split(",")[1], id=item.split(",")[0])
        
        # Old version:
        # checkbox = myCheckBox(self, text=item, id="2")

        if self.command is not None:
            checkbox.configure(command=self.command)
        # checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        checkbox.pack(fill=tk.X, padx=10, pady=10)
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        # return [checkbox.id for checkbox in self.checkbox_list if checkbox.get() == 1]
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

    def get_checked_items_id(self):
        # return [checkbox.id for checkbox in self.checkbox_list if checkbox.get() == 1]
        return [checkbox.id for checkbox in self.checkbox_list if checkbox.get() == 1]

class myCheckBox(tk.CTkCheckBox):
    def __init__(self, parent, id, **kwargs):
        super().__init__(parent, **kwargs)
        self.id = id

########################## TEST TEST TEST ######################