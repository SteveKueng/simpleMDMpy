# simpleMDMpy
python lib for simpleMDM API

## usage
clone the repo and download the simpleMDMpy.
copy the "simpleMDMpy" Folder somewhere you need it.

```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


account = simpleMDMpy.account(apiKey)
account.setAcountDetais(name="Test Comp", country_code="US")
print account.getAcountDetais()


devices = simpleMDMpy.devices(apiKey)
print devices.getDevice("all")
print devices.getDevice(deviceID="1234")

print devices.listInstalledApps(deviceID="1234")

devices.createDevice(name="My Device", groupID="4321")

devices.updateDevice(name="new device name", deviceID="1234")

devices.deleteDevice(deviceID="1234")

devices.lockDevice(deviceID="1234", message="my lock message", phone_number="52174823")

devices.clearPasscodeDevice(deviceID="1234")

devices.wipeDevice(deviceID="1234")

devices.pushAppsDevice(deviceID="1234")


deviceGroups = simpleMDMpy.deviceGroups(apiKey)
print deviceGroups.getDeviceGroup('all')
print deviceGroups.getDeviceGroup(deviceGoupID="4312")

deviceGroups.assignDevice(deviceID="1234", deviceGoupID="4312")
```
