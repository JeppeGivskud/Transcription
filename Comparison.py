import csv
from Names import Speaker1, Speaker2  # Hidden for anonymity

# Read speaker turns from speaker_turns_Limfjordsbroen.tsv
speaker_turns = []
with open("speaker_turns_Limfjordsbroen.tsv", "r") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        speaker = row["text"]
        if speaker == "speaker_SPEAKER_02":
            speaker = Speaker1
        elif speaker == "speaker_SPEAKER_01":
            speaker = Speaker2
        speaker_turns.append(
            {
                "start": float(row["start"]) * 1000,  # Convert to milliseconds
                "end": float(row["end"]) * 1000,  # Convert to milliseconds
                "speaker": speaker,
            }
        )

# Read text intervals from Limfjordsbroen.tsv
text_intervals = []
with open("Limfjordsbroen.tsv", "r") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        text_intervals.append(
            {"start": int(row["start"]), "end": int(row["end"]), "text": row["text"]}
        )

with open("combined_output.tsv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["speaker", "start", "end", "text"])

    for text_interval in text_intervals:
        closest_speaker = None
        min_distance = float("inf")

        for speaker_turn in speaker_turns:
            if (
                speaker_turn["start"] <= text_interval["start"] < speaker_turn["end"]
            ) or (speaker_turn["start"] < text_interval["end"] <= speaker_turn["end"]):
                # Calculate the distance to the start and end times
                distance = min(
                    abs(speaker_turn["start"] - text_interval["start"]),
                    abs(speaker_turn["end"] - text_interval["end"]),
                )

                if distance < min_distance:
                    min_distance = distance
                    closest_speaker = speaker_turn["speaker"]

        if closest_speaker:
            writer.writerow(
                [
                    closest_speaker,
                    text_interval["start"],
                    text_interval["end"],
                    text_interval["text"],
                ]
            )
