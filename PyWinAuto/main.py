from pywinauto import *
import time

app = Application()
#app.start(r"C:\Users\HP\AppData\Local\WhatsApp\WhatsApp.exe")
app.connect(title="WhatsApp", backend="win32" , visible_only="False")

time.sleep(120)
print("End of Waiting")

app.WhatsApp.print_control_identifiers()
#   app.WhatsApp.child_window(title="WhatsApp", class_name="Chrome_WidgetWin_1").click_input()
