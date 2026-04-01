import re
import sys
import os

print("Starting debug script...", file=sys.stderr)
filepath = "beijing_zhongkao_vocab_21days.md"
if not os.path.exists(filepath):
    print(f"File not found: {filepath}", file=sys.stderr)
    sys.exit(1)

print(f"File exists: {filepath}", file=sys.stderr)

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines.", file=sys.stderr)

day_pattern = re.compile(r'### (Day \d+):')

print("Tracing Day headers:", file=sys.stderr)
found_days = []
for i, line in enumerate(lines):
    line = line.strip()
    match = day_pattern.search(line)
    if match:
        print(f"Line {i+1}: Matched '{match.group(1)}'", file=sys.stderr)
        found_days.append(match.group(1))

if "Day 5" not in found_days:
    print("FATAL: Day 5 not detected!", file=sys.stderr)
else:
    print("Day 5 detected.", file=sys.stderr)
