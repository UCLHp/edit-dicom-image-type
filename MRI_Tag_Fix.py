import easygui
import pydicom
import os

dir = easygui.diropenbox("Please select the DICOM directory")
print(f'Selected directory is: {dir}\n')

if not dir:
    print('No directory selected:')
    print('Code terminated')
    exit()

dicom_file_list = os.listdir(dir)
counter=0
for filename in dicom_file_list:
    if filename.startswith('MR'):
        counter += 1
        # dicom = pydicom.read_file(os.path.join(dir + '\\', filename))
        # dicom.ImageType = dicom.ImageType.replace(' ', '\\')
        # dicom.save_as(os.path.join(dir + '\\', filename))
print(f'{counter} out of {len(dicom_file_list)} files identified as MRI images')
