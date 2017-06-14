#!/usr/bin/env python 

import json
import simpleMDM

class account(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/account")
    
    def getAcountDetais(self):
        """retruns account details as dict"""
        return self._getData(self.url)
    
    def setAcountDetais(self, name=None, country_code=None):
        """set account detail"""
        data = {}
        if name:
            data['name'] = name
        if country_code:
            data['apple_store_country_code'] = country_code
        return self._patchData(self.url, data)
        