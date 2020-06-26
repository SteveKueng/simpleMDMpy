#!/usr/bin/env python

"""installed apps module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class InstalledApps(SimpleMDMpy.SimpleMDM.Connection):
    """Installed apps represent apps that are installed and exist on devices."""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/installed_apps")

    def get_app(self, installed_app_id):
        """retrieve an installed app"""
        url = self.url + "/" + installed_app_id
        return self._get_data(url)

    def update(self, installed_app_id):
        """This submits a request to the device to update the specified app to
        the latest version. The app must be managed for this request to succeed."""
        url = self.url + "/" + installed_app_id
        return self._get_data(url)

    def delete_app(self, installed_app_id):
        """This submits a request to the device to uninstall the specified app.
        The app must be managed for this request to succeed."""
        url = self.url + "/" + installed_app_id
        return self._delete_data(url)
