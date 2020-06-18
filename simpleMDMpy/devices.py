#!/usr/bin/env python

"""devices module for SimpleMDMpy"""

import SimpleMDMpy.SimpleMDM

class Devices(SimpleMDMpy.SimpleMDM.Connection):
    """devices module for SimpleMDMpy"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/devices")

    def get_device(self, device_id="all", search=None):
        """Returns a device specified by id. If no ID or search is
        specified all devices will be returned"""
        url = self.url
        data = None
        if search:
            data = {'search': search}
        elif device_id != 'all':
            url = url + "/" + device_id
        return self._get_data(url, data)

    def create_device(self, name, group_id):
        """Creates a new device object in SimpleMDM. The response
        body includes an enrollment URL that can be used once to
        enroll a physical device."""
        data = {'name': name, 'group_id': group_id}
        return self._post_data(self.url, data)

    def update_device(self, name, device_id):
        """Update the SimpleMDM name or device name of a device object."""
        url = self.url + "/" + device_id
        data = {'name': name}
        return self._patch_data(url, data)

    def delete_device(self, device_id):
        """Unenroll a device and remove it from the account."""
        url = self.url + "/" + device_id
        data = {}
        return self._delete_data(url, data)

    def list_installed_apps(self, device_id):
        """Returns a listing of the apps installed on a device."""
        url = self.url + "/" + device_id + "/installed_apps"
        return self._get_data(url)

    def push_apps_device(self, device_id):
        """You can use this method to push all assigned apps
        to a device that are not already installed."""
        url = self.url + "/" + device_id + "/push_apps"
        data = {}
        return self._post_data(url, data)

    def restart_device(self, device_id):
        """This command sends a restart command to the device."""
        url = self.url + "/" + device_id + "/restart"
        data = {}
        return self._post_data(url, data)

    def shutdown_device(self, device_id):
        """This command sends a shutdown command to the device."""
        url = self.url + "/" + device_id + "/shutdown"
        data = {}
        return self._post_data(url, data)

    def lock_device(self, device_id, message, phone_number, pin=None):
        """You can use this method to lock a device and optionally display
        a message and phone number. The device can be unlocked with the
        existing passcode of the device."""
        url = self.url + "/" + device_id + "/lock"
        data = {'message': message, 'phone_number': phone_number, 'pin':pin}
        return self._post_data(url, data)

    def clear_passcode_device(self, device_id):
        """You can use this method to unlock and remove the passcode of a device."""
        url = self.url + "/" + device_id + "/clear_passcode"
        data = {}
        return self._post_data(url, data)

    def clear_firmware_password(self, device_id):
        """You can use this method to remove the firmware password from a device.
        The firmware password must have been originally set using SimpleMDM for
        this to complete successfully."""
        url = self.url + "/" + device_id + "/clear_firmware_password"
        data = {}
        return self._post_data(url, data)

    def wipe_device(self, device_id):
        """You can use this method to erase all content and settings stored on a
        device. The device will be unenrolled from SimpleMDM and returned to a
        factory default configuration."""
        url = self.url + "/" + device_id + "/wipe"
        data = {}
        return self._post_data(url, data)

    def update_os(self, device_id):
        """You can use this method to update a device to the latest OS version.
        Currently supported by iOS devices only."""
        url = self.url + "/" + device_id + "/update_os"
        data = {}
        return self._post_data(url, data)

    def refresh_device(self, device_id):
        """Request a refresh of the device information and app inventory.
        SimpleMDM will update the inventory information when the device responds
        to the request."""
        url = self.url + "/" + device_id + "/refresh"
        data = {}
        return self._post_data(url, data)

    def get_custom_attribute(self, device_id, custom_attribute_name):
        """get a devices custom attributes"""
        url = self.url + "/" + device_id + "/custom_attribute_values/" + custom_attribute_name
        data = {}
        return self._get_data(url, data)

    def set_custom_attribute(self, value, device_id, custom_attribute_name):
        """set a devices custom attribute to a specific value"""
        url = self.url + "/" + device_id + "/custom_attribute_values/" + custom_attribute_name
        data = {'value': value}
        return self._get_data(url, data)
