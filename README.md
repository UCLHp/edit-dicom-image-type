# edit-dicom-image-type


This script was created because we were unable to import MRI files

# MRI_Tag_Fix

converts spaces to backslash in MRI ImageType DICOM tag

### Components

README.md
.gitignore
LICENSE
MRI_Tag_Fix.py
f formed of multiple parts, outline file structure

## Installation

Unsure how to install - maybe provide executable here

### Requirements

pydicom
os
easygui

### Tests

No tests currently included

## Usage

Copy MRI DICOM files into temporary directory
Run the executable and follow the command prompt instructions
Once code has finished running, import the edited files into eclipse
Perform QA checks against PACS once imported into eclipse

## Limitations / Known Bugs

DICOM files must begin with MR
only the image type tag is edited, this will not solve other issues

## Contribute

Pull requests are welcome.  
For major changes, please open a ticket first to discuss desired changes:  
[[repo-name]/issues](http://github.com/UCLHp/[repo-name]/issues)

If making changes, please check all tests and add if required.

## Licence

All code within this package distributed under [GNU GPL-3.0 (or higher)](https://opensource.org/licenses/GPL-3.0).

Full license text contained within the file LICENCE.

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
