import os
import base64
from PIL import Image

def main():
    src_path = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/static/icon.png"
    dest_path = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/static/icon_apple.png"
    
    if not os.path.exists(src_path):
        print(f"Error: {src_path} not found!")
        return
        
    try:
        # 打开原始 512x512 图标并压缩为 iOS 推荐的 180x180 规格
        img = Image.open(src_path)
        img_resized = img.resize((180, 180), Image.Resampling.LANCZOS)
        
        # 优化并保存为较小体积的 PNG
        img_resized.save(dest_path, "PNG", optimize=True)
        print(f"Successfully resized and saved to {dest_path}")
        
        # 读取并转为 Base64
        with open(dest_path, "rb") as f:
            encoded_bytes = base64.b64encode(f.read())
            encoded_str = encoded_bytes.decode('utf-8')
            
        print("\nBase64 length:", len(encoded_str))
        # 打印前 100 和后 100 字符
        print("Base64 preview:")
        print(encoded_str[:100] + "..." + encoded_str[-100:])
        
        # 写入临时文本文件，以便复制
        txt_path = "/Users/lucas/Work/09.Antigravity/Oli/English_Study_Plan/scratch/icon_base64.txt"
        with open(txt_path, "w") as f_out:
            f_out.write(encoded_str)
        print(f"Base64 string written to {txt_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
