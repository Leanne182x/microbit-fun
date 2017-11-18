#Adapted from https://make.techwillsaveus.com/bbc-microbit/activities/micro-morse-phone
import radio
from microbit import *

dash = Image("00000:00000:99999:00000:00000")
dot = Image("00000:09990:09990:09990:00000")
over = Image("00900:00090:99999:00090:00900")

radio.on()
while True:
    incoming = radio.receive()

    if button_a.is_pressed() and button_b.is_pressed():
        display.show(over)
        radio.send(str("over"))
    elif button_a.is_pressed():
        display.show(dot)
        radio.send(str("dot"))
    elif button_b.is_pressed():
        display.show(dash)
        radio.send(str("dash"))
    elif incoming == "dot":
        display.show(dot)
    elif incoming == "dash":
        display.show(dash)
    elif incoming == "over":
        display.show(over)
    sleep(200)
    display.clear()
