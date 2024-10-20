import whisper

# Load the model
model = whisper.load_model("turbo")

# Correct file path
audio_file = r"C:\Users\Jeppe\Documents\Transcription\audio.mp3"
print(audio_file)
# Transcribe the audio file
try:
    result = model.transcribe(audio_file, language="Danish")
    print(f"Transcription for {audio_file}:")
    print(result["text"])
except FileNotFoundError as e:
    print(f"Skipping {audio_file} due to FileNotFoundError: {e}")
