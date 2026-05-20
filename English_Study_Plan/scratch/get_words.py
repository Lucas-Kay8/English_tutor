import re
import json

def get_words():
    filepath = "beijing_zhongkao_vocab_21days.md"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    day_pattern = re.compile(r'### (Day \d+):')
    word_pattern = re.compile(r'^\d+\.\s*\*\*(.*?)\*\*\s*-\s*(.*)')
    
    words_list = []
    current_day = None
    
    for line in lines:
        line = line.strip()
        day_match = day_pattern.search(line)
        if day_match:
            current_day = day_match.group(1)
            continue
            
        if current_day:
            day_num = int(current_day.replace("Day ", ""))
            if day_num >= 59 and day_num <= 80:
                word_match = word_pattern.match(line)
                if word_match:
                    words_list.append({
                        "day": current_day,
                        "word": word_match.group(1),
                        "meaning": word_match.group(2)
                    })
                    
    print(f"Total words in Day 59-80: {len(words_list)}")
    with open("scratch/day_59_80_words.json", "w", encoding="utf-8") as f:
        json.dump(words_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_words()
