# simpleMDMpy
python lib for simpleMDM API

https://simplemdm.com/docs/api

## usage
``` 
pip install simpleMDMpy

```

### Account
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


account = simpleMDMpy.account(apiKey)
account.setAcountDetais(name="Test Comp", country_code="US")
print account.getAcountDetais()
```

### Apps
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


apps = simpleMDMpy.apps(apiKey)
print apps.getApp('all')
print apps.getApp('123532')

apps.createApp(name="MyTestApp", appStoreID="1090161858", bundleID="com.myCompany.MyApp1", binary="/path/to/pkg/or/ipa")

apps.updateApp(appID="123532", binary="/path/to/ipa", name="MyNewAppName")

apps.deleteApp(appID="123532")
```

### Devices
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


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
```

### Device Groups
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


deviceGroups = simpleMDMpy.deviceGroups(apiKey)
print deviceGroups.getDeviceGroup('all')
print deviceGroups.getDeviceGroup(deviceGoupID="4312")

deviceGroups.assignDevice(deviceID="1234", deviceGoupID="4312")
```

### Installed Apps
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


installedApps = simpleMDMpy.installedApps(apiKey)

print installedApps.getApp(installedAppID="234123")

installedApps.deleteApp(installedAppID="234123")
```

### Managed App Configs
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


managedAppConfigs = simpleMDMpy.managedAppConfigs(apiKey)

print managedAppConfigs.getManagedConfigs(appID="12323")

managedAppConfigs.pushUpdates(appID="12323")
```

### Push Certificate
```python
import simpleMDMpy

apiKey = "adfasdf4rwrgasdfas"


pushCertificate = simpleMDMpy.pushCertificate(apiKey)

print pushCertificate.getPushCertificate()

updateCertificate(file=/path/to/cert, appleID="my.apple.id.com")

print pushCertificate.getSignedCSR()
```
