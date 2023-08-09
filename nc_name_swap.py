import os

# Define the root directory containing the nc files
root_dir = input("Enter the root directory containing the nc files: ")

# Traverse the directory tree recursively and process each nc file
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".nc"):
            # Read the text from the file
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r") as file:
                text = file.readlines()

            # Swap the contents of line 3 and line 5
            if len(text) >= 5:
                text[2], text[4] = text[4], text[2]

                # Write the new text to the file
                with open(file_path, "w") as file:
                    file.writelines(text)
            else:
                print(f"File {file_path} does not have at least 5 lines of text and cannot be processed.")
