import os
import random
import json
import time
from vocab_loader import load_vocab, get_all_words

# Constants
VOCAB_FILE = "beijing_zhongkao_vocab_21days.md"
PROGRESS_FILE = "vocab_progress.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"mistakes": [], "history": []}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=4, ensure_ascii=False)

def run_test(words, mode_name, progress):
    score = 0
    total = len(words)
    mistakes_in_session = []
    
    print(f"\n--- {mode_name} ---")
    print(f"Total words: {total}\n")
    
    for i, word_data in enumerate(words):
        print(f"[{i+1}/{total}] Meaning: {word_data['meaning']}")
        if word_data.get('example_en'):
             # Hide the target word in the example sentence slightly for hint
             # Simple replacement of the word with underscores, case insensitive
             target_word = word_data['word']
             example = word_data['example_en']
             # A simple naive replacement. Could be better with regex but sufficient for now.
             import re
             masked_example = re.sub(target_word, "____", example, flags=re.IGNORECASE)
             print(f"Example: {masked_example}")
             
        user_input = input("Enter word: ").strip()
        
        if user_input.lower() == word_data['word'].lower():
            print("✅ Correct!")
            score += 1
            # If word was in mistakes, ask if we should remove it? 
            # For now, let's keep it simple: if you get it right in Mistake Review, we remove it.
        else:
            print(f"❌ Wrong! The word was: {word_data['word']}")
            # Add to mistakes if not already there
            if word_data not in progress['mistakes']:
                 progress['mistakes'].append(word_data)
            mistakes_in_session.append(word_data)
        print("-" * 20)

    # End of test summary
    print(f"\nTest Complete!")
    print(f"Score: {score}/{total}")
    
    # Update history
    progress['history'].append({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "mode": mode_name,
        "score": score,
        "total": total
    })
    
    if mode_name == "Mistake Review":
        # Remove correctly answered words from mistakes list
        # Filter out words that were answered correctly (i.e., present in words but NOT in mistakes_in_session)
        # We use the 'word' string as the unique identifier to avoid issues with extra keys (like 'day')
        
        mistakes_in_session_words = set(m['word'] for m in mistakes_in_session)
        original_test_words = set(w['word'] for w in words)
        
        # We want to keep mistakes that were NOT in this test session
        # PLUS mistakes that were in this session AND failed again.
        # But easier: Just remove the ones we got right.
        # Ones we got right = generic_set(words) - generic_set(mistakes_in_session)
        
        corrected_words = original_test_words - mistakes_in_session_words
        
        # Rebuild progress['mistakes'] excluding the corrected words
        progress['mistakes'] = [
            m for m in progress['mistakes'] 
            if m['word'] not in corrected_words
        ]
    
    save_progress(progress)
    input("\nPress Enter to return to menu...")

def main_menu():
    progress = load_progress()
    vocab_data = load_vocab(VOCAB_FILE)
    
    while True:
        clear_screen()
        print("=== Beijing Zhongkao Vocab Trainer ===")
        print(f"Total Mistakes Pending: {len(progress['mistakes'])}")
        print("1. Unit Test (Select a Day)")
        print("2. Grand Test (All Words)")
        print("3. Mistake Review")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            day_keys = list(vocab_data.keys())
            print("\nAvailable Days:")
            for i, day in enumerate(day_keys):
                print(f"{i+1}. {day}")
            
            try:
                day_idx = int(input("Select Day number: ")) - 1
                if 0 <= day_idx < len(day_keys):
                    target_day = day_keys[day_idx]
                    words = vocab_data[target_day]
                    run_test(words, f"Unit Test ({target_day})", progress)
                else:
                    input("Invalid day selection. Press Enter...")
            except ValueError:
                input("Invalid input. Press Enter...")
                
        elif choice == '2':
            all_words = get_all_words(vocab_data)
            random.shuffle(all_words)
            # Optional: Limit grand test size? NO, user asked for "All words logic".
            run_test(all_words, "Grand Test", progress)
            
        elif choice == '3':
            if not progress['mistakes']:
                input("No mistakes recorded yet! Go do some tests first. Press Enter...")
            else:
                mistakes_to_test = list(progress['mistakes']) # Make a copy
                random.shuffle(mistakes_to_test)
                run_test(mistakes_to_test, "Mistake Review", progress)
                
        elif choice == '4':
            print("\n--- History ---")
            for h in progress['history'][-10:]: # Show last 10
                print(f"{h['timestamp']} - {h['mode']}: {h['score']}/{h['total']}")
            input("\nPress Enter...")
            
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    if not os.path.exists(VOCAB_FILE):
        print(f"Error: Vocab file '{VOCAB_FILE}' not found.")
    else:
        main_menu()
