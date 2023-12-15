import os
import zipfile

# Specify the directory to monitor
source_dir = '../UnzipFolder'

file_count = 0

while True:
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.zip'):
            file_path = os.path.join(source_dir, file_name)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(source_dir)
                # Rename the extracted files here
                for extracted_file_name in zip_ref.namelist():
                    extracted_file_path = os.path.join(source_dir, extracted_file_name)
                    
                    # You can rename the file as you like here
                    new_name = f'assignment_{file_count}.txt'  # Replace with your desired name
                    os.rename(extracted_file_path, os.path.join(source_dir, new_name))
            os.remove(file_path)
    # Add a delay before checking again (e.g., every 20 seconds)
    import time
    time.sleep(20)
