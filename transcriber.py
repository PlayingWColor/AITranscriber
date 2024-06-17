import whisper
import os

in_dir = "./in/"
out_dir = "./out/"

all_files = [file for file in os.listdir(in_dir)]

#print(all_files)

model = whisper.load_model("base")

for file in all_files:
    result = model.transcribe(in_dir+file)
    print(result["text"])

    output = open(out_dir+file[:-4]+".txt", 'w', encoding="utf-8")
    output.write("".join([s["text"]+"\n" for s in result["segments"]]))
    output.close()

    