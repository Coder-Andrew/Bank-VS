#Testing ways to write files to seperate directories
import os
import sys

dirname = os.path.split(os.getcwd())

print(dirname)

class DirectoryError(Exception):
    pass


def output_dir():
    dir = os.path.split(os.getcwd())
    if dir[1] == 'Bank VS':
        return dir[1]

    if dir[1] == 'writeFilesToDir':
        return dir[1]

    else:
        raise DirectoryError('File not in correct directory')

print(output_dir())