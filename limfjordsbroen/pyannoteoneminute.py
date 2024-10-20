from pyannote.audio import Pipeline

from config import HF_AUTH_TOKEN  # Hidden for anonymity

use_auth_token = HF_AUTH_TOKEN

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=use_auth_token,
)

# send pipeline to GPU (when available)
import torch

pipeline.to(torch.device("cuda"))

# specify the audio file
audio_file = r"C:\Users\Jeppe\Documents\Transcription\limfjordsbroen\Limfjordsbroen.wav"

# apply pretrained pipeline
diarization = pipeline(audio_file)

# create the output filename based on the input audio file
output_filename = f"speaker_turns_{audio_file.split('\\')[-1].split('.')[0]}.tsv"

with open(output_filename, "w") as file:
    # Write the header
    file.write("start\tend\ttext\n")

    # Iterate through the diarization tracks
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        # Format the string
        output = f"{turn.start:.1f}\t{turn.end:.1f}\tspeaker_{speaker}\n"
        # Print to console (optional)
        print(output.strip())
        # Write to the file
        file.write(output)
