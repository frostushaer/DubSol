from moviepy import VideoFileClip
from pathlib import Path

def extract_audio(video_path, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_path = output_dir / "extracted_audio.wav"
    
    video = VideoFileClip(str(video_path))
    video.audio.write_audiofile(str(audio_path), codec='pcm_s16le')

    return str(audio_path)