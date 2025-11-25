import os
import shutil

# 1. Locate the Downloads Directory
# Finds the user's home directory and targets 'Downloads'.
user_path = os.path.expanduser("~")
downloads_path = os.path.join(user_path, "Downloads")

# Define Paths for Destination Folders
images_path = os.path.join(downloads_path, "Images")
documents_path = os.path.join(downloads_path, "Documents")

# Define file extensions to look for
image_extensions = ['.jpg', '.jpeg', '.png']
document_extensions = ['.pdf', '.docx', '.doc']

def create_directories():
    """Creates destination folders if they don't exist."""
    if not os.path.exists(images_path):
        os.makedirs(images_path)
        print(f"[INFO] Created directory: '{images_path}'")
    
    if not os.path.exists(documents_path):
        os.makedirs(documents_path)
        print(f"[INFO] Created directory: '{documents_path}'")

def organize_files():
    """Scans files and moves them to respective folders."""
    print("--- Scanning Started ---\n")
    
    # List all files in the Downloads directory
    files = os.listdir(downloads_path)

    moved_file_count = 0

    for filename in files:
        # Full path of the source file
        source_file = os.path.join(downloads_path, filename)

        # Skip if it's a directory
        if os.path.isdir(source_file):
            continue

        # Get file extension and convert to lowercase
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        destination_folder = None

        # Determine destination based on extension
        if extension in image_extensions:
            destination_folder = images_path
        elif extension in document_extensions:
            destination_folder = documents_path

        # Move the file if a destination is determined
        if destination_folder:
            destination_file = os.path.join(destination_folder, filename)
            
            try:
                shutil.move(source_file, destination_file)
                # Print action to screen
                folder_name = os.path.basename(destination_folder)
                print(f"[MOVED] {filename} -> {folder_name}")
                moved_file_count += 1
            except Exception as e:
                print(f"[ERROR] Could not move {filename}. Reason: {e}")
        else:
            # Optional: Print skipped files
            # print(f"[SKIPPED] {filename} (Unknown extension)")
            pass

    print(f"\n--- Process Completed ---")
    print(f"Total files organized: {moved_file_count}")

if __name__ == "__main__":
    # Execution flow
    if os.path.exists(downloads_path):
        create_directories()
        organize_files()
    else:
        print("ERROR: Downloads directory not found!")