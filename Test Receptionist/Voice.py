import wave 
import winsound
from piper import PiperVoice


voice = PiperVoice.load("en_US-lessac-medium.onnx")


def speak(text):
    with wave.open("output.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    winsound.PlaySound("output.wav", winsound.SND_FILENAME)    