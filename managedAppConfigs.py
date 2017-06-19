#!/usr/bin/env python 

import simpleMDM

class managedAppConfigs(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/apps")

    def getManagedConfigs(self, appID):
        url = self.url + "/" + appID + "/managed_configs"
        return self._getData(url)

    def pushUpdates(self, appID):
        url = self.url + "/" + appID + "/managed_configs/push"
        return self._postData(url)