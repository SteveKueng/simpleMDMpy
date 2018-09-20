#!/usr/bin/env python 

import simpleMDM

class appGroups(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/app_groups")

    def getAppGroup(self, appGroupID="all"):
        url = self.url
        if not appGroupID == "all":
            url = url + "/" + appGroupID
        return self._getData(url)

    def createAppGroup(self, name, autoDeploy="true"):
        data = {'name': name, 'auto_deploy': autoDeploy}
        return self._postData(url, data)
    
    def updateAppGroup(self, appGroupID, name=None, autoDeploy="true"):
        url = self.url + "/" + appGroupID
        data = {}
        if name:
            data['name'] = name
        data['auto_deploy'] = autoDeploy
        return self._patchData(url, data)

    def deleteAppGroup(self, appGroupID):
        url = self.url + "/" + appGroupID
        return self._deleteData(url)

    def assignApp(self, appGroupID, appID):
        url = self.url + "/" + appGroupID + "/apps/" + appID
        data = {}
        return self._postData(url, data)
    
    def unAssignApp(self, appGroupID, appID):
        url = self.url + "/" + appGroupID + "/apps/" + appID
        data = {}
        return self._deleteData(self.url, data)
    
    def assignDeviceGroup(self, appGroupID, deviceGroupID):
        url = self.url + "/" + appGroupID + "/device_groups/" + deviceGroupID
        data = {}
        return self._postData(url, data)

    def unAssignDeviceGroup(self, appGroupID, deviceGroupID):
        url = self.url + "/" + appGroupID + "/device_groups/" + deviceGroupID
        data = {}
        return self._deleteData(url, data)
    
    def assignDevice(self, appGroupID, deviceID):
        url = self.url + "/" + appGroupID + "/devices/" + deviceID
        data = {}
        return self._postData(url, data)

    def unAssignDevice(self, appGroupID, deviceID):
        url = self.url + "/" + appGroupID + "/devices/" + deviceID
        data = {}
        return self._deleteData(url, data)

    def pushApps(self, appGroupID):
        url = self.url + "/" + appGroupID + "/push_apps"
        data = {}
        return self._postData(url, data)
    
    def updateApps(self, appGroupID):
        url = self.url + "/" + appGroupID + "/update_apps"
        data = {}
        return self._postData(url, data)
