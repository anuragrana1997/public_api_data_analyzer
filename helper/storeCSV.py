import csv
from pathlib import Path

def storeInCSV(data):
    BASE_DIR = Path(__file__).resolve().parent.parent
    filePath = BASE_DIR / "storage" / "data.csv"
    with open(filePath, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "firstName", "lastName", "maidenName", "age", "gender"],
            extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(data)