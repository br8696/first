import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
io.setup(18,io.OUT)

io.output(18,True)
sleep(1)
io.output(18,False)
sleep(1)
