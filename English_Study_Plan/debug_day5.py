from vocab_loader import load_vocab

data = load_vocab("beijing_zhongkao_vocab_21days.md")
if "Day 5" in data:
    print("Day 5 words:")
    for w in data["Day 5"]:
        print(f"'{w['word']}' codes: {[c.encode('unicode_escape') for c in w['word']]}")
else:
    print("Day 5 not found!")
