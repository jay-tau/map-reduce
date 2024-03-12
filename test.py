import os

# Count 'to' in all files in titles

rolling_sum = 0

for i in range(1, 10):
    with open(os.path.join("titles", f"{i}.txt"), "r", encoding="utf-8") as f:
        word_count: dict[str, int] = {}
        for line in f:
            for word in line.split():
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        print(word_count.get("to", 0))
        rolling_sum += word_count.get("to", 0)

print()
print(rolling_sum)
