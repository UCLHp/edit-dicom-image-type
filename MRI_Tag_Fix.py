# First import libraries required for code to function
import easygui
import pydicom
import os

print('Libraries imported\n')

# User selects the directory which is then confirmed in a print statement
dir = easygui.diropenbox("Please select the DICOM directory")
print(f'Selected directory is: {dir}\n')

# Code is exited if directory selection is cancelled
if not dir:
    print('No directory selected:')
    print('Code terminated')
    exit()

# Full list of files in the directory is assigned and counter is defined to
# track the number of MR images
dicom_file_list = os.listdir(dir)
counter = 0

# Terminate if selected directory is empty
if len(dicom_file_list) == 0:
    print('Selected directory is empty')
    print('Code Terminated')
    exit()

# Loops through each file in the directory,
# if the file name begins with MR, it is opened and the Image Type tag is
# edited to replace spaces with backslashes
for filename in dicom_file_list:
    if filename.startswith('MR'):
        counter += 1
        dicom = pydicom.read_file(os.path.join(dir + '\\', filename))
        dicom.ImageType = dicom.ImageType.replace(' ', '\\')
        dicom.save_as(os.path.join(dir + '\\', filename))

print(f'{counter} of {len(dicom_file_list)} files identified as MRI images')
print('\nCode Finished')
