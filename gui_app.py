import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import cv2
from PIL import Image
from ascii_to_img import _convert_ascii_to_img
from img_to_ascii import _convert_img_to_ascii
from ascii_art import convert_mul

OUTPUT_DIR = 'output_ascii'
RESTORED_DIR = 'restored_images'
VIDEO_OUT_DIR = 'ascii_videos'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RESTORED_DIR, exist_ok=True)
os.makedirs(VIDEO_OUT_DIR, exist_ok=True)

def process_image(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    ascii_str = _convert_img_to_ascii(img)

    base_name = os.path.basename(filepath)
    name_no_ext = os.path.splitext(base_name)[0]
    out_path = os.path.join(OUTPUT_DIR, f"{name_no_ext}.txt")

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(ascii_str)

    return out_path

def process_ascii_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        ascii_str = f.read()
    image = _convert_ascii_to_img(ascii_str)

    base_name = os.path.basename(filepath)
    name_no_ext = os.path.splitext(base_name)[0]
    out_path = os.path.join(RESTORED_DIR, f"{name_no_ext}_restored.png")

    image.save(out_path)
    return out_path

def process_video(filepath):
    base_name = os.path.basename(filepath)
    name_no_ext, ext = os.path.splitext(base_name)

    if ext.lower() == '.gif':
        out_path = os.path.join(VIDEO_OUT_DIR, f"{name_no_ext}_ascii.gif")
    else:
        out_path = os.path.join(VIDEO_OUT_DIR, f"{name_no_ext}_ascii.mp4")

    convert_mul(video_fp=filepath, wfp=out_path, processes=8)
    return out_path

def on_drop(event):
    filepath = event.data.strip('{}')
    if os.path.isfile(filepath):
        try:
            ext = os.path.splitext(filepath)[1].lower()
            if ext in ['.png', '.jpg', '.jpeg', '.bmp']:
                result_file = process_image(filepath)
                print(f"ASCII-файл сохранён: {result_file}")
            elif ext == '.txt':
                result_file = process_ascii_file(filepath)
                print(f"Изображение восстановлено: {result_file}")
            elif ext in ['.mp4', '.avi', '.mov', '.mkv', '.gif']:
                result_file = process_video(filepath)
                print(f"ASCII-видео сохранено: {result_file}")
            else:
                print("Неподдерживаемый формат файла.")
                return
            os.startfile(os.path.dirname(result_file))
        except Exception as e:
            print(f"Ошибка: {e}")

def main():
    app = TkinterDnD.Tk()
    app.title("Конвертер в ASCII")
    app.geometry('650x300')
    app.configure(bg='#f0f8ff')

    frame = tk.Frame(app, bg='#d0ebff', relief="ridge", bd=4, highlightbackground="#3399ff", highlightthickness=1)
    frame.pack(padx=30, pady=40, fill='both', expand=True)

    label_title = tk.Label(frame, text="Перетащи сюда файл для конвертации", font=("Segoe UI", 16, "bold"), bg='#d0ebff', fg='#003366')
    label_title.pack(pady=(25, 12))

    label_formats = tk.Label(frame, text="*.jpg, *.png, *.txt, *.mp4, *.avi, *.gif", font=("Segoe UI", 10, "italic"), bg='#d0ebff', fg='#003366')
    label_formats.pack()

    frame.drop_target_register(DND_FILES)
    frame.dnd_bind('<<Drop>>', on_drop)

    app.mainloop()

if __name__ == '__main__':
    main()
