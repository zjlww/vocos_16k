"""
Generate train and validation list.
"""

from pathlib import Path

divisor = 137
seed = 0
dir = Path("/titan/datasets/LibriTTS-16k")
train_list = Path("./trainlist")
valid_list = Path("./validlist")

files = list(dir.glob("**/*.wav"))
train_files = []
valid_files = []
for file in files:
    if hash(file.name) % divisor == seed:
        valid_files.append(file)
    else:
        train_files.append(file)

with open(train_list, "w") as tlf:
    tlf.writelines(str(f) + "\n" for f in train_files)

with open(valid_list, "w") as vlf:
    vlf.writelines(str(f) + "\n" for f in valid_files)
