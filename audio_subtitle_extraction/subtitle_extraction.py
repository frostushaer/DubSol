import whisper
from pathlib import Path
from whisper.utils import get_writer

model = whisper.load_model("base")

def transcribe_audio(audio_path, output_dir, output_format="srt"):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Transcribe using whisper
    result = model.transcribe(str(audio_path))

    # Write subtitle file using the writer
    writer = get_writer(output_format, output_dir)
    writer(result, audio_path)

    # Output subtitle path
    subtitle_path = output_dir / f"{Path(audio_path).stem}.{output_format}"
    
    return str(subtitle_path), result["language"]
