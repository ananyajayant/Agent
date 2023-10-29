import torch
import torchaudio
from whisper.asr import transcribe

# Load the Whisper ASR model
model = transcribe.load_model("whisper-large-lv60.pt")
model.eval()

# Load an audio segment
audio, sample_rate = torchaudio.load("segment_0.wav")

# Transcribe the audio segment
transcript = transcribe.transcribe_segment(model, audio)

print("Transcript:", transcript)
