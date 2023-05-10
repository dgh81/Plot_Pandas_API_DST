class User_selections(): # Flyt til bedre sted i koden, evt til egen fil?
    def __init__(self, parent):
        self.parent = parent
        self.sel = []
    
    def add_to_list(self, item):
        self.sel.append(item)