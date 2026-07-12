import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

duration = 5
sample_rate = 44100

print("Speak now...")

audio = sd.rec(int(duration * sample_rate),
               samplerate=sample_rate,
               channels=1,
               dtype='int16')

sd.wait()

write("recording.wav", sample_rate, audio)

print("Converting speech to text...")

model = WhisperModel("base")

segments, info = model.transcribe("recording.wav")

for segment in segments:
    print("You said:", segment.text)