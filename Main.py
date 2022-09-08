import sounddevice
import scipy.io.wavfile
from scipy.io.wavfile import write

fs = 44100

time = int(input("How long do you want to record? (Example: 1 min and 50 secs would be 1.50)")) #3 mins and 20 secs would be 3.20
intoseconds = time * 60
filename = input("Name of the file? (End it with .wav")
print("Now recording")
voicefile = sounddevice.rec(int(intoseconds*fs),samplerate=fs,channels=2)
sounddevice.wait()
write(filename,fs,voicefile)
print("Process done")