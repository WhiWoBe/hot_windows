from time import sleep
import keyboard
import tkinter as tk
import my_hotkeys

mode = 0 # 0 = insert / 1 = normal
window = tk.Tk()
window.config(background="black")
frm = tk.Frame(window)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.overrideredirect(1)
print (window.wm_attributes())
window.attributes('-alpha', 0.8, 
                  '-transparentcolor', '', 
                  '-disabled', 0, 
                  '-fullscreen', 0, 
                  '-toolwindow', 0, 
                  '-topmost', 0)

print(my_hotkeys.d_my_files['1'][0])

# for key, value in d_my_programs.items():
#     print(key,value[:3:2])

# print(list(d_my_programs.items())[0])

def pos_window():
    window_width = 400
    window_height = 300
    position_right = int(screen_width/2.1 - window_width/2)
    position_down = int(screen_height/1 - window_height/2)
    window.geometry(f"+{position_right}+{position_down}")
    window.geometry("800x100")

def activate_filelist():
  keyboard.remove_all_hotkeys()
  keyboard.add_hotkey("esc", deactivate_Vmode, suppress=True)
  keyboard.add_hotkey("1", lambda: my_hotkeys.run_explorer_sub('1'), suppress=True)
  keyboard.add_hotkey("2", lambda: my_hotkeys.run_explorer_sub('2'), suppress=True)
  keyboard.add_hotkey("3", lambda: my_hotkeys.run_explorer_sub('3'), suppress=True)
  keyboard.add_hotkey("4", lambda: my_hotkeys.run_explorer_sub('4'), suppress=True)
  keyboard.add_hotkey("5", lambda: my_hotkeys.run_explorer_sub('5'), suppress=True)
  frm.destroy()
  print_cheatsheet(my_hotkeys.d_my_files)
 
def activate_urllist():
  keyboard.remove_all_hotkeys()
  keyboard.add_hotkey("esc", deactivate_Vmode, suppress=True)
  keyboard.add_hotkey("1", lambda: my_hotkeys.run_browser_sub('1'), suppress=True)
  keyboard.add_hotkey("2", lambda: my_hotkeys.run_browser_sub('2'), suppress=True)
  keyboard.add_hotkey("3", lambda: my_hotkeys.run_browser_sub('3'), suppress=True)
  keyboard.add_hotkey("4", lambda: my_hotkeys.run_browser_sub('4'), suppress=True)
  keyboard.add_hotkey("5", lambda: my_hotkeys.run_browser_sub('5'), suppress=True)
  frm.destroy()
  print_cheatsheet(my_hotkeys.d_my_urls)

def activate_Vmode(x):
    if x == 0:
      set_mode(1)
      print("\nadding hotkeys\n")
      # activates these hotkeys
      keyboard.add_hotkey("f", my_hotkeys.run_explorer, suppress=True)
      keyboard.add_hotkey("shift+f", activate_filelist, suppress=True)
      keyboard.add_hotkey("shift+e", my_hotkeys.run_emacs, suppress=True)
      keyboard.add_hotkey("c", my_hotkeys.run_calendar, suppress=True)
      keyboard.add_hotkey("r", my_hotkeys.run_browser, suppress=True)
      keyboard.add_hotkey("shift+r", activate_urllist, suppress=True)
      keyboard.add_hotkey("k", my_hotkeys.run_keepass, suppress=True)
      keyboard.add_hotkey("shift+t", my_hotkeys.run_timo, suppress=True)
      keyboard.add_hotkey("shift+c", my_hotkeys.run_circular, suppress=True)
      keyboard.add_hotkey("q", run_quit, suppress=True)
      

      print("added hotkeys")      
      # populate the cheat sheet
      print_cheatsheet(my_hotkeys.d_my_hotkeys)
      pos_window()
      print("\nVmode activated...\n")

    elif x == 1:
      set_mode(1)
      print("Leader already added")


def print_cheatsheet(dict):
   print("\nListing Keybinds...\n")
   window.attributes('-topmost', True)
   global frm
   frm = tk.Frame(window)
   frm.config(background="black")
   r = 0
   c = 0
   frm.grid()
   for key, value in dict.items():
    print(key,value)
   
   for key, value in dict.items():
    tk.Button(frm,text=str(key) + " " + value[0],
                     font=("Consolas",16),
                     bg="black",
                     fg="white",
                     anchor="w",
                     padx=10,
                     pady=10, 
                     bd= 0).grid(column=c, row=r)
    
    if r == 1:
       c += 1
       r = 0
    else:
      r += 1

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
    keyboard.add_hotkey("alt+space", lambda: activate_Vmode(mode), suppress=True)
    keyboard.add_hotkey("esc", deactivate_Vmode, suppress=True)
    keyboard.add_hotkey("i", activate_Imode, suppress=True)
    print("\nleader keys added\n")

def set_mode(x):
  global mode
  mode = x

def run_quit():
      sleep(0.4)
      window.destroy()

def main():
   if __name__ == "__main__":
      activate_Leader()
      pos_window()
      window.mainloop()

main()