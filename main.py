from pathlib import Path
import shutil

print("""
--------------- Welcome to Folder Manager ---------------
** Want to manange your messed up folders, just run 
    this script and it will do it for you **\n
** You can also customize it by adding your file extension
    and folder name to this python script **
---------------------------------------------------\n
""")

directory = Path(input("Copy the exact path and paste it here.\nPATH: "))

file_extensions = {
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".pub": "Documents",
    ".csv": "Data",
    ".xlsx": "Data",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "Executables",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".flv": "Videos",
    ".wmv": "Videos",
    ".mkv": "Videos",
    ".pptx": "Presentation"
}

try:
    for file in directory.iterdir():
        if file.is_file():
            extension = file.suffix.lower()
            if extension in file_extensions:
                folder_name = Path(f"{directory}\\{file_extensions.get(extension)}")
                folder_name.mkdir(exist_ok=True)

                # move file to the dedicated folder
                shutil.move(str(file), str(folder_name))
    print("\n✅ Folder Managed Successfully.")
except Exception as e:
    print(f"❌ Error Occurred: {e}")