# import usocket as socket
import time, machine, socket
from machine import ADC
from time import sleep
pin = machine.Pin(32, machine.Pin.IN)
verde= machine.Pin(19, machine.Pin.OUT)
amarillo = machine.Pin(18, machine.Pin.OUT)
naranja = machine.Pin(5, machine.Pin.OUT)
rojo = machine.Pin(15, machine.Pin.OUT)
morado = machine.Pin(21, machine.Pin.OUT)
buzzer = machine.Pin(23, machine.Pin.OUT)

adc=ADC(pin)
# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
bufferSize  = 128

# Descomentar si el esp32 será una estación
# from wifiSTA import connectSTA as connect

# Descomentar si el esp32 estará en modo de acceso AP
from wifiAP import apConfig as connect




# poner acá el nombre de red ssid y password para conectarse
connect("Sensor-UV", "87654321")

# Esta función es de ejemplo,
# Lo que se plantea acá es saber qué hacer con el dato recibido
# En el ejemplo solo se está imprimiendo por terminal
def exec(val):
    if val <= 8738 and val >= 0:
        verde.on()
        amarillo.off()
        naranja.off()
        rojo.off()
        morado.off()
        buzzer.off()
        print("bajo")
        return "bajo"
    elif val > 8738 and val <= 21845:
        verde.off()
        amarillo.on()
        naranja.off()
        rojo.off()
        morado.off()
        buzzer.off()
        print("moderado")
        return "moderado"
    elif val > 21845 and val<= 30583:
        verde.off()
        amarillo.off()
        naranja.on()
        rojo.off()
        morado.off()
        buzzer.off()
        print("alto")
        return "alto"
    elif val > 30583 and val<=43690 :
        rojo.on()
        verde.off()
        amarillo.off()
        naranja.off()
        morado.off()
        buzzer.off()
        print("muy alto")
        return "muy alto"
    elif val > 43690:
        morado.on()
        verde.off()
        amarillo.off()
        naranja.off()
        rojo.off()
        buzzer.on()
        print("extremo")
        return "extremo"

sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)

while True:
    conn, addr = sk.accept()

    while True:
        data = conn.recv(bufferSize)
        # Si dato fue recibido, se decide que hacer con el.
        if data:
            val=adc.read_u16()
            # Con la siguiente instruccion se pueden enviar datos al
            # dispositivo conectado
            conn.sendall(str(exec(val)))
            # conn.send("ok")
    conn.close()



