import wave
import pyaudio

def record(output_path: str, duration: int = 30):
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    frames = []
    for _ in range(0, int(16000 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    pa.terminate()
    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))