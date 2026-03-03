import pandas as pd
from config import DATA_PATH

files = [
    "Occupation Data.txt",
    "Skills.txt",
    "Knowledge.txt",
    "Education, Training, and Experience.txt"
]

for file in files:
    print("\n" + "=" * 60)
    print(f"FILE: {file}")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH / file, sep="\t")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())