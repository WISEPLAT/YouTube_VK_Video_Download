# pip install yt_dlp tkinter requests webbrowser threading requests

import threading
import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
import yt_dlp
import requests
from datetime import datetime

currentVersion = '1.5+'
class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)
        self.setup_widgets()

    def setup_widgets(self):
        self.widgets_frame = ttk.Frame(self, padding=(0, 10, 0, 0))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(25, 0), sticky="nsew"
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)
        self.label = ttk.Label(
            self.widgets_frame,
            text="Insert the link(s) to the video separated by commas",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=0, column=0,padx=0, pady=25, sticky="n")

        self.entry_nm = ttk.Entry(self.widgets_frame, font=("Calibri 22"))
        self.entry_nm.insert(tk.END, str(''))
        self.entry_nm.grid(row=1, column=0, columnspan=10, padx=(5, 5), ipadx=150, ipady=5, pady=(0, 0), sticky="ew")
        self.entry_nm.bind('<Return>', self.on_enter_pressed)

        self.bt_frame = ttk.Frame(self, padding=(0, 0, 0, 0))
        self.bt_frame.grid(row=1, column=0, padx=(10, 10), pady=0, columnspan=10, sticky="n")

        self.accentbutton = ttk.Button(
            self.bt_frame, text="Download video", style="Accent.TButton",command=self.get_directory_string
        )
        self.accentbutton.grid(row=0, column=0,columnspan=3, ipadx=30, padx=2, pady=(5, 0), sticky="n")

        self.bt_frame.columnconfigure(index=0, weight=1)
        self.status_label = ttk.Label(
            self.bt_frame,
            text=" ",
            justify="center",
            font=("-size", 10, "-weight", "normal"),
        )
        self.status_label.grid(row=1, column=0,padx=0, pady=15, sticky="n") 

        self.copy_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.copy_frame.grid(row=8, column=0, padx=(10, 10), pady=5, columnspan=10 , sticky="s")
        self.UrlButton = ttk.Button(
            self.copy_frame, text="About", style="Url.TButton",command=self.openweb
        )
        self.UrlButton.grid(row=1, column=0, padx=20, pady=0, columnspan=2, sticky="n")
        self.UrlButton = ttk.Button(
            self.copy_frame, text="Vers.: " +currentVersion+" ", style="Url.TButton",command=self.checkUpdate
        ) 
        self.UrlButton.grid(row=1, column=4, padx=20, pady=0, columnspan=2, sticky="w")
        self.UrlButton = ttk.Button(
            self.copy_frame, text="Donate", style="Url.TButton",command=self.donate
        )
        self.UrlButton.grid(row=1, column=7, padx=20, pady=0, columnspan=2, sticky="w")

    def openweb(self):
        webbrowser.open_new_tab('https://github.com/WISEPLAT/YouTube_VK_Video_Download')

    def donate(self):
        return # webbrowser.open_new_tab('https://ko-fi.com/monseg')

    def checkUpdate(self, method='Button'):
        try:
            github_page = requests.get('https://raw.githubusercontent.com/WISEPLAT/YouTube_VK_Video_Download/main/README.md')
            github_page_html = str(github_page.content).split()
            for i in range(0,8):
                try:
                    index = github_page_html.index(('1.' + str(i)))
                    version = github_page_html[index]
                except ValueError:
                    pass

            if float(version) > float(currentVersion):
                self.updateApp(version)
            else:
                if method == 'Button':
                    messagebox.showinfo(title='No updates found', message=f'No updates found.\nCurrent version: {version}')
        except requests.exceptions.ConnectionError:
            if method == 'Button':
                messagebox.showwarning(title='No network access', message='No network access.\nCheck your internet connection.')
            elif method == 'ConnectionError':
                pass
        except Exception as e:
                print(f"An error occurred: {e}")

    def updateApp(self, version):
        update = messagebox.askyesno(title='An update has been found', message=f'A new version is available {version} . Update?')
        if update:
            webbrowser.open_new_tab('https://github.com/WISEPLAT/YouTube_VK_Video_Download')

    def get_directory_string(self):
        if self.entry_nm.get() == '':
            self.status_label.configure(text="You have not entered a link to the video")
            pass
        else:
            video_urls = self.entry_nm.get().split(',')
            for video_url in video_urls:
                video_url = video_url.strip()
                if video_url:
                    try:
                        t = threading.Thread(target=self.download_video, args=(video_url,))
                        t.start()
                    except:
                        self.status_label.configure(text="Error")
            self.entry_nm.delete(0, tk.END)

    def download_video(self, video_url):
        try:
            #ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s', 'quiet': True, 'progress_hooks': [self.my_hook]}

            # Текущая дата и время, преобразование в строку
            dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
            ydl_opts = {'outtmpl': f'downloads/{dt}_%(title)s.mp4', 'quiet': True, 'progress_hooks': [self.my_hook]}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                info = ydl.extract_info(video_url, download=True)
                self.status_label.configure(text=f"Video has been downloaded successfully: «{info['title']}»")
        except:
            self.status_label.configure(text="Error")

    def my_hook(self, d):
       if d['status'] == 'downloading':
           percent_str_clear = d['_percent_str'].replace('[0;94m', '')
           percent_str = percent_str_clear
           percent_str = ''.join(chr for chr in percent_str if chr.isprintable())
           percent = percent_str.split('%')[0].strip()
           root.after(0, lambda: self.status_label.configure(text=f"Downloading... {percent}% ", font=("Arial", 10)))
       elif d['status'] == 'finished':
           root.after(0, lambda: self.status_label.configure(text="Download completed!", font=("Arial", 10)))


    def on_enter_pressed(self, event):
        self.get_directory_string()


if __name__ == "__main__":
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w//2 
    h = h//2 
    w = w - 200
    h = h - 200
    root.geometry('680x350+{}+{}'.format(w, h))
    root.resizable(False, False)
    root.title("Download video from YouTube or VK (in Threads => may be Bans)")
    root.iconbitmap('theme/icon.ico')
    root.tk.call("source", "theme/vk_theme.tcl")
    root.tk.call("set_theme", "light")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.update()
    root.mainloop()
