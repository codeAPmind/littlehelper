# from pynput import keyboard, mouse
from threading import Thread
import tkinter as tk
from tkinter import messagebox

import os,time,datetime,dataclasses,webbrowser
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

from Message import showMsgGapFisrt
import simpleaudio as sa
from Settingpanel import SetDialog
from name import datfile,name,path
from keygen import query,permit,trial,key,sample,load,dump1,nt,dc,values
import setting

from AutoTest.AutoTest import Test

import os
import glob

DEBUG =  False



class RestReminderWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.keys = ''
        self.reminderTimes = 0
        self.isWork = False
        self.login_window = None
        self.work_id = None
        self.rest_id = None
        self.load_settings('settings.json')
        self.verify()
        self.initUI()
    
    def starttimer(self):
        self.flash()
        self.root.after(1000*5, self.starttimer) 
        
    def flash(self):
        self.state('zoomed') 
        # ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )#ctypes.windll.kernel32.GetConsoleWindow()
        
    def verify(self):
        self.license=path(datfile())
        self.IsFreetrial = not self.license
        self.query=query(self.license) if self.license else query(permit()) if os.path.exists(permit()) else trial(permit(),key(sample()))
        self.key=self.query[0][0]
        self.result=self.query[0][-1]
        self.endTimeStr = self.query[0][1]
        for k,v in zip(self.key._fields,self.key):setattr(self,k,v)
        self.ver=f'{self.version}'
        self.endTimeStr2=datetime.datetime.strptime(self.endTimeStr,'%a %b %d %H:%M:%S %Y').strftime("%Y-%m-%d %H:%M:%S")
        # self.title(f"{name()} {self.version} {self.edition} {int((self.time-time.time())/86400)} days. © {time.strftime('%Y')} 图正的小店")
        self.title(f"Unity小帮帮")

    def load_settings(self,f):
        self.settingsfile=path(f)
        d=load(self.settingsfile) if self.settingsfile else dump1(setting.s(),f)
        self.settingsfile=self.settingsfile or f
        self.settings=dc(d)
        self.settings0=nt(d)
    

    def show_set_window(self):
        self.login_window = SetDialog(self)
        self.login_window.grab_set()
    
    def updateUI(self,isUpdateAlpha,isUpdatebg,isUpdateSize):
        if isUpdateAlpha:
            self.attributes('-alpha', self.settings.alpha)  
        
        if isUpdatebg:
            self.configure(bg=self.settings.bg_color)  
        
        if isUpdateSize:
            self.timeUpdate.config(font=(self.settings.text_font, int(self.settings.text_size)))
            self.update_button.config(font=(self.settings.text_font, int(self.settings.text_size)))
        
        
    def initUI(self):
        self.geometry("420x230")
        self.attributes('-alpha', self.settings.alpha) 
        self.configure(bg=self.settings.bg_color)  

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="设置", command=self.show_set_window)
        # context_menu.add_command(label="购买", command=lambda:webbrowser.open("https://item.taobao.com/item.htm?id=753192371704"))
        self.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # self.timeUpdate = tk.Text(self, width=20, height=2) 

        # self.timeUpdate.grid(row=1, column=0,sticky='nsew',pady=(10, 0)) 
        # self.timeUpdate.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.update_button = tk.Button(self, text="Restart Unity", command=self.Restart)
        self.update_button.grid(row=0, column=0,sticky='nsew',pady=(10, 0)) 
        self.update_button.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.kil_button = tk.Button(self, text="Kill Unity", command=self.kill_unity)
        self.kil_button.grid(row=1, column=0,sticky='nsew',pady=(10, 0)) 
        self.kil_button.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.open_client_log = tk.Button(self, text="APP log", command=self.open_applog)
        self.open_client_log.grid(row=2, column=0,sticky='nsew',pady=(10, 0)) 
        self.open_client_log.config(font=(self.settings.text_font, int(self.settings.text_size)))


        self.open_sdk_log = tk.Button(self, text="Sdk log", command=self.open_sdklog)
        self.open_sdk_log.grid(row=3, column=0,sticky='nsew',pady=(10, 0)) 
        self.open_sdk_log.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.open_crash_log = tk.Button(self, text="Editor log", command=self.open_crashlog)
        self.open_crash_log.grid(row=4, column=0,sticky='nsew',pady=(10, 0)) 
        self.open_crash_log.config(font=(self.settings.text_font, int(self.settings.text_size)))

        # self.test_path_log = tk.Button(self, text="TestPath log", command=self.generate_testpath)
        # self.test_path_log.grid(row=5, column=0,sticky='nsew',pady=(10, 0)) 
        # self.test_path_log.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.test_auto = tk.Button(self, text="Auto Test", command=self.auto_test)
        self.test_auto.grid(row=5, column=0,sticky='nsew',pady=(10, 0)) 
        self.test_auto.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.arrow()
        if isinstance(self.result,tuple) and not all(self.result):
            self.update_button.config(state="disabled")
            messagebox.showwarning("License Error", f"{', '.join(j for i,j in zip(self.result,('软件过期','硬件错误','程序错误','授权错误')) if not i)}, 联系微信号w809500586购买")


    def open_applog(self):
                # Define the directory where the logs are stored
        log_directory = self.settings.propath + "/logs"#"F:/UnityProjects/crealityscan_pc2/Logs"
        
                # Find all directories in the log directory
        log_folders = [d for d in os.listdir(log_directory) if os.path.isdir(os.path.join(log_directory, d))]
        
        if log_folders:
            # Sort the folders by name in descending order to get the latest
            latest_folder = max(log_folders)
            latest_folder_path = os.path.join(log_directory, latest_folder)
            
            # Use glob to find all app_*.log files in the latest folder
            log_files = glob.glob(os.path.join(latest_folder_path, "app.log"))
            
            if log_files:

                # Sort the files by modification time in descending order
                latest_log_file = max(log_files, key=os.path.getmtime)
                
                # Open the latest log file
                os.startfile(latest_log_file)
            else:
                messagebox.showinfo("Info", "No log files found.")

    def auto_test(self):
        Test(self.settings.propath + "/CrealityScan 4.exe")

    def generate_testpath(self):
        import re

        # Define the directory where the logs are stored
        log_directory = os.path.join(self.settings.propath, "logs")
        
        # Find all directories in the log directory
        log_folders = [d for d in os.listdir(log_directory) if os.path.isdir(os.path.join(log_directory, d))]
        
        if log_folders:
            # Sort the folders by name in descending order to get the latest
            latest_folder = max(log_folders)
            print(latest_folder)
            latest_folder_path = os.path.join(log_directory, latest_folder)
            print(latest_folder_path)
            # Use glob to find all app_*.log files in the latest folder
            log_files = glob.glob(os.path.join(latest_folder_path, "app*.log"))
            print(log_files)
            if log_files:
                # Sort the files by modification time in descending order
                latest_log_file = max(log_files, key=os.path.getmtime)
                
                # Open the latest log file and extract relevant messages
                with open(latest_log_file, 'r', encoding='utf-8') as file:
                    log_content = file.readlines()
                
                # Extract messages after "测试路径"
                extracted_messages = []
                for line in log_content:
                    if "测试路径" in line:
                        match = re.search(r"测试路径.*?(\w+ Clicked)", line)
                        if match:
                            extracted_messages.append(match.group(1))
                
                # Write extracted messages to a new file
                testpath_log_file = os.path.join(latest_folder_path, "app_testpath.log")
                with open(testpath_log_file, 'w', encoding='utf-8') as file:
                    for message in extracted_messages:
                        file.write(message + "\n")
                
                # Open the new log file
                os.startfile(testpath_log_file)
            else:
                messagebox.showinfo("Info", "No log files found in the latest folder.")
        else:
            messagebox.showinfo("Info", "No log folders found.")

    def open_crashlog(self):
        edit_log_file = self.settings.editpath; #"C:/Users/xiwen/AppData/Local/Unity/Editor/Editor.log"
        os.startfile(edit_log_file)
        pass

    def open_sdklog(self):
        # Define the directory where the logs are stored
        log_directory = self.settings.propath + "/logs"#"F:/UnityProjects/crealityscan_pc2/Logs"
        

                # Find all directories in the log directory
        log_folders = [d for d in os.listdir(log_directory) if os.path.isdir(os.path.join(log_directory, d))]
        
        if log_folders:
            # Sort the folders by name in descending order to get the latest
            latest_folder = max(log_folders)
            print(latest_folder)
            latest_folder_path = os.path.join(log_directory, latest_folder)
            print(latest_folder_path)
            # Use glob to find all scan_log_*.txt files
            log_files = glob.glob(os.path.join(latest_folder_path, "scan_log_*.txt"))
            print(log_files)
            if log_files:
                # Sort the files by modification time in descending order
                latest_log_file = max(log_files, key=os.path.getmtime)
                
                # Open the latest log file
                os.startfile(latest_log_file)
            else:
                messagebox.showinfo("Info", "No log files found.")

    def vibrate_window(self, magnitude, duration, steps):
        x, y = self.winfo_x(), self.winfo_y()
        for _ in range(steps):
            self.geometry(f"+{x + magnitude}+{y}")
            self.update_idletasks()
            self.geometry(f"+{x - magnitude}+{y}")
            self.update_idletasks()
        self.geometry(f"+{x}+{y}")

    def set_reminder(self):
        self.vibrate_window(5,300,100)
        try:
            t1 = Thread(target=self.play_sound)
            t1.start()
        except:
            pass
        self.flash()
        self.isWork = False


    def enable_button_with_countdown(self, seconds_left):
        if seconds_left > 0:
            # self.update_button.config(state="disabled")
            self.update_button.config(text=f"休息时间 ({int(seconds_left/60)}分{seconds_left%60}秒)")
            self.rest_id = self.after(1000, lambda: self.enable_button_with_countdown(seconds_left - 1))
        else:
            # self.update_button.config(state="normal")
            self.reminderTimes += 1
            if "Trial" in self.edition:
                if self.reminderTimes >= 2:
                    self.update_button.config(text="开始工作")
                    messagebox.showwarning("Version Notes", "试用版连续提醒已超过限制，请手动再次开始或者购买升级")
                    return
            self.contiue_work()
            
    def cancel_work(self):
        if self.isWork:
            if self.work_id:
                self.after_cancel(self.work_id)  # Cancel the after event
                self.work_id = None  # Reset the after_id 
        else:
            if self.rest_id:
                self.after_cancel(self.rest_id)  # Cancel the after event
                self.rest_id = None  # Reset the after_id 

    def work_button(self,seconds_left):
        if seconds_left > 0:
            self.update_button.config(state="disabled")
            self.update_button.config(text=f"Restaring... ({seconds_left%60}秒)")
            self.work_id = self.after(1000, lambda: self.work_button(seconds_left - 1))
        else:
            self.update_button.config(text=f"Restart Unity")
            self.update_button.config(state="normal")
            # try:
            #     t1 = Thread(target=self.restart_unity)
            #     t1.start()
            # except:
            #     pass
            self.arrow()


    def play_sound(self):
        if self.settings.sound_on:
            f=path(self.settings.sound_file)
            if f:
                wave_obj = sa.WaveObject.from_wave_file(f)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                          
    def check_Time(self):
        set = self.settings.workminutes
        if set <= 0:
            try:
                t1 = Thread(target=showMsgGapFisrt)
                t1.start()
            except:
                pass
                # logger.debug("error, no set gap time")
            return False
    
    def arrow(self):
        f=path(self.settings.arrow_up if True else self.settings.arrow_down)
        self.iconphoto(False,tk.PhotoImage(file=f)) if f else None

    def on_closing(self):
        if any(i!=j for i,j in zip(values(self.settings),self.settings0)):
            if messagebox.askokcancel("Quit", "设置已修改，是否保存？"):
                dump1(dataclasses.asdict(self.settings),self.settingsfile)
        self.destroy()

    def contiue_work(self):
        self.cancel_work()
        self.work_button(0.1*60)
        self.isWork = True
        self.arrow()

    def start_work(self):
        self.reminderTimes = 0
        self.contiue_work()

    def restart_unity(self):
        import subprocess
        # Kill the Unity process with the specified window title
        project_name = os.path.basename(self.settings.propath)
        subprocess.run(f'taskkill /F /IM Unity.exe /FI "WINDOWTITLE eq {project_name}*"', shell=True)
        # Wait for 3 seconds
        subprocess.run('timeout /t 3 /nobreak >nul', shell=True)
        # Start Unity with the specified project path
        # subprocess.run('"C:\\Program Files\\Unity\\Hub\\Editor\\2022.3.20f1\\Editor\\Unity.exe" -projectPath "F:\\UnityProjects\\crealityscan_pc2"', shell=True)
        subprocess.run(f'"{self.settings.exepath}" -projectPath "{self.settings.propath}"', shell=True)
     
    def kill_unity(self):
        import subprocess
        # Kill the Unity process with the specified window title
        subprocess.run('taskkill /F /IM Unity.exe', shell=True)


    def Restart(self):
        self.reminderTimes = 0
        self.contiue_work()
        try:
            t1 = Thread(target=self.restart_unity)
            t1.start()
        except:
            pass


        
if __name__ == '__main__':
    # logger.add('worker.log') 
    app = RestReminderWin()
    app.mainloop()

    