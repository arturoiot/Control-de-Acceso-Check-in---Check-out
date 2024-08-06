#Registro de un nuevo usuario
'''
Este código realiza la comptura de imagen del usuario,
generando una carpeta con Nombre_ApellidoP_ApellidoM_Matricula,
retornando el estatus como Nuevo Usuario.
'''
import os
import sys
import requests
from datetime import datetime
import paho.mqtt.client as mqtt
import json

#Conexion MQTT
client = mqtt.Client()
topic = "topic"
client.connect("IP",1883,60)

def capture_image(person_name):
    # Define URL para captura de imagen
    capture_url = "http://IP-ESP32CAM/capture"
    
    # Envia un request a ESP32-CAM a capturar imagen
    response = requests.get(capture_url)
    
    if response.status_code == 200:
        # Crea un directorio del usuario en caso de que no exista
        person_dir = f"registro_alumnos/{person_name}"
        os.makedirs(person_dir, exist_ok=True)
        
        # Genera el archivo con la hora de captura
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{person_dir}/{person_name}_{timestamp}.jpg"
        
        # Guarda la imagen en el directorio correspondiente
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Imagen capturada {filename}")
    else:
        print("Failed to capture image from ESP32-CAM")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python register_person.py <person_name>")
        sys.exit(1)
    
    person_name = sys.argv[1]
    part = person_name.split("_")

    #Asignamos los datos correspondientes
    nombre = part[0]
    Apellido_P = part[1]
    Apellido_M = part[2]
    Matricula = part[3]

    #Formato json para publicar
    datos = json.dumps({"nom":nombre,"app":Apellido_P,"apm":Apellido_M,"mat":Matricula,"edo":"NUEVO REGISTRO"})
    client.publish(topic,datos)

    capture_image(person_name)