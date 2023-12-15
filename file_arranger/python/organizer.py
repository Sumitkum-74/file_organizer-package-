# organizer.py

import os
import shutil

class FileOrganizer:
    def __init__(self, target_directory):
        self.target_directory = target_directory
        self.file_types = {}

    def organize_files(self):
        # Iterate through files in the target directory
        for filename in os.listdir(self.target_directory):
            file_path = os.path.join(self.target_directory, filename)

            # Check if it's a file
            if os.path.isfile(file_path):
                # Get the file extension
                file_extension = filename.split('.')[-1].lower()

                # Create a folder for the file type if it doesn't exist
                if file_extension not in self.file_types:
                    self.file_types[file_extension] = os.path.join(self.target_directory, file_extension)
                    os.makedirs(self.file_types[file_extension])

                # Move the file to the corresponding folder
                destination_path = os.path.join(self.file_types[file_extension], filename)
                shutil.move(file_path, destination_path)

# # Example usage:
# if __name__ == "__main__":
#     # Replace 'path/to/your/directory' with the path to your target directory
#     target_directory = 'path'

#     organizer = FileOrganizer(target_directory)
#     organizer.organize_files()
