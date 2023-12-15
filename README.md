# file_organizer-package-
The file_organizer Python package simplifies the task of organizing files within a directory. It categorizes files based on their types or extensions and creates corresponding folders to neatly structure your files. 

# **Installation**
You can install the "file_organizer package' locally for testing purposes. Navigate to the root directory (where setup.py is located) and run:
pip install .

# Usage 

from file_organizer import FileOrganizer
#Replace 'path/to/your/directory' with the path to your target directory
target_directory = 'path/to/your/directory'

organizer = FileOrganizer(target_directory)
organizer.organize_files()

# Contributing
If you encounter issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.


