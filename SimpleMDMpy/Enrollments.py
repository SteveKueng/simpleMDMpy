#!/usr/bin/env python

"""enrollments module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class Enrollments(SimpleMDMpy.SimpleMDM.Connection):
    """enrollments module for SimpleMDMpy"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/enrollments")

    def get_enrollments(self, enrollment_id="all"):
        """get a devices group"""
        url = self.url
        if enrollment_id != 'all':
            url = url + "/" + enrollment_id
        data = {}
        return self._get_data(url, data)

    def send_invitation(self, enrollment_id, contact):
        """Send an enrollment invitation to an email address or phone number."""
        url = self.url + "/" + enrollment_id + "/invitations"
        data = {'contact': contact}
        return self._post_data(url, data)

    def delete_enrollment(self, enrollment_id):
        """delete enrollment"""
        url = self.url + "/" + enrollment_id
        data = {}
        return self._delete_data(url, data) #pylint: disable=too-many-function-args
