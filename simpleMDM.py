#!/usr/bin/env python 

import requests

class ApiError(Exception):
    pass

class connection:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def _url(self, path):
        return 'https://a.simplemdm.com/api/v1' + path

    def _getData(self, url):
        resp = requests.get(url, auth=(self.apiKey, ""))
        if resp.status_code != 200:
            raise ApiError('GET {}'.format(resp.status_code), url)
        return resp.json()
    
    def _patchData(self, url, data):
        resp = requests.patch(url, data, auth=(self.apiKey, ""))
        if resp.status_code != 200:
            raise ApiError('PATCH {}'.format(resp.status_code), url)
        return resp
    
    def _postData(self, url, data):
        resp = requests.post(url, data, auth=(self.apiKey, ""))
        if resp.status_code != 200:
            raise ApiError('POST {}'.format(resp.status_code), url)
        return resp
    
    def _deleteData(self, url):
        return requests.delete(url, auth=(self.apiKey, ""))