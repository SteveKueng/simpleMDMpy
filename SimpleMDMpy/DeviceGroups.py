#!/usr/bin/env python

"""device groups module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class DeviceGroups(SimpleMDMpy.SimpleMDM.Connection):
    """device groups module for SimpleMDMpy"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/device_groups")

    def get_device_group(self, device_group_id="all"):
        """get a devices group"""
        url = self.url
        if device_group_id != 'all':
            url = url + "/" + device_group_id
        return self._get_data(url)

    def assign_device(self, device_id, device_group_id):
        """assign device to a group"""
        url = self.url + "/" + device_group_id + "/devices/" + str(device_id)
        data = {}
        return self._post_data(url, data)
