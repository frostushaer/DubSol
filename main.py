# main.py

import argparse
from pathlib import Path
from audio_subtitle_extraction.audio_extraction import extract_audio
from audio_subtitle_extraction.subtitle_extraction import transcribe_audio
from dialogue_music_seperation.seperate import separate_audio
from character_profiling.diarize import diarize_dynamic_speakers

def main(video_path):
    audio_output_path = Path("data/audio_files")
    subtitle_output_path = Path("data/subtitles")
    speakers_output_path = Path("data/speakers")

    print("🔊 Extracting audio...")
    audio_path = extract_audio(video_path, audio_output_path)
    print(f"✅ Audio saved at {audio_path}")

    # Separating audio to get vocals-only (dialogue)
    print("🎛️ Separating audio...")
    vocals_audio_path, separated_audio_path = separate_audio(audio_path, audio_output_path)
    print(f"✅ Separated audio saved at {separated_audio_path}, vocals saved at {vocals_audio_path}")


    if vocals_audio_path:
        # Transcribing subtitles from the extracted vocals-only audio
        print("📝 Transcribing subtitles...")
        subtitle_file, detected_lang = transcribe_audio(str(vocals_audio_path), subtitle_output_path)
        print(f"✅ Subtitles saved at {subtitle_file}")
        print(f"🌐 Detected Language: {detected_lang}")

        # Profiling speakers
        print("🧑‍🤝‍🧑 Profiling speakers...")
        diarize_dynamic_speakers(str(vocals_audio_path), str(speakers_output_path))
        print(f"✅ Speaker profiles saved at {speakers_output_path}")
    else:
        print("❌ No vocals file found in the separated audio!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True, help="Path to input video file")
    args = parser.parse_args()
    main(args.video)
