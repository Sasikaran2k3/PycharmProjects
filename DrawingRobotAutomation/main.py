import time
import InkScape
import WapAutomation

WapAutomation.BeginWap()
WapAutomation.WapTransfer("DRAWING_ROBOT")
Command = WapAutomation.LastMsg()
WapAutomation.SendWap(Command)
InkScape.BeginInk()
InkScape.StartWrite(Command)
InkScape.Trace_BitImage()
InkScape.OpenExtention()
quit()
time.sleep(2)
ChatterBot.StartChatterBot()
ChatterBot.BotTrain()
Content, Mode = ChatterBot.BotResponse(Command)


if Mode == "draw":
    print("Selenium On Stage")
    ImageDownloadAutomation.BeginSelinium()
    Path = ImageDownloadAutomation.Search(Content)
    time.sleep(5)
    print(Path)
    InkScape.BeginInk()
    InkScape.StartDraw(Path)
    InkScape.Trace_BitImage()
    InkScape.SaveBitImg("Query")
    WapAutomation.SendWap("Gcode Ready .... Press Enter to Continue")
    Path = "E:\Collections of Gcode\\" + "Query_" + "0001.gcode"
    InkScape.UniGcode(Path)
elif Mode == "write":
    InkScape.BeginInk()
    InkScape.StartWrite(Content,"90")
    InkScape.Trace_BitImage()
    InkScape.SaveBitImg("Query")
    WapAutomation.SendWap("Gcode Ready .... Press Enter to Continue")
    Path = "E:\Collections of Gcode\\" + "Query_" + "0001.gcode"
    InkScape.UniGcode(Path)
elif Mode == "Chat":
        WapAutomation.SendWap(Content)
