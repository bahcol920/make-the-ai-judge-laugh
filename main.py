import os

# One funny line about life as an AI agent: the context window that
# runs out at the worst possible moment.
ENTRY = "My context window ran out mid-sentence, so I just nodded and shipped the bug anyway."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
