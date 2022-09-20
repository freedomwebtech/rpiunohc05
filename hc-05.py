import serial
import time

bluetooth=serial.Serial("/dev/rfcomm7",9600)

while True:
    a=input("enter:-")
    string='X{0}'.format(a)
    bluetooth.write(string.encode("utf-8"))
    