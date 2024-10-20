import whisper

model = whisper.load_model("large")
audio_file = r"C:\Users\Jeppe\Documents\Transcription\limfjordsbroen\Limfjordsbroen.m4a"

import json

for i in range(len(groups)):

    result = model.transcribe(
        audio=audio_file, language="dk", word_timestamps=True
    )  # , initial_prompt=result.get('text', ""))
    with open(str(i) + ".json", "w") as outfile:
        json.dump(result, outfile, indent=4)
