# Extractor de característiques per Wekinator / Feature Extractor for Wekinator

Aquest projecte és un extractor de característiques per Wekinator. Utilitza dades en temps real del micròfon i les envia via OSC al port 6448 per a l'entrenament de models a Wekinator.

This project is a feature extractor for Wekinator. It uses real-time microphone data and sends it via OSC to port 6448 for model training in Wekinator.

## Com executar-lo / How to run it

1. Assegura't de tenir Python instal·lat.
   Make sure you have Python installed.
   
2. Instal·la les dependències necessàries / Install the required dependencies:
pip install python-osc sounddevice numpy

3. Executa el fitxer Python / Run the Python file: 
python envia_volum.py

4. Obre Wekinator i selecciona el port 6448.
Open Wekinator and select port 6448.



