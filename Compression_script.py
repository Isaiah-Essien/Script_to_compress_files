import os
import shutil
import tarfile
import zipfile
from datetime import datetime

'''
This script prompts users to enter a file path to be compressed and then prompts them with file types
The users then input the numbers for the specific file type.
If the file path is correct, the file will be compressed. If it is incorrect it will display a message
'''

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        today = datetime.today().strftime('%Y_%m_%d')
        compressed_file_name = f"{folder_name}_{today}.{compress_type}"
        
        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_file_name, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
        
        elif compress_type == 'tar':
            with tarfile.open(compressed_file_name, 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        
        elif compress_type == 'tgz':
            with tarfile.open(compressed_file_name, 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        
        print(f"Compression successful. Compressed file saved as '{compressed_file_name}'.")
    
    except Exception as e:
        print(f"Compression failed: {e}")

def main():
    while True:
        folder_path = input("Enter the path of the folder to compress (or 'quit' to exit): ")
        if folder_path.lower() == 'quit':
            break
        
        if not os.path.exists(folder_path):
            print("Folder does not exist. Please enter a valid path or 'quit' to exit.")
            continue

        print("Available compressed file types:")
        print("1. zip")
        print("2. tar")
        print("3. tgz")

        compress_type_choice = input("Enter the number corresponding to the desired compressed file type (or 'quit' to exit): ")

        if compress_type_choice.lower() == 'quit':
            break
        
        if compress_type_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a valid number or 'quit' to exit.")
            continue

        if compress_type_choice == '1':
            compress_type = 'zip'
        elif compress_type_choice == '2':
            compress_type = 'tar'
        elif compress_type_choice == '3':
            compress_type = 'tgz'

        compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()

