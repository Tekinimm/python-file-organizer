# Python File Organizer 📂

A simple and efficient Python automation script to organize your cluttered "Downloads" folder.

## 🚀 What it does
This script scans your `Downloads` directory and automatically moves files into categorized folders based on their file extensions:
- **Images:** `.jpg`, `.jpeg`, `.png` are moved to `Downloads/Images`
- **Documents:** `.pdf`, `.docx`, `.doc` are moved to `Downloads/Documents`

It helps keep your workspace clean and organized instantly!

## 🛠️ How it works
The script utilizes Python's built-in `os` and `shutil` libraries to:
1. Detect the current user's Downloads path.
2. Check if destination folders exist (creates them if not).
3. Loop through files and move them to their respective folders securely.
