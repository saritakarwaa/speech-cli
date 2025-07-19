Speech Practice Analyzer CLI 🎤📊
https://img.shields.io/badge/python-3.8%252B-blue
https://img.shields.io/badge/License-MIT-yellow.svg

A command-line tool that helps you practice and improve public speaking or interview skills by recording your speech and providing AI-powered feedback on your performance.

Key Features ✨
Voice Recording: Capture your speech directly in the CLI

AI-Powered Transcription: Convert speech to text using OpenAI's Whisper

Performance Metrics: Get detailed feedback on:

Speaking pace (Words Per Minute)

Clarity score

Filler word count ("um", "like", "you know")

Vocabulary variety

Confidence indicators

Export Reports: Save feedback as Markdown or JSON files

Progress Tracking: View your improvement over time (history feature)

Tech Stack 🛠️
Python: Core language

PyAudio: Audio recording

OpenAI Whisper: Speech-to-text transcription

TextStat: Text analysis metrics

Rich: Terminal formatting

Usage 🚀
Record Your Speech
bash
python cli.py record --duration 30 --prompt "Tell me about yourself"
Creates WAV file in recordings/ directory

Analyze Your Recording
bash
python cli.py analyze recordings/1680000000.wav
Sample output:

text
📝 Transcription: "I'm a software engineer with experience in Python and machine learning"
📊 Feedback:
- WPM: 145.2
- Filler Count: 2
- Vocab Variety: 78.5%
- Clarity: 88.3%
- Confidence Score: 92.1%
Export Feedback Report
bash
# JSON format
python cli.py export recordings/1680000000.wav --format json

# Markdown format
python cli.py export recordings/1680000000.wav --format md
Reports saved to feedback/ directory

View Session History
bash
python cli.py history --limit 5
Output:

text
2023-10-15 14:30:00 — 142 WPM, clarity 85%
2023-10-14 09:15:00 — 135 WPM, clarity 82%
2023-10-13 16:45:00 — 128 WPM, clarity 79%