# Control de Acceso Check in – Check out mediante lector de biométricos, Lector de Huella Digital, Reconocimiento facial y/o Matricula de Empleado y/o Alumno.

## 1. Introducción
El presente repositorio tiene como objetivo presentar una propuesta para el desarrollo de un prototipo para proporcionar una solución integral que agilice y fortalezca el control de accesos en áreas restringidas, en específico para la implementación de control de acceso en los centros de cómputo de la Facultad de Ciencias Químicas e Ingeniería.

## 2. Problemática
El control de acceso se basa en métodos tradicionales de registro, y esto a menudo resultan ineficientes y pueden llevar a situaciones falta de control. La falta de una identificación segura y rápida de acceso de alumnos y profesores puede generar conflictos y comprometer las instalaciones. También se necesita identificar el uso de los equipos equipo que se les proporciona de manera segura.

## 3. Solucion Propuesta
El prototipo de prospecto de cliente propuesto aborda esta problemática mediante la Visión por Computadora(FaceID).

- **Visión por Computadora**

La visión por computadora se refiere a la capacidad de las máquinas para interpretar y comprender el entorno visual mediante el análisis de imágenes o videos. En este prototipo, la visión por computadora se utiliza para el reconocimiento facial y eficiencia en un registro de entrada y salida, esto proporciona:

*Identificación precisa de individuos*: 
La tecnología FaceID permite una identificación biométrica confiable.

*Detección de comportamientos anómalos*: El sistema puede alertar sobre acciones sospechosas, como personas no autorizadas.

## 4. Objetivos Especificos
- 4.1 Recopilar e implementar técnicas de reconocimiento facial.
- 4.2 Implementar un prototipo de prueba en un centro de computo.
- 4.3  Generar una base de datos de ingreso, salida y registro.

## Materiales Necesarios
- ESP32-CAM
![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/ESP32-CAM.jpg)
- Raspberry Pi 4B 8gb
![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/raspberry.jpg)
- Monitor portatil

![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/monitor.jpg)
- Relevador de 5V
![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/relay.jpg)
- Cables Jumpers

![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/jumpers.jpg)
- Diodo Led
![](https://github.com/arturoiot/Control-de-Acceso-Check-in---Check-out/blob/main/Imagenes/Leds.jpg)

## 6. infraestructura de Software
- [Raspberry Pi OS](https://www.raspberrypi.com/software/)
- [Node-RED](https://nodered.org/)
- [MySQL](https://www.mysql.com/)
- [Arduino](https://www.arduino.cc/)
- [Visual Studio Code](https://code.visualstudio.com/)

## 7. Servicios
- 7.1 Registro de Entrada: Se tomará una foto a la entrada para el registro en la base de datos.
- 7.2 Registro de salida: Se tomará una foto a la entrada para el registro en la base de datos.

## 8. Resultados Esperados
De ser implementado el proyecto, se lograrías los siguientes resultados:
- Restringir el paso a sitios por horarios, puertas y usuarios NO autorizados
- Controlar flujo de personas por las instalaciones 
- Trazabilidad (Generación de Reportes).
- Registro de tiempos y asistencia.
- Control automático de entradas y salidas 
- Control de personas dentro la sala de computo
- Permite un control exacto del personal sin necesidad de presencia de supervisores para el registro de los ingresos y salida de los empleados.

## 9. Conclusiones
El prototipo presenta una solución innovadora al realizar un sistema simple que ayuda a hacer las cosas más seguras, creando un sistema de verificación y registro.

En las pruebas finales se realizaron 2 versiones de Raspberry Pi; Se utilizo la versión 4 y la versión 5.

El prototipo funciona en ambas versiones, sin embargo, notamos que tiene mejor rendimiento en la versión 5. Por lo que se agrega evidencia de ambas versiones.


### Base de Datos: CC
