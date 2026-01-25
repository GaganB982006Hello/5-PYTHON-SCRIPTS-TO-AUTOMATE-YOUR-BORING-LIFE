import os
import shutil

# defined directories
source_dir = "/Users/YourName/Downloads/"  # Change this to your path
dest_dirs = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_files():
    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        # Skip directories, only move files
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Check which category the file belongs to
            for folder, extensions in dest_dirs.items():
                if file_ext in extensions:
                    # Create destination folder if it doesn't exist
                    target_folder = os.path.join(source_dir, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    # Move the file
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    print(f"Moved {filename} to {folder}")
                    break

if __name__ == "__main__":
    organize_files()
