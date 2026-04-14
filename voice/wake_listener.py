import pvporcupine, pyaudio, struct, wave
from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")
porcupine = pvporcupine.create(keywords=["jarvis"])

pa = pyaudio.PyAudio()
stream = pa.open(rate=16000, channels=1,
    format=pyaudio.paInt16, input=True, frames_per_buffer=512)

def listen():
    while True:
        pcm = stream.read(512)
        pcm = struct.unpack_from("h"*256, pcm)

        if porcupine.process(pcm) >= 0:
            return record()

def record():
    frames = [stream.read(1024) for _ in range(60)]
    with open("cmd.wav","wb") as f:
        f.write(b"".join(frames))

    seg,_ = model.transcribe("cmd.wav")
    return " ".join([s.text for s in seg])
