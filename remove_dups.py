import os
import re

files_to_process = [
    "Day1/Day1_Interview_Questions.txt",
    "Day1/InterviewQuestions.txt",
    "Day2/Day2_Interview_Questions.txt",
    "Day3/Day3_Interview_Questions.txt",
    "Day4/Day4_Interview_Questions.txt",
    "Day5/Day5_Interview_Questions.txt",
    "Day6/Day6_Interview_Questions.txt",
    "Day7/Day7_Interview_Questions.txt",
    "Master_Interview_Questions.txt"
]

seen_questions = set()
total_removed = 0

for rel_path in files_to_process:
    filepath = os.path.join(".", rel_path)
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        q_match = re.match(r'^(Q\d+):\s*(.*)', line)
        if q_match:
            q_num = q_match.group(1)
            q_text = q_match.group(2).strip()
            normalized_q = q_text.lower()
            
            # collect the whole Q&A block
            block = [line]
            i += 1
            while i < len(lines) and not re.match(r'^Q\d+:\s*', lines[i]) and not lines[i].startswith('---'):
                if lines[i].strip() != '' or (i + 1 < len(lines) and not re.match(r'^Q\d+:\s*', lines[i+1]) and not lines[i+1].startswith('---')):
                    # Keep empty lines only if they aren't the last line before the next question, 
                    # wait, simpler: just collect lines
                    pass
                block.append(lines[i])
                i += 1
                
            # Pop trailing empty lines from the block
            while block and block[-1].strip() == '':
                block.pop()
                
            if normalized_q not in seen_questions:
                seen_questions.add(normalized_q)
                new_lines.extend(block)
                new_lines.append('') # Add an empty line after the block
            else:
                total_removed += 1
                
            continue
            
        new_lines.append(line)
        i += 1

    # Clean up multiple consecutive empty lines
    cleaned_lines = []
    for line in new_lines:
        if cleaned_lines and cleaned_lines[-1].strip() == '' and line.strip() == '':
            continue
        cleaned_lines.append(line)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_lines))

print(f"Total unique questions kept: {len(seen_questions)}")
print(f"Total duplicates removed: {total_removed}")
