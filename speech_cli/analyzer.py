import re
import numpy as np

FILLERS = re.compile(r"\b(um|uh|like|you know)\b", re.IGNORECASE)

def analyze(text: str, confidences: list, duration_sec: int):
    words = re.findall(r"\w+", text)
    total = len(words)
    mins = duration_sec / 60
    wpm = total / mins if mins else 0
    fillers = len(FILLERS.findall(text))
    vocab_variety = len(set(words)) / total if total else 0
    avg_conf = float(np.mean(confidences)) if confidences else 0
    clarity = float(np.tanh(avg_conf)) * 100
    conf_var = float(np.std(confidences)) if confidences else 0
    confidence_score = max(0, 100 - conf_var * 10)
    return {
        'wpm': round(wpm,1),
        'filler_count': fillers,
        'vocab_variety': round(vocab_variety*100,1),
        'clarity': round(clarity,1),
        'confidence_score': round(confidence_score,1)
    }