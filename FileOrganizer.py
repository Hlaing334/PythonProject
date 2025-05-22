import os
import shutil

source_dir = "C:/Users/zinzi"
file_types = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar"],
}
for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(source_dir, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))
                break
