import os

SUPPORTED_EXTENSIONS = [
    ".py",
    ".c",
    ".cpp",
    ".java",
    ".js"
]

def scan_directory(directory: str):

    files_to_scan = []

    for root, dirs, files in os.walk(directory):

        for file in files:

            file_path = os.path.join(root, file)

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                files_to_scan.append(file_path)

    return files_to_scan
