import easygui
import pydicom
import os

selected_directory = easygui.diropenbox("Please select the folder containing the MRI DICOM Files")

DCM_file_list = os.listdir(selected_directory)

DCM_path_list=[]

for filename in DCM_file_list:
        if "MR" in filename.upper(): # Won't work if filenames don't start with MR
            DCM = pydicom.read_file(os.path.join(selected_directory+'\\',filename))
            DCM.ImageType = DCM.ImageType.replace(' ','\\')
            DCM.save_as(os.path.join(selected_directory+'\\',filename))
