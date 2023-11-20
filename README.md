# Dispositivo de detección uv
Nuestro dispositivo detecta la rediacion uv, y envia esta señal a una app en la cual dependiendo de el rango de  la radiacion se muestran las prevenciones que hay que tener para prevenir afectaciones por rayos UV
## Introducción
Nuestro proyecto consiste en un dispositivo capaz de detectar la radiacion UV, el cual envia unas señales al microcontrolador(ESP-32), y dependeindo el rango de intensidad de radiacion UV, se encarga de prender o apagar unos leds en el dispositivo los cuales  indican la peligrosidad de radiacion en ese momento especifico. Paralelemanete a esto mediante la conexion bluethot entre el esp 32 y el celular, se le indica al usario las prebenciones que deberia tomar de acuerdo al indice de radiaicon Uv que este indicando el microcontrolador, todo esto a travez de una aplicacion programda en app inventor.
## ¿porque?
Despues de realizar un analisis prifundo al clima de la ciudad de Bogota , nos dimos cuenta que la radiacion UV durante el dia, se mantiene en indices que se  consideran perjudicales para la piel,junto a esto tambien relacionamos  muchos datos de la liga colombinaa contra el cancer y le INC  los cuales indican que Bogota es una de las ciudades con mas inicidencia en casos de cancer de piel, y es aca donde nos dimos cuenta que estos dos datos estan correlacionados por lo cual nos parecio indispensable crear un dispopitvo que avise en todo momento a los bogotanos sobre la radiacion UV que  se presenta al instante, y las precauciones que deberian tomar.
# diagrama de cajas negras
<img src="https://i.postimg.cc/Vvc1S3F4/diagrama-de-cajas.png">

# Esquema del circuito 
A continuación presentamos el circuito  del dispositivo de detección UV elaborado en kicad.
<img src="https://i.postimg.cc/bJVkp9Hz/esquema-en-kicad.png">
