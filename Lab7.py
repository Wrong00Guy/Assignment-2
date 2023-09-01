import os
import zipfile
def backup_folder_to_zip(source folder, zip_filename) :

    if not os. path . exists( source_folder) :
        print(f"Error: Source folder {source_folder}' does not exist. ")
        return

    zipf = zipfi1e.ZipFi1e(zip_fi1ename, 'w' )

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path,os.path.relpath(file_path.source_path))
            print(f"Zipping: {file_path}")

    zipf.close()
folder_to_backup = input ("Enter the name of the folder to backup (in the current working directory)")
# Generate a ZIP filename based on the folder name
zip_filename = f"{folder_to_backup}.zip"
# Call the function to create the backup
backup_folder_to_zip(folder_to_backup, zip_filename)