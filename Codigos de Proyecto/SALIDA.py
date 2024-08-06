# Registro de salida del usuario
'''
Este código realiza la comparación entre una imagen capturada en tiempo real
con respecto a una imagen previamente registarda. Se utiliza la libreria DeepFace
para realizar dicha comparación, de ser verdadero, desplegara los datos del usuario
y el registro de SALIDA.
'''
import os
import requests
from deepface import DeepFace
from datetime import datetime
import paho.mqtt.client as mqtt
import json

#Conexion MQTT
client = mqtt.Client()
topic = "topic"
client.connect("IP",1883,60)

def capture_image():
    # Define the URL to capture the image
    capture_url = "http://IP-ESP32CAM/capture"
    
    # Send a request to the ESP32-CAM to capture the image
    response = requests.get(capture_url)
    
    if response.status_code == 200:
        # Generate a filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"temp/{timestamp}.jpg"
        
        # Save the image to the specified directory
        os.makedirs("temp", exist_ok=True)
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Image captured and saved to {filename}")
        return filename
    else:
        print("Failed to capture image from ESP32-CAM")
        return None

def compare_faces(captured_image_path):
    database_path = "registro_alumnos"
    recognized = False
    
    # Iterate through each person folder in the database
    for person_name in os.listdir(database_path):
        person_dir = os.path.join(database_path, person_name)
        
        if os.path.isdir(person_dir):
            # Iterate through each image file in the person's directory
            for img_file in os.listdir(person_dir):
                img_path = os.path.join(person_dir, img_file)
                
                # Compare the captured image with the current image in the database
                try:
                    result = DeepFace.verify(captured_image_path, img_path, enforce_detection=False)
                    if result["verified"]:
                        print(f"Person recognized as {person_name}")
                        recognized = True
                        # Mostramos los datos del usuario en NodeRED
                        part = person_name.split("_")

                        #Asignamos los datos correspondientes
                        nombre = part[0]
                        Apellido_P = part[1]
                        Apellido_M = part[2]
                        Matricula = part[3]

                        #Formato json para publicar
                        datos = json.dumps({"nom":nombre,"app":Apellido_P,"apm":Apellido_M,"mat":Matricula,"edo":"SALIDA"})
                        client.publish(topic,datos)
                        break
                except Exception as e:
                    print(f"Error comparing images: {e}")
                    continue
        
        if recognized:
            break
    
    if not recognized:
        print("Person not recognized in the database")
    
    # Capture the image from ESP32-CAM
captured_image_path = capture_image()
    
if captured_image_path:
    # Compare the captured image with the database
    compare_faces(captured_image_path)