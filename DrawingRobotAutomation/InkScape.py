import time
import datetime
import pyautogui as py
from pywinauto import *


def BeginInk():
    ink = Application(backend="uia")
    ink.start(r"C:\Program Files\Inkscape\bin\inkscape.exe")
    ink.connect(title='New document 1 - Inkscape', timeout=20, title_re=".*Windows Software.*")
    """
    ink.NewDocumentInkscape.print_control_identifiers()
    MinButton = ink.NewDocumentInkscape.child_window(title="Minimize", control_type="Button").wrapper_object()
    MaxButton = ink.NewDocumentInkscape.child_window(title="Restore", control_type="Button").wrapper_object()
    MaxButton.click_input()
    MinButton.click_input()
    MaxButton.click_input()
"""
def StartWrite(text="R M D Engineering College", font="50"):
    py.press("5")  # Fitpage
    py.moveTo(16, 485, duration=0.5)  # TextTool
    py.click()
    if (len(text) < 100):
        py.moveTo(1240, 68, duration=0.5)  # Vertical Font
        py.click()
        py.moveTo(460, 120, duration=0.5)  # TextBox
        py.dragTo(260, 660, 2, button="left")
        py.hotkey("ctrl", "a")
        py.write(text)
        py.moveTo(647, 67, duration=0.5)  # Allign Centre
        py.click()
        py.hotkey("ctrl", "a")
        py.moveTo(388, 64, duration=0.5)
        py.doubleClick()
        py.hotkey("ctrl", "a")
        py.write(font)
        py.press("enter")
        print("Done Written")

    else:
        py.moveTo(1214, 65)  # Horizontal Font
        py.click()
        py.moveTo(388, 64, duration=0.5)
        py.doubleClick()
        py.write(font)
        py.press("enter")
        py.moveTo(270, 122, duration=0.5)  # TextBox
        py.dragTo(650, 665, 2, button="left")
        py.write(text)
        py.press("f1")
        py.hotkey("ctrl", "a")
        print("Done Written")


def StartDraw(path):
    py.press("5")  # Fitpage
    py.hotkey("ctrl","o")
    time.sleep(1)
    py.write(path)
    py.press("enter")


def Trace_BitImage():
    py.press("f1")  # Selection Tool
    py.hotkey("ctrl", "a")
    py.hotkey("alt", "b")  # Bit map Copy
    print("Bit Map Ready")
    py.hotkey("alt", "shift", "b")  # Trace Bit map
    time.sleep(2)
    py.press("tab",presses=3)
    py.write("0.650")
    py.press(["tab"]*12)  # For enter button ... Since the tab position is random
    py.press("enter")  # Trace Bit map Completed
    py.hotkey("alt", "f4")  # Close Bit map
    py.hotkey("f1")  # Select
    py.hotkey("alt", "i")
    py.moveTo(430, 360, duration=0.5)  # Select Bit Map
    py.dragTo(630, 360, 1)  # Drag it
    py.hotkey("shift", "1")
    py.hotkey("alt", "i")
    py.press("delete")
    py.moveTo(610, 360, duration=0.5)
    py.dragTo(410, 360, 1)
    py.hotkey("ctrl", "a")
    py.hotkey("shift", "alt", "i")


def SaveBitImg(text):
    py.moveTo(375,37)
    py.click()
    py.press(["down"]*3)
    py.press("right")
    py.press("down")
    py.press("enter")
    py.press("tab", presses=12)
    py.write(text+".gcode")
    py.press("tab",presses=5)
    py.press("enter")
    time.sleep(15)
    py.hotkey("alt","f4")
    py.hotkey("alt", "w")


def UniGcode(path):
    gcode = Application(backend="uia")
    gcode.start(r"C:\Users\HP\Downloads\ugsplatform-win\bin\ugsplatform64.exe")
    gcode.connect(title='Universal Gcode Platform (Version 2.0.7-SNAPSHOT / Dec 02, 2020)', timeout=100)
    py.moveTo(20, 60, duration=0.5)
    py.click()
    time.sleep(3    )
    py.write(path+"\n")
    time.sleep(10)
    py.moveTo(60, 60, duration=0.5)
    py.click()
    time.sleep(10)
    py.moveTo(80, 130, duration=0.5)
    py.click()
    time.sleep(10)
    py.moveTo(95, 55, duration=0.5)
    py.click()
