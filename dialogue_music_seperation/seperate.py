# separate.py
import torch
from demucs.pretrained import get_model
from demucs.apply import apply_model
from demucs.audio import convert_audio
import torchaudio
import torchaudio.transforms as T
import os
from pathlib import Path

def separate_audio(audio_path, output_dir):
    audio_path = Path(audio_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("🎛️ Loading Demucs model...")
    model = get_model(name="htdemucs")
    model.cpu()

    print("🎧 Loading audio...")
    wav, sr = torchaudio.load(str(audio_path))
    wav = convert_audio(wav, sr, model.samplerate, model.audio_channels)
    wav = wav.unsqueeze(0)

    print("🔄 Separating sources...")
    with torch.no_grad():
        sources = apply_model(model, wav, device="cpu")[0]

    stems = model.sources
    for source, name in zip(sources, stems):
        out_path = output_dir / f"{audio_path.stem}_{name}.wav"
        torchaudio.save(str(out_path), source, model.samplerate)
        print(f"✅ Saved {name} to {out_path}")

    vocals_path = output_dir / f"{audio_path.stem}_vocals.wav"
    if not vocals_path.exists():
        raise FileNotFoundError("❌ vocals.wav not found!")

    return str(vocals_path), str(output_dir)
