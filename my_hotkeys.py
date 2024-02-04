import os
import subprocess
import keyboard

### Hotkey Definitions

def add_hotkey():
    pass


### HOTKEY ACTIONS

#### Run Generic Program

def run_program(x):
    pass


#### Run Specific Program

def run_explorer():
    os.startfile("")
    print ("Running explorer")

def run_browser():
    subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    print ("Running Explorer")

def run_emacs():
    subprocess.run("C:\Program Files\Emacs\emacs-29.1\\bin\\runemacs.exe")
    print ("Running Emacs")

def run_keepass():
    subprocess.run("C:\Program Files\KeePass Password Safe 2\KeePass.exe")
    print ("Running KeePass")

def run_keepass():
    subprocess.run("C:\Program Files\KeePass Password Safe 2\KeePass.exe")
    print ("Running KeePass")

### HOTKEY DEFINITIONS
    
# run_program()