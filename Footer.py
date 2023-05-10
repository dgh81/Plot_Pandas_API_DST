import customtkinter as tk

class Footer(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.footerFrame = tk.CTkFrame(self)
        self.btn_back = tk.CTkButton(self.footerFrame, text="Back", font=("Bold", 12), command = parent.move_back_page)
        self.btn_next = tk.CTkButton(self.footerFrame, text="Next", font=("Bold", 12), command = parent.move_next_page)
        self.btn_back.pack(side=tk.LEFT, padx=20)
        self.btn_next.pack(side=tk.RIGHT, padx=20)
        self.footerFrame.pack(expand=True, fill='both')