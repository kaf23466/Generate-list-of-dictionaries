#!/usr/bin/env python3.7

import os
import glob

def get_files_with_sizes(directory_path):
    return [
        {"PATH": file, "SIZE": os.path.getsize(file)} 
        for file in glob.glob(directory_path + '/*') 
        if os.path.isfile(file)
    ]

def main():
    cwd_path = os.getcwd()
    cwd_path_files = get_files_with_sizes(cwd_path)
    
    for file_info in cwd_path_files:
        print(file_info)

if __name__ == "__main__":
    main()
