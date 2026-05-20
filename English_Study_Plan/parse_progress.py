import json
from datetime import datetime

file_path = '/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/vocab_progress.json'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Let's inspect what keys are available
    print("Keys in vocab_progress.json:", data.keys())
    
    if 'history' in data:
        # Check history for today's date
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"Looking for history for {today}...")
        # Since I don't know the exact format of history, I'll print the last few entries
        print("Last 3 history entries:", data['history'][-3:] if isinstance(data['history'], list) else "Not a list")
        
    if 'dailyStats' in data:
        print("Daily Stats:", list(data['dailyStats'].items())[-3:])
        
    # Just to get an idea of the structure:
    for key, val in data.items():
        if isinstance(val, dict):
            print(f"Key: {key}, type: dict, keys: {list(val.keys())[:5]}")
        elif isinstance(val, list):
            print(f"Key: {key}, type: list, length: {len(val)}")
        else:
            print(f"Key: {key}, type: {type(val)}, value: {val}")

except Exception as e:
    print("Error:", e)
