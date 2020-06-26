#!/usr/bin/env python

"""Methods related to the Apple Push Notification
Certificate utilized by the account."""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class PushCertificate(SimpleMDMpy.SimpleMDM.Connection):
    """Push cert module actions"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/push_certificate")

    def getpush_certificate(self):
        """Show details related to the current push
        certificate being used."""
        return self._get_data(self.url)

    def update_certificate(self, file, apple_id):
        """Upload a new certificate and replace the
        existing certificate for your account."""
        files = {'file': open(file, 'rb')}
        data = {}
        if apple_id:
            data["apple_id"] = apple_id
        return self._put_data(self.url, data, files)

    def get_signed_csr(self):
        """Download a signed CSR file. This file is
        provided to Apple when creating and renewing a
        push certificate. The API returns a base64
        encoded plist for upload to the Apple Push
        Certificates Portal. The value of the data
        key can be uploaded to Apple as is"""
        return self._get_data(self.url + "/scsr")
