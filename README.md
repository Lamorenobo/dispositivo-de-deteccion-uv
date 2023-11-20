# Dispositivo de detección uv
Nuestro dispositivo detecta la rediacion uv, y envia esta señal a una app en la cual dependiendo de el rango de  la radiacion se muestran las prevenciones que hay que tener para prevenir afectaciones por rayos UV
## Introducción
Nuestro proyecto consiste en un dispositivo capaz de detectar la radiacion UV, el cual envia unas señales al microcontrolador(ESP-32, programado en C), y dependiendo el rango de intensidad de radiacion UV, se encarga de prender o apagar unos leds en el dispositivo los cuales  indican la peligrosidad de la radiacion en ese momento especifico. Paralelamente a esto,mediante la conexion Bluetooth entre el esp 32 y el celular, se le indica al usario las prevenciones que deberia tomar de acuerdo al indice de radiación UV que este indicando el microcontrolador, todo esto a travez de una aplicacion programada en app inventor.
## ¿Porque?
Despues de realizar un analisis profundo al clima de la ciudad de Bogota, nos dimos cuenta que la radiacion UV durante el día, se mantiene en indices que se  consideran perjudicales para la piel.Ademas es importante mencionar que segun datos de la liga Colombiana contra el cancer y el INC Bogota es una de las ciudades con mas incidencia en casos de cancer de piel, y es aca donde nos dimos cuenta que estos dos datos estan correlacionados por lo cual nos pareció indispensable crear un dispopitvo que avise en todo momento a los bogotanos sobre la radiacion UV que  se presenta al instante, y las precauciones que deberian tomar.
# Objetivo General
Desarrolar un Dispositivo que mediante la lectura del ESP-32 de los datos recogidos por el sensor UV, prenda determiando led indicando la intensidad de radiación UV en tiempo real y por conexión Bluetooth enviar esta información a un aplicativo movil.
# Objetivos específicos
- Programar el microcontrolador y configurar la conectividad Bluetooth 
- Programar una aplicación que indique al usuario las precauciones que debería tomar, dependiendo la intensidad de radiacion UV en tiempo real
- Hacer en KICAD el Diseño de la placa (PCB) en la cual van a ir montados los componentes
- Hacer las respectivas pruebas del artefacto
- Documentar el proceso de creacion
# Materiales
- ESP-32
- Modulo de Carga MH18650
- Portabateria 18650
- Sensor UV
- 5 resistencias de 330 Ohmios
- 1 resistencia de 1KiloOhm
- Placa de Circuito (PCB)
- Materiales para soldar
- Bateria 9V
- 5 Leds
# Proceso Creativo
Empezariamos, como es debido en todo proceso de creacion tecnologico, con el diagrama de caja negra y el esquema del circuito:

# diagrama de cajas negras
<img src="https://i.postimg.cc/Vvc1S3F4/diagrama-de-cajas.png">

# Esquema del circuito 
A continuación presentamos el circuito  del dispositivo de detección UV elaborado en kicad.
<img src="https://i.postimg.cc/bJVkp9Hz/esquema-en-kicad.png">
# Programacion del ESP-32 (Micropython)

import time, machine
from machine import ADC
from time import sleep
pin = machine.Pin(25, machine.Pin.IN)
verde= machine.Pin(21, machine.Pin.OUT)
amarillo = machine.Pin(19, machine.Pin.OUT)
naranja = machine.Pin(18, machine.Pin.OUT)
rojo = machine.Pin(5, machine.Pin.OUT)
morado = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(23, machine.Pin.OUT)
adc = ADC(pin)
while True:
    val = adc.read_u16()# dependiendo el valor se enciende cada led
    print(val)
    if val <= 8738 and val >= 0:
        verde.on()
        amarillo.off()
        naranja.off()
        rojo.off()
        morado.off()
        buzzer.off()
        print("bajo")
    elif val > 8738 and val <= 21845:
        verde.off()
        amarillo.on()
        naranja.off()
        rojo.off()
        morado.off()
        buzzer.off()
        print("moderado")
    elif val > 21845 and val<= 30583:
        verde.off()
        amarillo.off()
        naranja.on()
        rojo.off()
        morado.off()
        buzzer.off()
        print("alto")
    elif val > 30583 and val<=43690 :
        rojo.on()
        verde.off()
        amarillo.off()
        naranja.off()
        morado.off()
        buzzer.off()
        print("muy alto")
    elif val > 43690:
        morado.on()
        verde.off()
        amarillo.off()
        naranja.off()
        rojo.off()
        buzzer.on()
        print("extremo")
