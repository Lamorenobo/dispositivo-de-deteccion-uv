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

# Version (Protoboard)
tras tener la programacion del microcrontolador y el esquema del circuito, procedimos a pasarlo todo a una protoboard y comprobar el funcionamiento de todo el dispositivo
![IMG-20231101-WA0012](https://github.com/Lamorenobo/dispositivo-de-deteccion-uv/assets/142939223/cd006ca4-e626-4ef7-86d0-6ea3b0fa4b34)



En esas fotos se puede apreciar nuestra felicidad al percaarnos que el ESP-32 estaba haciendo su trabajo a la perfeccion, encendiendo y apagando Leds, dependiendo a la radiacion UV que fuera expuesto el SENSOR, ya solo faltaba empezar a crear la aplicacion
# Capitulo:PCB
Sin embargo debido a errores grupales no contabamos con que el proyecto debia realizarse sobre una PCB, por lo cual empezamos a documentarnos sobre el uso de la herramienta KICAD y las 
 librerias necesarias para armar el Esquema de la PCB para posteriormente mandarla a fabricar
Primera Version de la PCB:(Error)

Segunda Version:(Error)

PCB FINAL:


# Componentes en la PCB.....
Despues de tener Todos los materiales necesarios, nos vimos ante el reto de la soldadura puesto que ninguno tenia la experticia ni la tecnica para esta, sin embargo tras dedicarle bastante y con ayuda del profesor Johnny, logramos soldar todos los componenetes del dispositivo de manera correcta en la PCB:

Soldadura:

Dispositivo Final:
# Prueba ¿Final?:
Tras el armado del Dispositivo fisico procedimos a probarlo, y tras un primer fallo debido a un error de digitalizacion de un pin en el codgio, no obtuvimos el resultado esperado, sin embargo despues de corregir este error, obtuvimos lo que queriamos:

# La aplicacion:
La otra parte del proyecto no tuvo mayores inconvenientes, si no hasta lampreuba final, ya que .................
Como solucion a esto pasamos todo el codigo del ESP-32 el cual estab en Micropython, a el lenguaje C.
# Aplicacion Final:
