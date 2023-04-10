import time

import pyautogui as py
from pyautogui import *
from pywinauto import *

ink = Application(backend="uia")
ink.start(r"C:\Program Files\Inkscape\bin\inkscape.exe")
ink.connect(title='New document 1 - Inkscape',timeout=10,title_re=".*Windows Software.*")

def StartWrite(text="R M D Engineering College",font="50"):
    # Fitpage
    py.press("5")
    # TextTool
    py.moveTo(16, 485, duration=0.5)
    py.click()
    if(len(text)<100):
        # Vertical Font
        py.moveTo(1240, 68, duration=0.5)
        py.click()
        # TextBox
        py.moveTo(460,120,duration = 0.5)
        py.dragTo(260 , 673, 2, button="left")
        py.hotkey("ctrl","a")
        py.write(text)
        py.moveTo(647,67,duration = 0.5)
        py.click()
        #Change font
        py.hotkey("ctrl","a")
        py.moveTo(388, 64, duration=0.5)
        py.doubleClick()
        py.hotkey("ctrl", "a")
        py.write(font)
        py.press("enter")
    else:
        py.moveTo(1214, 65)
        py.click()
        py.moveTo(270, 122, duration=0.5)
        py.dragTo(650, 665, 2, button="left")
        py.write(text)
        time.sleep(4)
        py.press("f1")
        print("Done Written")
def Gcode_Converter():
    py.hotkey("ctrl","a")
    time.sleep(2)
    print("bit")
    py.hotkey("alt", "b") # Bit map Copy
    py.hotkey("alt", "shift", "b") # Trace Bit map
    py.press(["tab"]*14) # For enter button ... Since the tab position is random
    time.sleep(2) # For few Cases
    py.press("tab")  # Last Jump
    py.press("enter") # Trace Bit map Completed
    py.hotkey("alt","f4") # Close Bit map
    py.hotkey("f1") # Select
    py.hotkey("alt", "i")
    py.moveTo(430, 410, duration=0.5) # Select Bit Map
    py.dragTo(630, 410, 1) # Drag it
    py.press("f1")
    py.hotkey("shift","1")
    time.sleep(2)
    py.hotkey("alt","i")
    py.moveTo(430, 410, duration=0.5)
    py.click()
    py.press("delete")
    py.click()
    py.press("delete")
    py.moveTo(610, 410, duration=0.5)
    py.dragTo(460, 410, 1)
    time.sleep(2)
    py.hotkey("ctrl", "a")
    py.hotkey("shift", "alt", "i")
StartWrite("Naveen Broo Manogara Brooo Sasi Brooo Salman Brooosdfsdfasdfasfasfasgasgasgasdgasgasgasdfgasdgadsfgsdfgsdfgagasgasgadfgdfgsdfgsdgsdfgdfgsdfaggasgsagafsgasgasg",font="90")
#StartWrite("R M D Engineering College")
Gcode_Converter()
