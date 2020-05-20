from pwm import Led
import esp
from machine import UART

esp.osdebug(None)

uart = UART(1, 9600)
uart.init(baudrate=9600, bits=8, parity=None, stop=1)

Red = Led(19)
Green = Led(21)
Blue = Led(22)


def update(m):
    s = m.decode("utf-8") # bytes to str
    R = int(s[:3])
    G = int(s[4:7])
    B = int(s[8:11])
    Red.duty(R)
    Green.duty(G)
    Blue.duty(B)

msg = b""
while True:
    n = uart.any()
    if n:
        msg += uart.read(n)
    v = msg.find(b'\n')
    if v >= 0:
        update(msg[:v+1])
        msg = b""

# Red.led.deinit()
# Green.led.deinit()
# Blue.led.deinit()
