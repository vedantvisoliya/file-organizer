# 📁 Folder Manager - A Python File Organizer

Organize your messy folders in just a few seconds!

This Python script helps you manage and organize files in a given directory by sorting them into subfolders based on their file extensions (e.g., Images, PDFs, Music, etc.).

## 🚀 Features

    Automatically sorts files into folders like Images, Documents, Videos, Archives, etc.

    Supports a wide range of file types.

    Customizable: Add or remove file extensions and their associated folder names.

    Simple, lightweight, and no external dependencies (only uses Python standard libraries).

## 🧑‍💻 How It Works

    1. Prompts you to enter the path of the folder you want to organize.

    2. Iterates through each file in the folder.

    3. Checks the file extension and moves it into the appropriate subfolder.

    4. Creates folders automatically if they don’t exist.

## 🛠️ Supported Extensions

| Folder       | Extensions                             |
| ------------ | -------------------------------------- |
| PDFs         | `.pdf`                                 |
| Images       | `.png`, `.jpg`, `.jpeg`, `.gif`        |
| Documents    | `.doc`, `.docx`, `.txt`, `.pub`        |
| Data         | `.csv`, `.xlsx`                        |
| Archives     | `.zip`, `.rar`                         |
| Executables  | `.exe`                                 |
| Music        | `.mp3`, `.wav`                         |
| Videos       | `.mp4`, `.avi`, `.flv`, `.wmv`, `.mkv` |
| Presentation | `.pptx`                                |

## 📝 How to Use
    
1. Clone or download this script:

```
    git clone https://github.com/your-username/folder-manager.git
    cd folder-manager
```

2. Run the script:

```
python manager.py
```

3. Paste the path of the folder you want to organize when prompted.

## ✏️ Customization

To add new file types or folder categories, just modify the file_extensions dictionary in the script:

```python
file_extensions = {
    ".pdf": "PDFs",
    ".psd": "Photoshop Files",  # Add this line for PSD files
}
```

## ⚠️ Note

    1. Ensure you have write access to the folder you are organizing.

    2. Files are moved, not copied — be careful while using it on important folders

## 📌 Requirements

    Python 3.x
    Modules used: pathlib, shutil (standard libraries)

## 🤝 Contributing

Pull requests and feedback are welcome! Open an issue or suggest improvements.