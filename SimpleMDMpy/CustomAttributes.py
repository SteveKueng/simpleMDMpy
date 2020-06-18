#!/usr/bin/env python

"""custom attributes module"""

import SimpleMDMpy.SimpleMDM

class CustomAttributes(SimpleMDMpy.SimpleMDM.Connection):
    """work with custom attributes"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/custom_attributes")

    def get_custom_attributes(self):
        """lists all custom attributes"""
        url = self.url
        data = {}
        return self._get_data(url, data)

    def create_custom_attribute(self, name):
        """create custom attribute"""
        url = self.url
        data = {'name': name}
        return self._post_data(url, data)

    def delete_custom_attribute(self, custom_attribute_id):
        """deletes custom attribute"""
        url = self.url + "/" + custom_attribute_id
        return self._delete_data(url)

