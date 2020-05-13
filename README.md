# edit-dicom-image-type
Created by Callum Gillies 06/05/2020

Convert spaces to backslashes in ImageType DICOM tag. 

This script was created because we were unable to import various files from other centres.
This code intends to edit the tag only and leave the image intact. 

This code was not intended to be a completely automated procedure. Appropriate QA checks
should be performed after the code is run to ensure the imagess are unchanged

I take no responsibility if this code is used in any way other than
intended or without checks that may result in errors.


## Installation

Do not install, please use the latest version of the executable.

### Requirements

pydicom 
os 
easygui 


## Usage

* Copy MRI DICOM files into temporary directory, run the executable and
follow the command prompt instructions. 
* Import the edited files into eclipse. 
* Perform QA checks against PACS once imported into eclipse. 


## Contribute

Pull requests are welcome.  
For major changes, please open a ticket first to discuss desired changes: [edit-dicom-image-type/issues](http://github.com/UCLHp/edit-dicom-image-type/issues)


## Licence

All code within this package distributed under [GNU GPL-3.0 (or higher)](https://opensource.org/licenses/GPL-3.0). Full license text contained within the file LICENSE.

###  (C) License for all programmes

```
###  Copyright (C) 2020:  Callum Stuart Main Gillies

  #  This program is free software: you can redistribute it and/or modify
  #  it under the terms of the GNU General Public License as published by
  #  the Free Software Foundation, either version 3 of the License, or
  #  (at your option) any later version.

  #  This program is distributed in the hope that it will be useful,
  #  but WITHOUT ANY WARRANTY; without even the implied warranty of
  #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  #  GNU General Public License for more details.

  #  You should have received a copy of the GNU General Public License
  #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
