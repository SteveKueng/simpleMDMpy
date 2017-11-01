#!/usr/bin/env python 

import requests

class ApiError(Exception):
    pass

class connection:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def _url(self, path):
        return 'https://a.simplemdm.com/api/v1' + path

    def _getData(self, url, data=None):
        resp = requests.get(url, data, auth=(self.apiKey, ""))
        return resp.json()
        
    
    def _patchData(self, url, data, files=None):
        resp = requests.patch(url, data, auth=(self.apiKey, ""), files=files)
        return resp
    
    def _postData(self, url, data, files=None):
        resp = requests.post(url, data, auth=(self.apiKey, ""), files=files)
        return resp
        
    
    def _putData(self, url, data, files=None):
        resp = requests.put(url, data, auth=(self.apiKey, ""), files=files)
        return resp
    
    def _deleteData(self, url):
        return requests.delete(url, auth=(self.apiKey, ""))