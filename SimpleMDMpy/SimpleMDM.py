#!/usr/bin/env python

"""base module for calling simplemdm api"""
#pylint: disable=invalid-name

from builtins import str
from builtins import range
from builtins import object
import json
import requests

class ApiError(Exception):
    """Catch for API Error"""
    pass

class Connection(object): #pylint: disable=old-style-class,too-few-public-methods
    """create connection with api key"""
    proxyDict = dict()

    def __init__(self, api_key):
        self.api_key = api_key

    def _url(self, path): #pylint: disable=no-self-use
        """base api url"""
        return 'https://a.simplemdm.com/api/v1' + path

    def _get_data(self, url, data=None):
        """GET call to SimpleMDM API"""
        id = 0 #pylint: disable=invalid-name,redefined-builtin
        has_more = True
        resp_data = []
        while has_more:
            url = url + "?limit=20&starting_after=" + str(id)
            resp = requests.get(url, data, auth=(self.api_key, ""), proxies=self.proxyDict)
            resp_json = resp.json()
            if not resp.status_code in range(200, 207):
                break
            has_more = resp_json.get('has_more', None)
            if has_more is None:
                resp_data = resp_json['data']
                break
            else:
                resp_data = resp_data + resp_json['data']
                id = resp.json()['data'][-1].get('id') #pylint: disable=invalid-name
        resp_json['data'] = resp_data
        return resp

    def _patch_data(self, url, data, files=None):
        """PATCH call to SimpleMDM API"""
        resp = requests.patch(url, data, auth=(self.api_key, ""), \
            files=files, proxies=self.proxyDict)
        return resp

    def _post_data(self, url, data, files=None):
        """POST call to SimpleMDM API"""
        resp = requests.post(url, data, auth=(self.api_key, ""), \
            files=files, proxies=self.proxyDict)
        return resp

    def _put_data(self, url, data, files=None):
        """PUT call to SimpleMDM API"""
        resp = requests.put(url, data, auth=(self.api_key, ""), \
            files=files, proxies=self.proxyDict)
        return resp

    def _delete_data(self, url):
        """DELETE call to SimpleMDM API"""
        return requests.delete(url, auth=(self.api_key, ""), proxies=self.proxyDict)
