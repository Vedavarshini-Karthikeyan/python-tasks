import os

folders = input("Provide the list of folder paths separated by spaces:").split()
for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Folder Not Found:" + folder)
        continue
    except PermissionError:
        print("Permission Denied:" + folder)
        continue

    print("Listing the files in the folder:" + folder + ":")
    for file in files:
        print(file)


#Using the Function
import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()