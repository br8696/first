import RPi.GPIO as io
from time import sleep
io.setmode(io,BCM)
a=[18,23,24]
"""
for i in range(3):
    io.setup(a[i],io.OUT)
while True:
    for i in range(3):
        io.output(a[i],True)
        sleep(1)
    for i in range(3):
        io.output(a[i],False)
        sleep(1)
"""

for i in a:
    io.setup(a.io,out)
i=0
b=0
while True:
    io.output(a[i],True)
    sleep(1)
    print i
    i=i+1
    if(i==(len(a)-1)):
        while True:
            io.output(a[i],False)
            sleep(1)
            i=i-1
            print i
            if(i==0):
                break
        
