from vocab_loader import load_vocab
data = load_vocab("beijing_zhongkao_vocab_21days.md")
print(f"Loaded keys: {list(data.keys())}")
