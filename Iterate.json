import json

conversation = []

for i, segment in enumerate(segments):
    audio, sample_rate = torchaudio.load(f"segment_{i}.wav")
    transcript = transcribe.transcribe_segment(model, audio)
    speaker = "caller" if i % 2 == 0 else "callee"
    conversation.append({"speaker": speaker, "transcript": transcript})

with open("conversation.json", "w") as json_file:
    json.dump(conversation, json_file, indent=4)
