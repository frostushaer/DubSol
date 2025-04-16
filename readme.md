# 🎙️ DubSol: Multilingual Emotion-Preserving Voice Cloning & Dubbing Tool

DubSol is a fully open-source pipeline that takes a video and a desired output language, and generates a dubbed version while:
- Separating vocals from music
- Transcribing the dialogue
- Profiling characters by voice
- Preparing for realistic voice cloning in multiple languages

## ✅ Features Completed

### 1. 🎞️ Extract Audio from Video
- Extracts high-quality audio from any input video file.

### 2. 📝 Subtitle Transcription (Optional for now)
- Uses Whisper to transcribe audio and detect language.
- (Disabled temporarily in `main.py`, can be uncommented when needed.)

### 3. 🎛️ Dialogue & Music Separation
- Uses Demucs to separate dialogue (vocals) and background music.
- Stores vocals for use in transcription and speaker profiling.

### 4. 🧑‍🤝‍🧑 Speaker Diarization
- Uses Resemblyzer and KMeans clustering to identify dynamic number of speakers.
- Creates separate profiles for each character based on vocal embeddings.

## Setup environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

---

## To run 

python .\DubSol\main.py --video .\inputs\test.mp4 

---

## 🧩 Features Yet to Come

- 🗣️ **Voice Cloning**: Clone the speaker's voice to preserve tone and personality.
- 🌍 **Multilingual Speech Generation**: Translate subtitles and speak them in the original speaker's cloned voice.
- 🎭 **Emotion Preservation**: Analyze emotions from the original voice and reflect them in the cloned speech.
- 🔁 **Dialogue Replacement**: Replace original dialogue with dubbed version while keeping the background music.
- 🎚️ **Audio Mixing**: Merge the dubbed voices with preserved background music.
- 📼 **Final Video Export**: Recombine video with dubbed audio into a finished output file.
- 🛠️ **Web Interface / GUI**: Optional control panel to upload video, select target language, and download output.

---

## 🚫 Cons

- 🧠 **Memory & Processing Intensive**  
  Character profiling (diarization) especially consumes a lot of memory and time.

- 🪟 **Limited Windows Compatibility**  
  Many audio diarization models like `pyannote.audio` and `SpeechBrain` do not work natively on Windows.

- 📦 **Low Portability**  
  Due to heavy dependencies and GPU reliance, the solution isn’t easy to deploy on all systems.

- ⏳ **Slow Processing**  
  Overall runtime may take **~5x the original video length**, depending on system specs and model sizes.

- 🧏 **Subtitle Inaccuracy with Mixed Noises**  
  Auto subtitling can confuse language detection and transcription accuracy when the input audio contains mixed or unclear sounds.

---

---

Let me know if you'd like a version with emojis stripped or tailored for GitHub Pages. Want me to generate a `requirements.txt` based on the current modules?
