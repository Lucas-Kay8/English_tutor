import sys
from vocab_loader import load_vocab

print("Loading vocabulary...", file=sys.stderr)
data = load_vocab("beijing_zhongkao_vocab_21days.md")

if "Day 5" in data:
    print("Day 5 words:", file=sys.stderr)
    for w in data["Day 5"]:
        print(f"Word: {repr(w['word'])} | Codes: {[ord(c) for c in w['word']]}", file=sys.stderr)
else:
    print("FATAL: Day 5 not in data!", file=sys.stderr)
