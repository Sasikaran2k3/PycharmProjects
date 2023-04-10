import time
import pyttsx3

engine=pyttsx3.init()
# Creating Object

engine.setProperty("rate",178)
# Changing default rate to 178 USING setProperty

engine.say("sasikaran is my boss")
# Say() pile/add ups text in a stack

engine.runAndWait()
# runAndWait() clears the stack by reading

time.sleep(5)
engine.say("I will die for him")
engine.runAndWait()


