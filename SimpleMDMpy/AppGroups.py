#!/usr/bin/env python

"""App Groups module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class AppGroups(SimpleMDMpy.SimpleMDM.Connection):
    """App Groups class provides interaction with Application Groups"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/app_groups")

    def get_app_group(self, app_group_id="all"):
        """Get an app group, defaults to 'all' if 'app_group_id' is not present"""
        url = self.url
        if app_group_id != 'all':
            url = url + "/" + app_group_id
        return self._get_data(url)

    def create_app_group(self, name, auto_deploy="true"):
        """create app group"""
        url = self.url
        data = {'name': name, 'auto_deploy': auto_deploy}
        return self._post_data(url, data)

    def update_app_group(self, app_group_id, name=None, auto_deploy="true"):
        """update app group"""
        url = self.url + "/" + app_group_id
        data = {}
        if name:
            data['name'] = name
        data['auto_deploy'] = auto_deploy
        return self._patch_data(url, data)

    def delete_app_group(self, app_group_id):
        """remove app group"""
        url = self.url + "/" + app_group_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args

    def assign_app(self, app_group_id, app_id):
        """remove app group from group"""
        url = self.url + "/" + app_group_id + "/apps/" + app_id
        data = {}
        return self._post_data(url, data)

    def un_assign_app(self, app_group_id, app_id):
        """unassign app from app group"""
        url = self.url + "/" + app_group_id + "/apps/" + app_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args

    def assign_device_group(self, app_group_id, device_group_id):
        """assign device group from app group"""
        url = self.url + "/" + app_group_id + "/device_groups/" + device_group_id
        data = {}
        return self._post_data(url, data)

    def un_assign_device_group(self, app_group_id, device_group_id):
        """remove device group from app group"""
        url = self.url + "/" + app_group_id + "/device_groups/" + device_group_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args

    def assign_device(self, app_group_id, device_id):
        """assign device to app group"""
        url = self.url + "/" + app_group_id + "/devices/" + str(device_id)
        data = {}
        return self._post_data(url, data)

    def un_assign_device(self, app_group_id, device_id):
        """unassign apps in app group"""
        url = self.url + "/" + app_group_id + "/devices/" + str(device_id)
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args

    def push_apps(self, app_group_id):
        """push apps in app group"""
        url = self.url + "/" + app_group_id + "/push_apps"
        data = {}
        return self._post_data(url, data)

    def update_apps(self, app_group_id):
        """update apps"""
        url = self.url + "/" + app_group_id + "/update_apps"
        data = {}
        return self._post_data(url, data)
