from vocab_loader import load_vocab

data = load_vocab("beijing_zhongkao_vocab_21days.md")
found = False
for day, words in data.items():
    for w in words:
        if "pay" in w['word']:
            print(f"Found: {repr(w['word'])}")
            print(f"Hex: {[hex(ord(c)) for c in w['word']]}")
            found = True

if not found:
    print("Word 'pay' not found in vocab.")
