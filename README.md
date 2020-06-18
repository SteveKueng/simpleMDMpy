# SimpleMDMpy

python lib for simpleMDM API

https://simplemdm.com/docs/api

## Install

Your SimpleMDM API key will need to be set as an environmental variable `api_key`.

Help available via `help(SimpleMDMpy)

## Available Modules

### Account

```python
class Account(SimpleMDMpy.SimpleMDM.Connection)
 |  account class provides auth and basic account details
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  get_account_details(self)
 |      returns account details as dict
 |
 |  set_account_details(self, name=None, country_code=None)
 |      set account detail
```

### App Groups

```python
class AppGroups(SimpleMDMpy.SimpleMDM.Connection)
 |  App Groups class provides interaction with Application Groups
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  assign_app(self, app_group_id, app_id)
 |      remove app group from group
 |
 |  assign_device(self, app_group_id, device_id)
 |      assign device to app group
 |
 |  assign_device_group(self, app_group_id, device_group_id)
 |      assign device group from app group
 |
 |  create_app_group(self, name, auto_deploy='true')
 |      create app group
 |
 |  delete_app_group(self, app_group_id)
 |      remove app group
 |
 |  get_app_group(self, app_group_id='all')
 |      Get an app group, defaults to 'all' if 'app_group_id' is not present
 |
 |  push_apps(self, app_group_id)
 |      push apps in app group
 |
 |  un_assign_app(self, app_group_id, app_id)
 |      unassign app from app group
 |
 |  un_assign_device(self, app_group_id, device_id)
 |      unassign apps in app group
 |
 |  un_assign_device_group(self, app_group_id, device_group_id)
 |      remove device group from app group
 |
 |  update_app_group(self, app_group_id, name=None, auto_deploy='true')
 |      update app group
 |
 |  update_apps(self, app_group_id)
 |      update apps
 |

```

### Apps

```python
class Apps(SimpleMDMpy.SimpleMDM.Connection)
 |  apps module for SimpleMDMpy
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  create_app(self, name=None, app_store_id=None, bundle_id=None, binary=None)
 |      upload an app binary
 |
 |  delete_app(self, app_id)
 |      delete an app
 |
 |  get_app(self, app_id='all')
 |      list app, if none specified all return
 |
 |  update_app(self, app_id, binary=None, name=None)
 |      update an apps info binary etc
 |
```

### Assignment Groups

```python
class AssignmentGroups(SimpleMDMpy.SimpleMDM.Connection)
 |  assignment groups module for SimpleMDMpy
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  assign_app(self, assignment_group_id, app_id)
 |      assign app to an assignment group
 |
 |  assign_device(self, assignment_group_id, device_id)
 |      assign device to an assignment group
 |
 |  assign_device_group(self, assignment_group_id, device_group_id)
 |      assigns a device group
 |
 |  create_assignment_group(self, name, auto_deploy)
 |      creates an assignment group
 |
 |  delete_assignment_group(self, assignment_group_id)
 |      delete an app to an assignment group
 |
 |  get_assignment_groups(self, assignment_group_id='all')
 |      returns assignment group(s), defaults to all if none specified
 |
 |  push_apps(self, assignment_group_id)
 |      push apps in an assignment group
 |
 |  unassign_app(self, assignment_group_id, app_id)
 |      unassign app to an assignment group
 |
 |  unassign_device(self, assignment_group_id, device_id)
 |      unassign device to an assignment group
 |
 |  unassign_device_group(self, assignment_group_id, device_group_id)
 |      delete a device group assignment
 |
 |  update_apps(self, assignment_group_id)
 |      update apps in an assignment group
 |
 |  update_assignment_group(self, assignment_group_id, name, auto_deploy)
 |      updates an assignment group
 |

```

### Custom Attributes

```python
class CustomAttributes(SimpleMDMpy.SimpleMDM.Connection)
 |  work with custom attributes
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  create_custom_attribute(self, name)
 |      create custom attribute
 |
 |  delete_custom_attribute(self, custom_attribute_id)
 |      deletes custom attribute
 |
 |  get_custom_attributes(self)
 |      lists all custom attributes
 |
```

<!-- TODO: Custom Configuration -->

### Custom Configuration Profiles
<!-- TODO: DOWNLOAD PROFILE -->
```python
class CustomConfigurationProfiles(SimpleMDMpy.SimpleMDM.Connection)
 |  work with custom profiles
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  assign_to_device_group(self, profile_id, device_group_id)
 |      assigns custom profile to group
 |
 |  create_profile(self, name, mobileconfig, user_scope=None, attribute_support=False)
 |      upload a config file
 |
 |  delete_profile(self, profile_id)
 |      deletes custom profile
 |
 |  get_profiles(self)
 |      returns profiles
 |
 |  unassign_from_device_group(self, profile_id, device_group_id)
 |      deletes profile from device group
 |
 |  update_profile(self, profile_id, name=None, mobileconfig=None, user_scope=None, attribute_support=None)
 |      update a config file
 |
```

### DEP Servers

```python
class DepServers(SimpleMDMpy.SimpleMDM.Connection)
 |  module for interacting with dep server configurations
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  get_dep_devices(self, dep_server_id, dep_device_id='all')
 |      return a DEP device via an ID, defaults to all if none specified
 |
 |  get_dep_servers(self, dep_server_id='all')
 |      returns dep servers, defaults to all if none specified
 |
 |  sync_dep_servers(self, dep_server_id)
 |      syncs specified server with Apple DEP
 |
