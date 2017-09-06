#!/usr/bin/env python 

import simpleMDM

class pushCertificate(simpleMDM.connection):
    def __init__(self, apiKey):
        simpleMDM.connection.__init__(self, apiKey)
        self.url = self._url("/push_certificate")

    def getPushCertificate(self):
        return self._getData(self.url)

    def updateCertificate(self, file, appleID=None):
        files = {'file': open(file,'rb')}
        data = {}
        if appleID:
            data["apple_id"] = appleID
        return self._putData(self.url, data, files)
    
    def getSignedCSR(self):
        return self._getData(self.url + "/scsr")