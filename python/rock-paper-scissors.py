from microbit import *
import random

ROCK = "R"
PAPER = "P"
SCISSORS = "S"

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(Image.SMILE)
        sleep(1)
        handshape = random.randint(0,2)

        if handshape == 0:
            display.show(ROCK)
        elif handshape == 1:
            display.show(PAPER)
        else:
            display.show(SCISSORS)

# TODO Count down 3,2,1 before showing the selection
# TODO Create another script to keep score for two players.