# simpleMDMpy
python lib for simpleMDM API

## usage
clone the repo and download the simpleMDMpy.
copy the "simpleMDMpy" Folder somewhere you need it.

import simpleMDMpy

apiKey = "adfasdf4rwrg"
devices = simpleMDMpy.devices(apiKey)
print devices.getDevice()
