#!/usr/bin/env python

"""Lost Mode module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class LostMode(SimpleMDMpy.SimpleMDM.Connection):
    """Interact with lost mode on a device."""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/devices")

    def enable(self, device_id):
        """Activate lost mode on a device."""
        url = self.url + "/" + str(device_id) + "/lost_mode"
        data = {}
        return self._post_data(url, data)

    def disable(self, device_id):
        """Disable lost mode on a device."""
        url = self.url + "/" + str(device_id) + "/lost_mode"
        return self._delete_data(url)

    def play_sound(self, device_id):
        """Request that the device play a sound to assist
        with locating it."""
        url = self.url + "/" + str(device_id) + "/lost_mode/play_sound"
        data = {}
        return self._post_data(url, data)

    def update_location(self, device_id):
        """Request that the device provide its current,
        up-to-date location. Location data can be viewed
        using the devices endpoint."""
        url = self.url + "/" + str(device_id) + "/lost_mode/update_location"
        data = {}
        return self._post_data(url, data)
