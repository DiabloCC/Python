# batch_file_rename.py
# copied: 2016-03-13
# python version: 3.x

'''
This will batch rename a group of files in  a given directory,
once you pass the current and new extensions
'''

__author__ = 'Craig Richards'
__changeby__ = 'Charlie Chen'
__originver__ = '1.0'
__version__ = '1.1'

import os
import sys


def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        # Charlie: splitext() returns the extension with a leading dot. 
		if file_ext == '.' + old_ext:
            # Set newfile to be the filename, replaced with the new extension
            newfile = filename.replace(old_ext, new_ext)
            # Write the files
            os.rename(
              os.path.join(work_dir, filename),
              os.path.join(work_dir, newfile)
            )


def main():
    '''
    This will be called if the script is directly envoked.
    '''
    # Set the variable work_dir with the first argument passed
    work_dir = sys.argv[1]
    # Set the variable old_ext with the second argument passed
    old_ext = sys.argv[2]
    # Set the variable new_ext with the third argument passed
    new_ext = sys.argv[3]
    if (old_ext[0] == '.'):
		r = input('The old extension has a leading dot. \nBy default, \
file extensions may not include the leading dot. \
\nDo you want remove the leading dot? (y|n) ')
		if r == 'y':
			old_ext = sys.argv[2][1:]
	if (new_ext[0] == '.'):
		r = input('The new extension has a leading dot. \nBy default \
file extension does not include the leading dot. \
\nDo you want remove the leading dot? (y|n) ')
		if r == 'y':
			new_ext = sys.argv[3][1:]
    batch_rename(work_dir, old_ext, new_ext)
    # Print the file list to see if the names are changed.
    print('The file list in the given directory is:\n', os.listdir(work_dir))

if __name__ == '__main__':
    main()

