import threading
import sys
import os
import subprocess
import customtkinter as tk
# root = tk.Tk()

def convert():
    # s = f"ffmpeg -sseof -00:00:30 -display_hflip -nostdin -i original.mp4 -crf 30 -s 720x360 {output_sv.get()}{file_e} 2>C:\myffmpeg\log.txt"
    print("calling convert...")
    try:
        #TODO Opret dynamisk sti til input parameter herunder... Husk også at lave 001, 002 til images...
        # save_img_path = f"{os.path.join(os.getcwd())}\\img\\img{index}.png"
        results = subprocess.call([
            'ffmpeg',
            '-framerate', '2',
            '-pattern_type', 'sequence',
            '-i', f'{os.path.join(os.getcwd())}\\img\\img%3d.png',
            '-s:v', '1920x1080',
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            f'{os.path.join(os.getcwd())}\\img\\out1.mp4'])


        if results:
            print("Failure")
        else:
            print("Success!")
        
    except:
        print("Failure")

def start_submit_thread():
    print("starting submit thread...")
    global submit_thread
    submit_thread = threading.Thread(target=convert)
    submit_thread.daemon = True #TODO Hvad er daemon?
    submit_thread.start()
    tk.after(20, check_submit_thread)

def check_submit_thread():
    print("checking submit thread...")
    if submit_thread.is_alive():
        tk.after(20, check_submit_thread)
    else:
        print("done")
