import os
import shutil

def organize_files(source_dir):
    # Dictionary mapping file extensions to destination folders
    extensions_mapping = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".jpeg": "Images",
        ".docx": "Documents",
        ".ipynb": "Jupyter Notebook"
    }

    # Create destination folders if they do not exist
    for folder in extensions_mapping.values():
        folder_path = os.path.join(source_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files based on their extensions
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = os.path.splitext(filename)[1]
            if file_extension in extensions_mapping:
                destination_folder = extensions_mapping[file_extension]
                source_file = os.path.join(source_dir, filename)
                destination_file = os.path.join(source_dir, destination_folder, filename)
                shutil.move(source_file, destination_file)
                print(f"Moved '{filename}' to '{destination_folder}' folder.")

# Specify the directory to be organized
source_directory = "./files_to_be_organized"

# Call the function to organize files
organize_files(source_directory)
