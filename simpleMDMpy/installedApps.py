#!/usr/bin/env python 

import simpleMDM

class installedApps(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/installed_apps")

    def getApp(self, installedAppID):
        url = self.url + "/" + installedAppID
        return self._getData(url)

    def deleteApp(self, installedAppID):
        url = self.url + "/" + installedAppID 
        return self._deleteData(url)