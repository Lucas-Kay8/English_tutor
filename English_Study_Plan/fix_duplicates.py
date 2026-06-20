import re
import shutil

def fix_vocabulary_duplicates(filepath):
    # 1. 备份原始文件
    backup_path = filepath + ".fix_bak"
    shutil.copy(filepath, backup_path)
    print(f"✅ 已备份原始文件至 {backup_path}")

    # 2. 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. 按 Day 拆分内容
    # 我们用正则匹配 `### Day \d+:` 这样的标题
    day_sections = re.split(r'(### Day \d+:[^\n]*)', content)
    
    # 拆分后，day_sections[0] 是文件头部的说明，之后的部分是 标题 + 这一天的内容
    new_content_parts = [day_sections[0]]
    
    for i in range(1, len(day_sections), 2):
        day_title = day_sections[i]
        day_body = day_sections[i+1] if i+1 < len(day_sections) else ""
        
        # 处理这一天的单词
        fixed_body = process_day_body(day_title, day_body)
        new_content_parts.append(day_title)
        new_content_parts.append(fixed_body)

    # 4. 写回原文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("".join(new_content_parts))
    print(f"✅ 成功完成去重并写回文件 {filepath}")

def process_day_body(title, body):
    # 解析这一天的单词
    lines = body.split('\n')
    
    # 一个单词条目由一个单词行和若干行例句组成
    # 我们可以通过扫描行来将它们组合为独立的 entry
    entries = []
    current_entry = None
    
    word_pattern = re.compile(r'^\d+\.\s*\*\*(.*?)\*\*\s*-\s*(.*)')
    
    for line in lines:
        stripped = line.strip()
        word_match = word_pattern.match(stripped)
        
        if word_match:
            # 发现新的单词行
            if current_entry:
                entries.append(current_entry)
            word = word_match.group(1).strip()
            meaning = word_match.group(2).strip()
            current_entry = {
                "word": word,
                "meaning": meaning,
                "lines": [line]  # 保留原始行格式，以便写回时格式不失真
            }
        else:
            if current_entry:
                # 认为是例句或者描述行，追加到当前 entry
                current_entry["lines"].append(line)
            else:
                # 单词列表开始之前的空白行或过渡行，直接作为空 entry 处理
                entries.append({"word": None, "lines": [line]})
                
    if current_entry:
        entries.append(current_entry)
        
    # 开始对 entries 进行去重和重新编号
    seen_words = set()
    unique_entries = []
    word_counter = 1
    
    for entry in entries:
        word = entry.get("word")
        if word is None:
            # 这一行没有单词（通常是空行或说明行），直接保留
            unique_entries.append(entry)
        else:
            # 统一转为小写去重
            lower_word = word.lower()
            if lower_word not in seen_words:
                seen_words.add(lower_word)
                # 重新编号
                # 原始行是类似 "1. **word** - meaning"
                # 我们用正则把最前面的数字替换为新的 counter
                raw_lines = entry["lines"]
                # 替换第一行
                first_line = raw_lines[0]
                # 找到最前方的 "数字." 并替换为 "word_counter."
                new_first_line = re.sub(r'^\s*\d+\.', f"{word_counter}.", first_line)
                raw_lines[0] = new_first_line
                
                unique_entries.append(entry)
                word_counter += 1
            else:
                # 如果是重复单词，丢弃，不加入 unique_entries
                # 注意：我们也同时丢弃了它的例句（也就是 entry["lines"] 里的其他行）
                pass
                
    # 重新拼装为 body
    new_body_lines = []
    for entry in unique_entries:
        new_body_lines.extend(entry["lines"])
        
    return "\n".join(new_body_lines)

if __name__ == "__main__":
    fix_vocabulary_duplicates("beijing_zhongkao_vocab_21days.md")
