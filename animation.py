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
            # 'ffmpeg',
            # '-ss', '00:19:15', # denne slags tider må gerne sættes direkte i sekunder, fx 1,5 min = 90 (ingen : eller noget)
            # # '-display_hflip',
            # '-nostdin',
            # '-i', input_sv.get(),
            # '-crf', '15', # 9 er minimum?
            # '-s', '1080x720', # yt standard?
            # '-an', # no audio...
            # '-t', '00:00:45', # time after -ss to include...
            # '-vf','setpts=16*PTS', # slow mo... 8 = amount
            # 'test.mp4'])
            # f"{output_sv.get()}{file_e}"])

        if results:
            print("Failure")
            # done.set("Working on it...")
        else:
            print("Success!")
            # done.set("Done!")

        
    except:
        print("Failure")

def start_submit_thread():
    print("starting submit thread...")
    global submit_thread
    submit_thread = threading.Thread(target=convert)
    submit_thread.daemon = True #TODO Hvad er daemon?
    # progressbar.start()
    submit_thread.start()
    tk.after(20, check_submit_thread)

def check_submit_thread():
    print("checking submit thread...")
    if submit_thread.is_alive():
        tk.after(20, check_submit_thread)
    else:
        print("done")
        # progressbar.stop()

# start_submit_thread()