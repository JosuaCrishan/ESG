# Emotional Speech Generation using Coqui TTS

## Overview
Convert input text into a `.wav` file using **Coqui TTS (XTTS-v2)**.  
Supports multiple **emotions**: `neutral`, `happy`, `sad`, `angry`.

## Requirements
- Python 3.9+
- Install dependencies:
```bash
pip install TTS
```
Usage
Run:
```bash
python solution.py "Hello world, this is a neutral narration." neutral.wav neutral
```

With emotion:
```bash
python solution.py "I'm so excited to share this news!" excited.wav happy
```

Notes
Default voice: female-en-5.

You can change speaker to other available voices in XTTS-v2.
Supported emotions: neutral | happy | sad | angry.
Model: tts_models/multilingual/multi-dataset/xtts_v2
