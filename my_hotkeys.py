import subprocess
import webbrowser


### Hotkey Definitions

d_my_hotkeys = {
   'e':['explorer'],
   'E':['emacs'],
   'r':['browser'],
   'f':['files'],
   'R':['browse-url'],
   'k':['keepass'],
   'c':['calendar'],
   'q':['quit']
   }
d_my_urls = {
   '1' : ['Youtube', 'https://www.youtube.com/', 'Keybind1'],  
   '2' : ['Calendar', 'https://calendar.google.com/calendar/u/0/r?pli=1', 'Keybind2'],   
   '3' : ['Youtube3', 'https://www.youtube.com/', 'Keybind3'],  
   '4' : ['Youtube4', 'https://www.youtube.com/', 'Keybind4'],  
   '5' : ['Youtube5', 'https://www.youtube.com/', 'Keybind5']  
}
d_my_files = {
   '1' : ['Projects (P)', 'D:\private\projects', 'Keybind1'],  
   '2' : ['Projects (W)', 'D:\kroener\OneDrive - Kröner Medizintechnik\TMI\\04_Projects', 'Keybind2'],   
   '3' : ['Products (W)', 'D:\kroener\OneDrive - Kröner Medizintechnik\TMI\\03_Products', 'Keybind3'],  
   '4' : ['Downloads()', 'D:\down', 'Keybind4'],  
   '5' : ['Notebooks()', 'D:\\notebooks', 'Keybind5']  
}

### HOTKEY ACTIONS

#### Run Generic Program

def run_program(x):
    pass

#### Run Specific Program

def run_explorer():
    subprocess.run("explorer", shell=True)
    print ("Running explorer")

def run_calendar():
    subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe  --profile-directory=Default --app-id=kjbdgfilnfhdoflbpgamdcdgpehopbep --app-url=https://calendar.google.com/calendar/r --app-launch-source=4")
    print ("Running explorer")

def run_explorer_sub(cmd):
    subprocess.run(f'explorer "{d_my_files[cmd][1]}"')
    print ("Running explorer")

def run_browser():
    subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    print ("Running Explorer")

def run_browser_sub(cmd):
    webbrowser.open(d_my_urls[cmd][1])
    print ("Opening Website")

def run_emacs():
    subprocess.run("C:\Program Files\Emacs\emacs-29.1\\bin\\runemacs.exe")
    print ("Running Emacs")

def run_keepass():
    subprocess.Popen("C:\\Program Files\\KeePass Password Safe 2\\KeePass.exe")
    ("Running keepass")