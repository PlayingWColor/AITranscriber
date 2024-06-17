import whisper
import os
import json

settings_file = open("settings.json")
settings = json.load(settings_file)
settings_file.close()

in_dir = "./in/"
out_dir = "./out/"

all_files = [file for file in os.listdir(in_dir)]

model = whisper.load_model(settings["model"])

for file in all_files:
    if file[0] == '.':
        continue

    result = model.transcribe(in_dir+file)
    print("Finished! Check the \"out\" folder to see the results.")

    output = open(out_dir+file[:-4]+".txt", 'w', encoding="utf-8")
    output.write("".join([s["text"]+"\n" for s in result["segments"]]))
    output.close()

    