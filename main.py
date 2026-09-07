import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 10  # segundos de gravação
sample_rate = 44100

print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse:", text)
    translator = Translator()
    translated = translator.translate(text, dest='en')
    print("🌍 Tradução para o inglês:", translated.text)

except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
    print("A fala não pôde ser reconhecida.")
except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
        print(f"Service error: {e}")

dest_language = input("Para qual idioma devo traduzir? (ex: 'fr' para francês, 'es' para espanhol, 'de' para alemão): ")
translator = Translator()
translated = translator.translate(text, dest=dest_language)
print(f"🌍 Tradução para {dest_language}:", translated.text)
