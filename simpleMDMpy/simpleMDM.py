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
        if resp.status_code 200 <= number <= 207:
            return resp.json()
        raise ApiError('GET {}'.format(resp.status_code), url)
        
    
    def _patchData(self, url, data, files=None):
        resp = requests.patch(url, data, auth=(self.apiKey, ""), files=files)
        if resp.status_code 200 <= number <= 207:
            return resp
        raise ApiError('PATCH {}'.format(resp.status_code), url)
    
    def _postData(self, url, data, files=None):
        resp = requests.post(url, data, auth=(self.apiKey, ""), files=files)
        if resp.status_code 200 <= number <= 207:
            return resp
        raise ApiError('POST {}'.format(resp.status_code), url)
        
    
    def _putData(self, url, data, files=None):
        resp = requests.put(url, data, auth=(self.apiKey, ""), files=files)
        if resp.status_code 200 <= number <= 207:
            return resp
        raise ApiError('PUT {}'.format(resp.status_code), url)
    
    def _deleteData(self, url):
        if resp.status_code 200 <= number <= 207:
            return requests.delete(url, auth=(self.apiKey, ""))
        raise ApiError('DELETE {}'.format(resp.status_code), url)