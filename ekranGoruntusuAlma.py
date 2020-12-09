from PIL import ImageGrab
import keyboard
from datetime import datetime

while True:
    try:
        if keyboard.is_pressed('c'):
            image = ImageGrab.grab()
            image.save(f"{datetime.today().strftime('%Y-%m-%d')}.png")
            break
        else:
            pass
    except:
        break
