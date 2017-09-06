#!/usr/bin/env python 

import simpleMDM

class apps(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/apps")

    def getApp(self, appID="all"):
        url = self.url
        if not appID == "all":
            url = url + "/" + appID
        return self._getData(url)

    def createApp(self, name=None, appStoreID=None, bundleID=None, binary=None):
        data = {}
        files = {}
        if name:
            data['name'] = name
        if appStoreID:
            data['app_store_id'] = appStoreID
        elif bundleID:
            data['bundle_id'] = bundleID
        elif binary:
            files['binary'] = open(binary,'rb')
        return self._postData(self.url, data, files)
    
    def updateApp(self, appID, binary=None, name=None):
        url = self.url + "/" + appID
        data = {}
        files = {}
        if name:
            data['name'] = name
        if binary:
            files['binary'] = open(binary,'rb')
        return self._patchData(url, data, files)

    def deleteApp(self, appID):
        url = self.url + "/" + appID
        return self._deleteData(url)