```

### Devices

```python
class Devices(SimpleMDMpy.SimpleMDM.Connection)
 |  devices module for SimpleMDMpy
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  clear_firmware_password(self, device_id)
 |      You can use this method to remove the firmware password from a device.
 |      The firmware password must have been originally set using SimpleMDM for
 |      this to complete successfully.
 |
 |  clear_passcode_device(self, device_id)
 |      You can use this method to unlock and remove the passcode of a device.
 |
 |  create_device(self, name, group_id)
 |      Creates a new device object in SimpleMDM. The response
 |      body includes an enrollment URL that can be used once to
 |      enroll a physical device.
 |
 |  delete_device(self, device_id)
 |      Unenroll a device and remove it from the account.
 |
 |  get_custom_attribute(self, device_id, custom_attribute_name)
 |      get a devices custom attributes
 |
 |  get_device(self, device_id='all', search=None)
 |      Returns a device specified by id. If no ID or search is
 |      specified all devices will be returned
 |
 |  list_installed_apps(self, device_id)
 |      Returns a listing of the apps installed on a device.
 |
 |  lock_device(self, device_id, message, phone_number, pin=None)
 |      You can use this method to lock a device and optionally display
 |      a message and phone number. The device can be unlocked with the
 |      existing passcode of the device.
 |
 |  push_apps_device(self, device_id)
 |      You can use this method to push all assigned apps
 |      to a device that are not already installed.
 |
 |  refresh_device(self, device_id)
 |      Request a refresh of the device information and app inventory.
 |      SimpleMDM will update the inventory information when the device responds
 |      to the request.
 |
 |  restart_device(self, device_id)
 |      This command sends a restart command to the device.
 |
 |  set_custom_attribute(self, value, device_id, custom_attribute_name)
 |      set a devices custom attribute to a specific value
 |
 |  shutdown_device(self, device_id)
 |      This command sends a shutdown command to the device.
 |
 |  update_device(self, name, device_id)
 |      Update the SimpleMDM name or device name of a device object.
 |
 |  update_os(self, device_id)
 |      You can use this method to update a device to the latest OS version.
 |      Currently supported by iOS devices only.
 |
 |  wipe_device(self, device_id)
 |      You can use this method to erase all content and settings stored on a
 |      device. The device will be unenrolled from SimpleMDM and returned to a
 |      factory default configuration.
 |
```

### Device Groups

```python
class DeviceGroups(SimpleMDMpy.SimpleMDM.Connection)
 |  device groups module for SimpleMDMpy
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  assign_device(self, device_id, device_group_id)
 |      assign device to a group
 |
 |  get_device_group(self, device_group_id='all')
 |      get a devices group
 |
```

### Enrollments

```python
class Enrollments(SimpleMDMpy.SimpleMDM.Connection)
 |  enrollments module for SimpleMDMpy
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  delete_enrollment(self, enrollment_id)
 |      delete enrollment
 |
 |  get_enrollments(self, enrollment_id='all')
 |      get a devices group
 |
 |  send_invitation(self, enrollment_id, contact)
 |      Send an enrollment invitation to an email address or phone number.
 |
```

### Installed Apps

```python
class InstalledApps(SimpleMDMpy.SimpleMDM.Connection)
 |  Installed apps represent apps that are installed and exist on devices.
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  delete_app(self, installed_app_id)
 |      This submits a request to the device to uninstall the specified app.
 |      The app must be managed for this request to succeed.
 |
 |  get_app(self, installed_app_id)
 |      retrieve an installed app
 |
 |  update(self, installed_app_id)
 |      This submits a request to the device to update the specified app to
 |      the latest version. The app must be managed for this request to succeed.
 |
```

### Logs

```python
class Logs(SimpleMDMpy.SimpleMDM.Connection)
 |  GET all the LOGS
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  get_logs(self)
 |      And I mean all the LOGS, before pagination
 |

```

### Lost Mode

```python
class LostMode(SimpleMDMpy.SimpleMDM.Connection)
 |  Interact with lost mode on a device.
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  disable(self, device_id)
 |      Disable lost mode on a device.
 |
 |  enable(self, device_id)
 |      Activate lost mode on a device.
 |
 |  play_sound(self, device_id)
 |      Request that the device play a sound to assist
 |      with locating it.
 |
 |  update_location(self, device_id)
 |      Request that the device provide its current,
 |      up-to-date location. Location data can be viewed
 |      using the devices endpoint.
 |

```

### Managed App Configs

```python
class ManagedAppConfigs(SimpleMDMpy.SimpleMDM.Connection)
 |  Create, modify, and remove the managed app configuration
 |  associated with an app.
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  delete_config(self, app_id, managed_config_id)
 |      Delete managed config from an app by ID.
 |
 |  get_managed_configs(self, app_id)
 |      "Retrieve the managed configs for an app.
 |
 |  push_updates(self, app_id)
 |      Push any updates to the managed configurations
 |      for an app to all devices. This is not necessary
 |      when making managed config changes through the UI.
 |      This is necessary after making changes through the API.
 |
```

### Push Certificate

```python
class PushCertificate(SimpleMDMpy.SimpleMDM.Connection)
 |  Push cert module actions
 |
 |  Methods defined here:
 |
 |  __init__(self, api_key)
 |
 |  get_signed_csr(self)
 |      Download a signed CSR file. This file is
 |      provided to Apple when creating and renewing a
 |      push certificate. The API returns a base64
 |      encoded plist for upload to the Apple Push
 |      Certificates Portal. The value of the data
 |      key can be uploaded to Apple as is
 |
 |  getpush_certificate(self)
 |      Show details related to the current push
 |      certificate being used.
 |
 |  update_certificate(self, file, apple_id)
 |      Upload a new certificate and replace the
 |      existing certificate for your account.
 |
```
