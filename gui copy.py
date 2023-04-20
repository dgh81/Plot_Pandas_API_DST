import tkinter as tk

class page_content():
    def __init__(self):
        self.entryText = ""

window = tk.Tk()
window.geometry("500x500")
window.title("test")

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)


page_1 = tk.Frame(main_frame)
page_1_label = tk.Label(page_1, text="start page",font=("Bold"))
page_1_entry = tk.Entry(page_1)
page_1_entry.pack() 
page_1_label.pack()
page_1.pack(pady=100)


page_2 = tk.Frame(main_frame)
page_2_label_1 = tk.Label(page_2, text="Page 2",font=("Bold"))
page_2_label_1.pack()
page_2_label_2 = tk.Label(page_2, text="",font=("Bold"))
page_2_label_2.pack()


pages = [page_1, page_2]
count = 0

def move_next_page():
    print(page_1_entry.get())
    global count
    if not count > len(pages) - 2:
        for p in pages:
            p.pack_forget()
        count += 1
        page = pages[count]
        # update label:
        page_2_label_2.config(text=page_1_entry.get())
        page.pack(pady=100)


def move_back_page():
    global count
    if not count == 0:
        for p in pages:
            p.pack_forget()
        count -= 1
        page = pages[count]
        page.pack(pady=100)

bottom_frame = tk.Frame(window, bg='blue')

back_btn = tk.Button(bottom_frame, text="Backbutton", font=("Bold", 12), command = move_back_page).pack(side=tk.LEFT, padx=10)
next_btn = tk.Button(bottom_frame, text="Nextbutton", font=("Bold", 12), command = move_next_page).pack(side=tk.RIGHT, padx=10)

bottom_frame.pack(side=tk.BOTTOM, pady=10)

window.mainloop()