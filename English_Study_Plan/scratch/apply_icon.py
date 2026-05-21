import os

def main():
    base64_path = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/scratch/icon_base64.txt"
    html_path = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/templates/index.html"
    
    if not os.path.exists(base64_path):
        print(f"Error: {base64_path} not found!")
        return
    if not os.path.exists(html_path):
        print(f"Error: {html_path} not found!")
        return
        
    with open(base64_path, "r", encoding="utf-8") as f:
        base64_content = f.read().strip()
        
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    target = '<link rel="apple-touch-icon" href="/static/icon.png">'
    replacement = f'<link rel="apple-touch-icon" href="data:image/jpeg;base64,{base64_content}">'
    
    if target in html_content:
        new_html_content = html_content.replace(target, replacement)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_html_content)
        print("Successfully replaced apple-touch-icon in index.html with inline Base64!")
    else:
        # 看看是不是已经存在 data:image 的 apple-touch-icon 了，如果是，做一下提示或者也可以重新替换。
        if 'link rel="apple-touch-icon" href="data:image' in html_content:
            print("Warning: An inline base64 apple-touch-icon is already present in index.html.")
        else:
            print("Error: Target tag not found in index.html. Check if already modified or dynamic.")

if __name__ == "__main__":
    main()
