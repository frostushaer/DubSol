# steps/character_profiling/diarize_resemblyzer_dynamic.py

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from resemblyzer import VoiceEncoder, preprocess_wav
import librosa
from pathlib import Path
from pydub import AudioSegment
import matplotlib.pyplot as plt

def estimate_optimal_speakers(embeds, max_speakers=6):
    scores = []
    for k in range(2, max_speakers + 1):
        kmeans = KMeans(n_clusters=k)
        labels = kmeans.fit_predict(embeds)
        score = silhouette_score(embeds, labels)
        scores.append(score)
    
    best_k = np.argmax(scores) + 2
    print(f"📊 Estimated number of speakers: {best_k}")
    return best_k

def diarize_dynamic_speakers(audio_path, output_dir, max_speakers=6):
    audio_path = Path(audio_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("🔊 Loading audio...")
    wav, _ = librosa.load(audio_path, sr=16000)
    encoder = VoiceEncoder()

    print("🧠 Getting speaker embeddings...")
    _, cont_embeds, wav_slices = encoder.embed_utterance(wav, return_partials=True, rate=16)

    print("🤖 Estimating number of speakers...")
    num_speakers = estimate_optimal_speakers(cont_embeds, max_speakers)

    print(f"👥 Clustering into {num_speakers} speakers...")
    kmeans = KMeans(n_clusters=num_speakers)
    labels = kmeans.fit_predict(cont_embeds)

    audio = AudioSegment.from_wav(audio_path)
    speaker_segments = {f"speaker_{i}": [] for i in range(num_speakers)}

    for label, (start, end) in zip(labels, wav_slices):
        start_ms = int(start * 1000)
        end_ms = int(end * 1000)
        segment = audio[start_ms:end_ms]

        speaker_name = f"speaker_{label}"
        speaker_dir = output_dir / speaker_name
        speaker_dir.mkdir(parents=True, exist_ok=True)

        count = len(list(speaker_dir.glob("*.wav")))
        segment.export(speaker_dir / f"{count+1:03}.wav", format="wav")

        speaker_segments[speaker_name].append((start, end))

    print(f"✅ Diarization complete. {num_speakers} speakers identified.")
    return speaker_segments
