# import threading
# import subprocess

import keyboard
import tkinter as tk
import my_hotkeys

mode = 0 # 0 = insert / 1 = normal
window = tk.Tk()
window.config(background="black")
frm = tk.Frame(window)

#frame = tk.Frame(window)
#frame.pack()
#button = tk.Button(frame,text="a",font=("Consolas", 25),width=3)
#button.pack()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.overrideredirect(1)

print (window.wm_attributes())

def pos_window():
    window_width = 400
    window_height = 300
    position_right = int(screen_width/2.0 - window_width/2)
    position_down = int(screen_height/1.1 - window_height/2)
    window.geometry(f"+{position_right}+{position_down}")
    window.geometry("400x300")

window.attributes('-alpha', 0.8, 
                  '-transparentcolor', '', 
                  '-disabled', 0, 
                  '-fullscreen', 0, 
                  '-toolwindow', 0, 
                  '-topmost', 0)

list_my_hotkeys = {'e':'explorer',
                   'r':'browser',
                   'E':'emacs',
                   'k':'keepass'}

list_my_programs = {
   
}

def activate_Vmode(x):
    if x == 0:
      set_mode(1)
      print("\nadding hotkeys\n")
      # activates these hotkeys
      keyboard.add_hotkey("e", my_hotkeys.run_explorer, suppress=True)
      print("added e")
      keyboard.add_hotkey("r", my_hotkeys.run_browser, suppress=True)
      print("added r")
      keyboard.add_hotkey("shift+e", my_hotkeys.run_emacs, suppress=True)
      print("added t")
      # keyboard.add_hotkey("k", my_hotkeys.run_keepass, suppress=True)
      # print("added k")
      
      # populate the cheat sheet
      print_cheatsheet()
      pos_window()
      print("\nVmode activated...\n")


    elif x == 1:
      set_mode(1)
      print("Leader already added")


def print_cheatsheet():
   print("\nListing Keybinds...\n")
   window.attributes('-topmost', True)
   global frm
   frm = tk.Frame(window)
   frm.config(background="black")
   r = 0
   c = 0
#  frm.pack()
   frm.grid()
   for key, value in list_my_hotkeys.items():
    print(key,value)
   
   for key, value in list_my_hotkeys.items():
    tk.Button(frm,text=key + " " + value,
                     font=("Consolas",22),
                     bg="black",
                     fg="white",
                     anchor="w",
                     padx=10,
                     pady=10, 
                     bd= 0).grid(column=c, row=r)
    
    if r == 2:
       c += 1
       r = 0
    else:
      r += 1

#   btn.pack()
#   window.iconphoto(False)
#   print(list_my_hotkeys.items())

def activate_Imode():
    keyboard.remove_all_hotkeys()
    keyboard.add_hotkey("esc", deactivate_Vmode, suppress=True)
    set_mode(0)
    window.attributes('-alpha', 0.1,'-topmost', False, '-disabled', 1)
    window.config(background="red")
    window.geometry("0x0")
    frm.destroy()
    print("\nImode activated, press esc to return\n")

def deactivate_Vmode(): 
    print("\ndeactivating Vmode removing hotkeys...\n")
    keyboard.remove_all_hotkeys()
    set_mode(0)
    activate_Leader()
    window.attributes('-alpha', 0.8,'-topmost', 0, '-disabled', 0)
    window.config(background="black")
    frm.destroy()
    pos_window()
    print("\nVmode deactivated...\n")

def activate_Leader():
    print("\nRegistering leader Keys...\n")
    keyboard.add_hotkey("space", lambda: activate_Vmode(mode), suppress=True)
    keyboard.add_hotkey("esc", deactivate_Vmode, suppress=True)
    keyboard.add_hotkey("i", activate_Imode, suppress=True)
    print("\nleader keys added\n")

def set_mode(x):
  global mode
  mode = x

def main():
   activate_Leader()
   pos_window()
   window.mainloop()

main()

# def mainloop():
#    root = tk.Tk()
#    root.mainloop()

#t_win = threading.Thread(target=mainloop, args=())
#t_win.start()
#tmain = threading.Thread(target=keyboard.wait, args=())
#tmain.start()









#def initiate():
#    keyboard.add_hotkey("ctrl+space", lambda: activate_Leader(ldr), suppress=True)
#    print("init")
#initiate()

# keyboard.wait() 