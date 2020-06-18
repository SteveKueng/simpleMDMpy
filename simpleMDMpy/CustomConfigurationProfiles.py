#!/usr/bin/env python

""" Custom Configuration Profiles module """

import SimpleMDMpy.SimpleMDM

class CustomConfigurationProfiles(SimpleMDMpy.SimpleMDM.Connection):
    """work with custom profiles"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/custom_configuration_profiles")

    def get_profiles(self):
        """returns profiles"""
        url = self.url
        return self._get_data(url)

    def create_profile(self, name, mobileconfig, user_scope=None, attribute_support=False):
        """upload a config file"""
        url = self.url
        data = {'name': name}
        files = {'mobileconfig': open(mobileconfig, 'rb')}
        if user_scope:
            data['user_scope'] = user_scope
        if attribute_support:
            data['attribute_support'] = attribute_support
        return self._post_data(url, data, files)

    def update_profile(self, profile_id, name=None, mobileconfig=None,\
    user_scope=None, attribute_support=None):
        """update a config file"""
        url = self.url + "/" + profile_id
        data = {}
        files = {}
        if name:
            data['name'] = name
        if mobileconfig:
            files['mobileconfig'] = open(mobileconfig, 'rb')
        if user_scope:
            data['user_scope'] = user_scope
        if attribute_support:
            data['attribute_support'] = attribute_support
        return self._patch_data(url, data, files)


    def delete_profile(self, profile_id):
        """deletes custom profile"""
        url = self.url + "/" + profile_id
        return self._delete_data(url)

    def assign_to_device_group(self, profile_id, device_group_id):
        """assigns custom profile to group"""
        url = self.url + "/" + profile_id + "/device_groups/" + device_group_id
        data = {}
        return self._post_data(url, data)

    def unassign_from_device_group(self, profile_id, device_group_id):
        """deletes profile from device group"""
        url = self.url + "/" + profile_id + "/device_groups/" + device_group_id
        return self._delete_data(url)
