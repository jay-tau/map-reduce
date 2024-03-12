import json
import os
from datetime import datetime

from fastapi import FastAPI, HTTPException, status

data_dir = os.path.join(os.getcwd(), "data")

app = FastAPI()


@app.get("/")
def read_root():
    return {"current_time": datetime.now()}


@app.get("/count/{file_num}")
def counter(file_num: int = 0):
    with open(
        os.path.join(data_dir, "titles", f"{file_num}.txt"), "r", encoding="utf-8"
    ) as f:
        word_count: dict[str, int] = {}
        for line in f:
            for word in line.split():
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Write the dict to a JSON file
    with open(
        os.path.join(data_dir, "counts", f"{file_num}.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(word_count, f, indent=4, sort_keys=True)

    return 0
