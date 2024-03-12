import json
import os
import sys
import time
from pprint import pprint as print

import requests

data_dir = os.path.join(os.getcwd(), "data")

if __name__ == "__main__":
    print("Starting...")
    time.sleep(
        5
    )  # Wait till the mapper servers are initialized in the respective containers

    for i in range(1, 10):
        response = requests.get(f"http://mapper{i}/count/{i}", timeout=10)

        if response.text.strip() == "0":
            continue
        else:
            print(response.text)
            print(type(response.text))
            sys.exit(1)

    global_word_count: dict[str, int] = {}

    for i in range(1, 10):
        with open(
            os.path.join(data_dir, "counts", f"{i}.json"), "r", encoding="utf-8"
        ) as f:
            word_count = json.load(f)
            for word, count in word_count.items():
                if word in global_word_count:
                    global_word_count[word] += count
                else:
                    global_word_count[word] = count

    with open(
        os.path.join(data_dir, "counts", "total_counts.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(global_word_count, f, indent=4, sort_keys=True)

    print("Finished.")
