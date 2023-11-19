# dispositivo-de-deteccion-uv
Nuestro dispositivo detecta la rediacion uv, y envia esta señal a una app en la cual dependiendo de el rango de  la radiacion se muestran las prevenciones que hay que tener para prevenir afectaciones por rayos UV
# INTRODUCCION
Nuestro proyecto consiste en un dispositivo capaz de detectar la radiacion UV que envia unas señales al microcontrolador(ESP-32),el cual es programado con micropython, y dependeindo el rango e intensidad de radiaicon UV, se encarga de prender o apagar unos leds en el dipsotivo que indican la peligroidad de radiacion en ese momento especifico.Paralelemanete a esto mediante la conexion bluethot entre el esp 32 y el celular, se le indica al usario las prebenciones que deberia tomar de acuerdo al indice de radiaicon Uv que este indicando el microcontrolador, todo esto a travez de una aplicacion programda en app inventor.
#¿porque?
Despues de realizar un analisis prifundo al clima de la ciidad de Bogota , nos dimos cuenta que la radiacion UV durante el dia, se mantiene en indices conseidrados cmo perjudicales para la piel,junto a esto tambine nos dimso cuenta que muhcos datos de la liga colombinaa ocntra el cancer y le INC indican que Bogota e sna de las ciudades con mas inicendica en caoss de cancer de piel, y es aca odnde nos dimos cuenta que estos dos datos tienen una importante correlacion por lo cual nos parecio indispensable crear un disppitvo que avise en todo9 momento a los bogotanos sobre la radiacion UV que  se presneta al instante, y las precuaicones que deberia tomar
# diagrama de cajas negras
<img src="https://i.postimg.cc/Vvc1S3F4/diagrama-de-cajas.png">

# Esquema del circuito 
A continuación presentamos el circuito  del dispositivo de detección UV elaborado en kicad
<img src="https://i.postimg.cc/bJVkp9Hz/esquema-en-kicad.png">
