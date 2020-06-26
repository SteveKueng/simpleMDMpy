#!/usr/bin/env python

"""managed app configs module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class ManagedAppConfigs(SimpleMDMpy.SimpleMDM.Connection):
    """Create, modify, and remove the managed app configuration
    associated with an app."""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/apps")

    def get_managed_configs(self, app_id):
        """"Retrieve the managed configs for an app."""
        url = self.url + "/" + app_id + "/managed_configs"
        data = {}
        return self._get_data(url, data)

    def push_updates(self, app_id):
        """Push any updates to the managed configurations
        for an app to all devices. This is not necessary
        when making managed config changes through the UI.
        This is necessary after making changes through the API."""
        url = self.url + "/" + app_id + "/managed_configs/push"
        data = {}
        return self._post_data(url, data)

    def delete_config(self, app_id, managed_config_id):
        """Delete managed config from an app by ID."""
        url = self.url + "/" + app_id + "/managed_configs/" + managed_config_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args
