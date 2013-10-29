import os

def walk(dirname):
    """Walks through a directory and prints the names of all 
    files in the directories and subdirectories.

    dirname: string
    Returns: None"""
    t = os.walk(dirname)
    for path, dirs, files in t:
        for f in files:
            print os.path.join(path, f)
