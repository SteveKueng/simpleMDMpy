#!/usr/bin/env python

"""Logs module for SimpleMDMpy"""

import SimpleMDMpy.SimpleMDM

class Logs(SimpleMDMpy.SimpleMDM.Connection):
    """GET all the LOGS"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/logs")

    def get_logs(self):
        """And I mean all the LOGS, before pagination"""
        url = self.url
        data = {}
        return self._get_data(url, data)
