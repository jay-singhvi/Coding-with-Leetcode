# python code to rename files where filename contains blank or whitespaces with hyphen "-"  or replace "." with "" and make sure "." for seperating extension does not get replaced from the file name. in the folder "Solutions"

import os
import re

def rename_file(filename):
    # Split the filename and extension
    name, ext = os.path.splitext(filename)

    # Replace spaces with hyphens
    name = name.replace(" ", "-")

    # Use regex to replace the dot after numbers with a hyphen,
    # but only if it's not already preceded by a hyphen
    name = re.sub(r'(\d+)(?<!-)\.', r'\1-', name)

    # Replace any remaining dots with hyphens
    name = name.replace(".", "-")

    # Remove any double hyphens that might have been created
    name = re.sub(r'-+', '-', name)

    # Combine the modified name and the original extension
    return f"{name}{ext}"

def main():
    folder_path = "Solutions"

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        new_filename = rename_file(filename)
        new_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except OSError as e:
            print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    main()