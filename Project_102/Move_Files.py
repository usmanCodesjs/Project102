import os
import shutil

from_dir = "Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)

print("Files in the source path:")
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if not extension:
        continue

    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    if extension.lower() in allowed_extensions:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", file_name)

        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
        else:
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
        shutil.move(path1, path3)
