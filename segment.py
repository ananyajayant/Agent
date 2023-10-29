from pydub import AudioSegment
from pydub.playback import play

# Load the audio file
audio = AudioSegment.from_file("conversation.mp3")

# Split the audio into segments of 10 seconds (adjust as needed)
segment_duration = 10 * 1000  # 10 seconds in milliseconds
segments = [audio[i:i + segment_duration] for i in range(0, len(audio), segment_duration)]

# Play or save the segments as needed
for i, segment in enumerate(segments):
    segment.export(f"segment_{i}.wav", format="wav")
