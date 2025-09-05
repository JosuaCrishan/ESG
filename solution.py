import sys
from pathlib import Path
from TTS.api import TTS

def main():
    if len(sys.argv) != 4:
        print("Usage: python solution.py \"<text>\" <output.wav> <emotion>")
        print("Available emotions: neutral | happy | sad | angry")
        sys.exit(1)

    text = sys.argv[1]
    output_path = Path(sys.argv[2])
    emotion = sys.argv[3].lower()

    if not text.strip():
        print("Error: Text input cannot be empty.")
        sys.exit(1)

    if output_path.suffix.lower() != ".wav":
        print("Error: Output file must have .wav extension.")
        sys.exit(1)

    if emotion not in ["neutral", "happy", "sad", "angry"]:
        print("Error: Unsupported emotion. Use: neutral | happy | sad | angry")
        sys.exit(1)

    try:
        print("Loading Coqui TTS model (XTTS-v2)...")
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

        print(f"Generating speech in '{emotion}' style...")
        tts.tts_to_file(
            text=text,
            file_path=str(output_path),
            speaker="female-en-5",   
            emotion=emotion
        )

        print(f"Saved output to {output_path}")

    except Exception as e:
        print(f"Error during synthesis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
