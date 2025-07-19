# import whisper

# model = whisper.load_model("base")

# def transcribe(audio_path: str):
#     result = model.transcribe(audio_path)
#     text = result['text']
#     confidences = [seg.get('avg_logprob', 0) for seg in result.get('segments', [])]
#     return text, confidences

# speech_cli/transcriber.py
import speech_recognition as sr

def transcribe(audio_path: str):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, show_all=False)
            return text, [1.0]  # Using max confidence for testing
        except sr.UnknownValueError:
            print("⚠️ Could not understand audio")
            return "", [0.0]
        except sr.RequestError as e:
            print(f"⚠️ API error: {str(e)}")
            return "", [0.0]