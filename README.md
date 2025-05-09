# ASCII Converter GUI

This project provides a drag-and-drop graphical interface (GUI) for converting media files to and from ASCII format.

## ✨ Features

* **Convert images** (.jpg, .png, .bmp) to ASCII text (.txt)
* **Restore images** from ASCII text files (.txt → .png)
* **Convert videos and gifs** (.mp4, .avi, .mov, .mkv, .gif) to ASCII-style animations
* **Modern GUI** with styled drop zone and format hints
* Supports `.gif` looped playback and improved frame rates

## 🖼 GUI Overview

Just drag and drop a file onto the light blue box:

* Top label: "Drag file here to convert"
* Supported formats shown in italic

## 📁 Output

* ASCII text files: stored in `output_ascii/`
* Restored images: stored in `restored_images/`
* ASCII videos: stored in `ascii_videos/`

## 🚀 How to Run

```bash
python gui_app.py
```

Make sure all dependencies are installed (see below).

## 📦 Requirements

```
tkinterdnd2
opencv-python
Pillow
imageio
imageio[ffmpeg]  # optional but recommended for video support
numpy
```

Install all at once:

```bash
pip install tkinterdnd2 opencv-python Pillow imageio[ffmpeg] numpy
```

---

Forked and enhanced with GUI and full media support.
