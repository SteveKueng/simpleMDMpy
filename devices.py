#!/usr/bin/env python 

import simpleMDM

class devices(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/devices")

    def getDevice(self, deviceID="all"):
        """retruns a device specified by id. If no ID is specified all devices will be returned"""
        url = self.url
        if not deviceID == "all":
            url = url + "/" + deviceID
        return self._getData(url)

    def listInstalledApps(self, deviceID):
        url = self.url + "/" + deviceID + "/installed_apps"
        return self._getData(url)

    def createDevice(self, name, groupID):
        data = {'name': name, 'group_id': groupID}
        return self._postData(self.url, data)
    
    def updateDevice(self, name, deviceID):
        url = self.url + "/" + deviceID
        data = {'name': name}
        return self._patchData(url, data)

    def deleteDevice(self, deviceID):
        url = self.url + "/" + deviceID
        return self._deleteData(url)
    
    def lockDevice(self, deviceID, message, phone_number):
        url = self.url + "/" + deviceID + "/lock"
        data = {'message': message, 'phone_number': phone_number}
        return self._postData(url, data)
    
    def clearPasscodeDevice(self, deviceID):
        url = self.url + "/" + deviceID + "/clear_passcode"
        data = {}
        return self._postData(url, data)
    
    def wipeDevice(self, deviceID):
        url = self.url + "/" + deviceID + "/wipe"
        data = {}
        return self._postData(url, data)
    
    def pushAppsDevice(self, deviceID):
        url = self.url + "/" + deviceID + "/push_apps"
        data = {}
        return self._postData(url, data)