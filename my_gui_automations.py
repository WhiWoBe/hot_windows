import pyautogui

pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 1

def get_pos(image: str):
    try:
        pos = pyautogui.locateCenterOnScreen(image, confidence=0.7)
        if pos is None:
            print(f'{image} not found on  screen')
        else:
            x = pos[0]
            y = pos[1]
            return x, y
    except OSError as e:
        raise Exception(e)
    
if __name__ == "__main__":
    position = get_pos('Unbenannt.png')
    print(position)
    pyautogui.moveTo(position, duration=0.2)
