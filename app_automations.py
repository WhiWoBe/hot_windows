from time import sleep
import pyautogui
import secret
import webbrowser

# Specify the URL you want to open

pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 1

def get_pos(image: str):
    try:
        pos = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if pos is None:
            print(f'{image} not found on  screen')
        else:
            x = pos[0]
            y = pos[1]
            return x, y
    except OSError as e:
        raise Exception(e)
    
def restart_router_wifi():
    # Open the URL in a new tab
    webbrowser.open("https://192.168.1.1/", new=2)
    # wait
    sleep(9)
    # select the field
    position = get_pos('assets/RouterUserField.png')
    print(position)
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()
    pyautogui.write(secret.routerusername)
    sleep(0.3)
    pyautogui.press("tab")
    pyautogui.write(secret.routerpassword)
    position = get_pos('assets/RounterLoginButton.png')
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()

def timo_login():
    webbrowser.open("https://www.timo24.de/members/login/login.php", new=2)
    # wait
    sleep(2)
    position = get_pos('assets/TimoLoginFirma.png')
    print(position)
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()
    pyautogui.write(secret.timofirma)
    sleep(0.3)
    pyautogui.press("tab")
    pyautogui.write(secret.timousername)
    sleep(0.3)
    pyautogui.press("tab")
    pyautogui.write(secret.timopassword)
    position = get_pos('assets/TimoLoginButton.png')
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()
    sleep(5)
    position = get_pos('assets/TimoZeitbuchungButton.png')
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()
    sleep(1)
    position = get_pos('assets/TimoKommenBuchen.png')
    pyautogui.moveTo(position, duration=0.1)
    # pyautogui.click()

def timo_logout():
    pass

if __name__ == "__main__":
    # restart_router_wifi()
    timo_login()
