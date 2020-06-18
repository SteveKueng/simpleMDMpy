#!/usr/bin/env python

""" apps module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class Apps(SimpleMDMpy.SimpleMDM.Connection):
    """ apps module for SimpleMDMpy"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/apps")

    def get_app(self, app_id="all"):
        """list app, if none specified all return"""
        url = self.url
        if app_id != 'all':
            url = url + "/" + app_id
        return self._get_data(url)

    def create_app(self, name=None, app_store_id=None, bundle_id=None, binary=None):
        """upload an app binary"""
        data = {}
        files = {}
        if name:
            data['name'] = name
        if app_store_id:
            data['app_store_id'] = app_store_id
        elif bundle_id:
            data['bundle_id'] = bundle_id
        elif binary:
            files['binary'] = open(binary, 'rb')
        return self._post_data(self.url, data, files)

    def update_app(self, app_id, binary=None, name=None):
        """update an apps info binary etc"""
        url = self.url + "/" + app_id
        data = {}
        files = {}
        if name:
            data['name'] = name
        if binary:
            files['binary'] = open(binary, 'rb')
        return self._patch_data(url, data, files)

    def delete_app(self, app_id):
        """delete an app"""
        url = self.url + "/" + app_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args
