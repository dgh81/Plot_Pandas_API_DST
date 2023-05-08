import customtkinter as tk

class ScrollableCheckBoxFrame(tk.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list): #TODO: Behøver ikke enumerate?
            self.add_item(item)

    def add_item(self, item_text, item_id):
        #TODO Opret 2 input parametre i stedet for at splitte i funktionen!
        checkbox = myCheckBox(self, text=item_text, id=item_id)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.pack(fill=tk.X, padx=10, pady=10)
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

    def get_checked_items_id(self):
        #TODO Kan vi bruge flere generatorer som denne rundt om i koden?
        return [checkbox.id for checkbox in self.checkbox_list if checkbox.get() == 1]

class myCheckBox(tk.CTkCheckBox):
    def __init__(self, parent, id, **kwargs):
        super().__init__(parent, **kwargs)
        self.id = id