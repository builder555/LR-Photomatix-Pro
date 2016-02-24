# LR-Photomatix-Pro
A python script used to create HDR photos from Adobe Lightroom and Photomatix Pro software automatically on Mac OS X.

This script was tested on OS X 10.8-10.10+ successfully.

## How it works

* The script goes to the open Lightroom
* Creates two virtual copies of the selected photo (**NB: you must be in Library module**)
* Sets exposure to -2 on one virtual copy and +2 on another. 
* Exports original and the copies to Photomatix Pro
* Creates an HDR using settings that are selected already
* Re-imports created image into LR
* Deletes virtual copies and sets Picked flag on the original image. _Personally, i set a filter on library to only show unflagged images, so this last step hides the original image automatically_

## Prerequisites

The script requires [py-applescript](https://pypi.python.org/pypi/py-applescript/1.0.0) to be installed.

_You may need CLI Tools to install py-applescript*_

In order for Lightroom to contact Photomatix Pro, you also need the LR plugin from Photomatix (on OS X it should be automatically installed when you install Photomatix Pro, but if not, see [here](http://www.hdrsoft.com/support/faq_lrplugin.html#install_location))

 
## Installation

1. Open Terminal app (/Application/Utilities)

2. Clone the repository. In terminal type:
``` bash
git clone https://github.com/andreixk/LR-Photomatix-Pro
```

## Usage

1. Open Adobe Lightroom&copy;

2. Select the image you want to turn into an HDR.

3. Open Terminal and navigate to where you saved the script.
``` bash
#e.g. if you saved it to your Downloads folder, type this:
cd ~/Downloads/LR-Photomatix-Pro  
```

3. Run the script: 
``` bash 
python light.py
``` 
press enter and watch the magic happen.



<br/> <br/>
_*To install CLI tools run this command in terminal: ```xcode-select --install```_
