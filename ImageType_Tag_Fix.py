'''
Created by Callum Gillies 06/05/2020,
This code intends to edit the tag only and leave the image intact

This code was not intended to be a completely automated procedure.
Appropriate QA checks should be performed after the code is run
to ensure the imagess are unchanged

I take no responsibility if this code is used without checks resulting
in changes to the image.
'''

# First import libraries required for code to function
import easygui
import pydicom
import os

print('''Created by Callum Gillies 06/05/2020,
This code intends to edit the tag only and leave the image intact

This code was not intended to be a completely automated procedure.
Appropriate QA checks should be performed after the code is run
to ensure the imagess are unchanged

I take no responsibility if this code is used in any way other than
intended or without checks that may result in errors.
''')

if easygui.ynbox("Do you accept the disclaimer and wish to continue?:"):
    pass  # continue
else:
    print('Code will not run if disclaimer is not accepted')
    input('Press enter to close window')
    exit()  # exit the program

# User selects the directory then exited if directory selection is cancelled
dir = easygui.diropenbox("Please select the DICOM directory")

if not dir:
    print('No directory selected:')
    print('Code terminated')
    input('Press enter to close window')
    exit()

print(f'Selected directory is: {dir}\n')
print('Please wait, checking tags...\n')

# Full list of files in the directory is assigned and counter is defined to
# track the number of images requiring correction
dicom_file_list = os.listdir(dir)
counter = 0

# Terminate if selected directory is empty
if len(dicom_file_list) == 0:
    print('Selected directory is empty')
    print('Code Terminated')
    input('Press enter to close window')
    exit()

# Loops through each file in the directory,
# if the file contains the ImageType Tag, it is opened, checked for spaces and
# edited to replace spaces with backslashes if present
for filename in dicom_file_list:
    dicom = pydicom.read_file(os.path.join(dir + '\\', filename))
    if (0x0008, 0x0008) in dicom:
        if isinstance(dicom.ImageType, str):
            counter += 1
            dicom.ImageType = dicom.ImageType.replace(' ', '\\')
            dicom.save_as(os.path.join(dir + '\\', filename))

print(f'{counter} of {len(dicom_file_list)} files corrected for spaces')
print('\nCode Finished')
input('Press enter to close window')
