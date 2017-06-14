#!/usr/bin/env python 

import simpleMDM

class devices(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/device_groups")

    def getDeviceGroup(self, deviceGoupID="all"):
        url = self.url
        if not deviceGoupID == "all":
            url = url + "/" + deviceGoupID
        return self._getData(url)

    def assignDevice(self, deviceID, deviceGoupID):
        url = self.url + "/" + deviceGoupID + "/devices/" + deviceID
        data = {}
        return self._postData(url, data)