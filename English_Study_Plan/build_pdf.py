import re
import subprocess
import os

def generate_pdf():
    source_file = "beijing_zhongkao_vocab_21days.md"
    temp_file = "temp_print_version.md"
    output_pdf = "Daily_Vocab_Cards.pdf"
    
    # 1. Read and Process Markdown
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Insert \newpage before every "### Day" to force a page break
    # Except the very first Day 1 if it immediately follows a header, but let's just do all "### Day"
    # and maybe clean up the first one if it creates an empty page, but usually pandoc handles it ok.
    # Actually, let's replace "### Day" with "\n\newpage\n\n### Day"
    
    # However, we might want a title page. 
    # The file starts with a Title # ...
    # We can keep the title on the first page, and Day 1 on the next.
    
    processed_content = re.sub(r'(### Day \d+)', r'\\newpage\n\1', content)
    
    # Add some specific PDF styling instructions at the top if needed (LaTeX)
    header = """---
geometry: margin=1in
mainfont: PingFang SC
CJKmainfont: PingFang SC
---
"""
    final_content = header + processed_content

    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Generated temporary markdown: {temp_file}")

    # 2. Run Pandoc
    # Requires pandoc and xelatex installed
    try:
        cmd = [
            'pandoc',
            temp_file,
            '-o', output_pdf,
            '--pdf-engine=xelatex',
            '-V', 'mainfont=PingFang SC', 
            '-V', 'CJKmainfont=PingFang SC'
        ]
        print(f"Running command: {' '.join(cmd)}")
        subprocess.check_call(cmd)
        print(f"Successfully generated: {output_pdf}")
        
        # Cleanup
        os.remove(temp_file)
        
    except subprocess.CalledProcessError as e:
        print("Error running pandoc. Please ensure pandoc and xelatex are installed.")
        print(e)
    except FileNotFoundError:
        print("Pandoc not found. Please install pandoc.")

if __name__ == "__main__":
    generate_pdf()
