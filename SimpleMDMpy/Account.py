#!/usr/bin/env python

"""accounts module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class Account(SimpleMDMpy.SimpleMDM.Connection):
    """account class provides auth and basic account details"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/account")

    def get_account_details(self):
        """returns account details as dict"""
        return self._get_data(self.url)

    def set_account_details(self, name=None, country_code=None):
        """set account detail"""
        data = {}
        if name:
            data['name'] = name
        if country_code:
            data['apple_store_country_code'] = country_code
        return self._patch_data(self.url, data)
