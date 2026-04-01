import re

def load_vocab(filepath):
    """
    Parses the vocabulary markdown file.
    
    Args:
        filepath (str): Path to the markdown file.
        
    Returns:
        dict: A dictionary where keys are Day strings (e.g., "Day 1") and values are lists of word dictionaries.
              Each word dictionary contains: 'word', 'meaning', 'example_en', 'example_cn'.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Vocabulary file not found at {filepath}")
        return {}

    vocab_data = {}
    current_day = None
    
    # Split content by lines to process line by line
    lines = content.split('\n')
    
    day_pattern = re.compile(r'### (Day \d+):')
    # Regex to capture word line: "1. **word** - meaning"
    word_pattern = re.compile(r'^\d+\.\s*\*\*(.*?)\*\*\s*-\s*(.*)')
    example_pattern = re.compile(r'^\*\s*\*(.+)\*\s*\((.+)\)\s*$')

    current_words = []
    
    for line in lines:
        line = line.strip()
        
        # Check for Day header
        day_match = day_pattern.search(line)
        if day_match:
            if current_day:
                vocab_data[current_day] = current_words
            current_day = day_match.group(1)
            current_words = []
            continue
            
        # Check for Word line
        word_match = word_pattern.match(line)
        if word_match and current_day:
            word = word_match.group(1)
            meaning = word_match.group(2)
            current_words.append({
                'word': word,
                'meaning': meaning,
                'example_en': '',
                'example_cn': ''
            })
            continue
            
        # Check for Example line
        # Examples usually follow the word immediately.
        # We assign it to the last added word.
        if current_words:
            example_match = example_pattern.match(line)
            if example_match:
                example_en = example_match.group(1).strip()
                example_cn = example_match.group(2).strip()
                current_words[-1]['example_en'] = example_en
                current_words[-1]['example_cn'] = example_cn

    # Add the last day
    if current_day:
        vocab_data[current_day] = current_words
        
    return vocab_data

def get_all_words(vocab_data):
    """
    Flattens the vocab data into a single list of all words.
    """
    all_words = []
    for day, words in vocab_data.items():
        for word in words:
            # Add 'day' info to the word dict for context if needed
            word_with_info = word.copy()
            word_with_info['day'] = day
            all_words.append(word_with_info)
    return all_words

if __name__ == "__main__":
    # Simple test
    import sys
    
    # Allow passing file path as argument, otherwise default to known path (for testing)
    filepath = "beijing_zhongkao_vocab_21days.md"
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        
    try:
        data = load_vocab(filepath)
        print(f"Successfully loaded {len(data)} days.")
        total_words = len(get_all_words(data))
        print(f"Total words found: {total_words}")
        
        # Print first day's first word as sample
        if data:
            first_day = list(data.keys())[0]
            print(f"\nSample from {first_day}:")
            if data[first_day]:
                print(data[first_day][0])
            else:
                print("No words in first day.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
