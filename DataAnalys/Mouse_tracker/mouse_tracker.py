import json
import csv
from time import sleep
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x, pt.y]

with open ('record.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow('xy')

while True:
    sleep(0.01)
    with open ('record.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(queryMousePosition())
