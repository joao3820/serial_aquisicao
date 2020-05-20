from machine import Pin, PWM

class Led:
    def __init__(self, pin_no):
        self.pin_no = pin_no
        self.led = PWM(Pin(self.pin_no))
        self.led.freq(100)

    def duty(self, percentagem):
        self.led.duty(int(percentagem*1023/255))  # temos que 255 é o valor máximo permitido, que guardaremos no bloco de notas, nas configurações do sistema de iluminação
