import numpy as np
import sounddevice as sd
from pythonosc import udp_client

# Configura el client OSC per comunicar-se amb Wekinator
client = udp_client.SimpleUDPClient("127.0.0.1", 6448)  # 127.0.0.1 és el localhost i 6448 és el port per defecte de Wekinator

# Paràmetres de captura d'àudio
samplerate = 44100  # Taxa de mostreig (samples per segon)
channels = 1        # Canals (1 per mono, 2 per estéreo)
duration = 0.1      # Durada de la captura (en segons) - capturar una mica de temps de so en cada bucle

# Funció per obtenir el volum del micròfon
def get_volume(indata):
    # Calcula el volum com la norma de les mostres (amplitud del senyal)
    volume_norm = np.linalg.norm(indata) * 10  # Multiplicat per 10 per augmentar el rang del volum
    return volume_norm

# Funció per capturar l'àudio i enviar el volum a Wekinator
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # Calcula el volum del senyal d'àudio
    volume = get_volume(indata)
    
    # Envia el volum a Wekinator a través de OSC
    client.send_message("/wek/inputs", [volume])  # Envia com a missatge OSC

    # Mostra el volum (per controlar que tot està funcionant)
    print(f"Volum: {volume:.2f}")

# Captura l'àudio en temps real
with sd.InputStream(callback=audio_callback, channels=channels, samplerate=samplerate):
    print("Capturant àudio... Prem Ctrl+C per aturar.")
    while True:
        pass  # Deixa el flux d'àudio treballant en segon pla
