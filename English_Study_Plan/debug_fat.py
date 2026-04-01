from vocab_loader import load_vocab

data = load_vocab("beijing_zhongkao_vocab_21days.md")
found = False
for day, words in data.items():
    for w in words:
        if "fat" in w['word'].lower():
            print(f"Found: {repr(w['word'])}")
            print(f"Hex: {[hex(ord(c)) for c in w['word']]}")
            found = True

if not found:
    print("Word 'fat' not found in vocab.")