##se enciende la alarma
    sleep(1)
# Version (Protoboard)
tras tener la programacion del microcrontolador y el esquema del circuito, procedimos a pasarlo todo a una protoboard y comprobar el funcionamiento de todo el dispositivo
![IMG-20231101-WA0012](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/cd006ca4-e626-4ef7-86d0-6ea3b0fa4b34)
![IMG-20231101-WA0009 (1)](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/1882761e-569a-4de6-bbcb-30b5e1bd2889)
![IMG-20231101-WA0007 (1)](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/7859dd87-f984-44a2-aa87-1661b7eeefd0)

En esas fotos se puede apreciar nuestra felicidad al percaarnos que el ESP-32 estaba haciendo su trabajo a la perfeccion, encendiendo y apagando Leds, dependiendo a la radiacion UV que fuera expuesto el SENSOR, ya solo faltaba empezar a crear la aplicacion
# Capitulo:PCB
Sin embargo debido a errores grupales no contabamos con que el proyecto debia realizarse sobre una PCB, por lo cual empezamos a documentarnos sobre el uso de la herramienta KICAD y las 
 librerias necesarias para armar el Esquema de la PCB para posteriormente mandarla a fabricar
Primera Version de la PCB:(Error)
![image-1](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/b3865dde-5675-484d-9549-cda3c17796f7)


Segunda Version:(Error)
![image-2](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/515148cc-6562-42b6-9f1c-198dca20f6c6)

PCB FINAL:
![image](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/33144e16-bc5f-4f5a-9cc6-ff85843e0b53)
![IMG-20231119-WA0025](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/1a7ce271-ddc5-4419-be28-f555582dc895)


# Componentes en la PCB.....
Despues de tener Todos los materiales necesarios, nos vimos ante el reto de la soldadura puesto que ninguno tenia la experticia ni la tecnica para esta, sin embargo tras dedicarle bastante y con ayuda del profesor Johnny, logramos soldar todos los componenetes del dispositivo de manera correcta en la PCB:

Soldadura:
![IMG-20231119-WA0026 (1)](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/48cfa765-ba74-425b-afa2-0e25a1d116a8)

Dispositivo Final:
![IMG-20231111-WA0007](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/cf82e874-7b2d-4036-8f81-4ffe877c1216)
![IMG-20231119-WA0022](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/c0e7e46a-1c48-40c4-bf70-db69e31ea9da)

# Prueba ¿Final?:
Tras el armado del Dispositivo fisico procedimos a probarlo, y tras un primer fallo debido a un error de digitalizacion de un pin en el codigo, no obtuvimos el resultado esperado, sin embargo despues de corregir este error, obtuvimos lo que queriamos:


https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/29cb111f-80ca-4eb9-bf07-753b7d6bfc69


# La aplicacion:
La otra parte del proyecto no tuvo mayores inconvenientes, si no hasta lampreuba final, ya que .................
Como solucion a esto pasamos todo el codigo del ESP-32 el cual estab en Micropython, a el lenguaje C.
# Programacion ESP-32(C)
[codigo esp32 micropython.txt](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/files/13405605/codigo.esp32.micropython.txt)

##se enciende la alarma
    sleep(1)

# Aplicacion Final:......
