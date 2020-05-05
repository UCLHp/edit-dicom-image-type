import easygui
import pydicom
import os

dir = easygui.diropenbox("Please select the DICOM directory")

dicom_file_list = os.listdir(dir)

dicom_path_list = []

for filename in dicom_file_list:
    if filename.startswith('MR'):
        dicom = pydicom.read_file(os.path.join(dir + '\\', filename))
        dicom.ImageType = dicom.ImageType.replace(' ', '\\')
        dicom.save_as(os.path.join(dir + '\\', filename))
