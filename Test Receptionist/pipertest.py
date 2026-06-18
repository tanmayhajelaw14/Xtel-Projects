import wave
from piper import PiperVoice


voice = PiperVoice.load("en_US-lessac-medium.onnx")


with wave.open("test.wav","wb") as wav_file:
    voice.synthesize_wav(
        "Hello, Tapendra, welcome to the dental clinic. How can I assist you today? ",
        wav_file,
    )
print("Audio generated and saved as test.wav")