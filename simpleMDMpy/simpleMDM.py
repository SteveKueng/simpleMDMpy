#!/usr/bin/env python 

import requests
import json

class ApiError(Exception):
    pass

class connection:
    proxyDict = dict()

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def _url(self, path):
        return 'https://a.simplemdm.com/api/v1' + path

    def _getData(self, url, data=None):
        id = 0
        has_more = True
        respData = []
        while has_more:
            url = url + "?limit=20&starting_after=" + str(id)
            resp = requests.get(url, data, auth=(self.apiKey, ""), proxies=self.proxyDict)
            respJson = resp.json()
            if not resp.status_code in range(200,207):
                break
            respData = respData + respJson['data']
            has_more = respJson['has_more']
            id = resp.json()['data'][-1].get('id')
        
        respJson['data'] = respData
        resp.encoding, resp._content = 'utf8', json.dumps(respJson)
        return resp
        
    def _patchData(self, url, data, files=None):
        resp = requests.patch(url, data, auth=(self.apiKey, ""), files=files, proxies=self.proxyDict)
        return resp
    
    def _postData(self, url, data, files=None):
        resp = requests.post(url, data, auth=(self.apiKey, ""), files=files, proxies=self.proxyDict)
        return resp
        
    def _putData(self, url, data, files=None):
        resp = requests.put(url, data, auth=(self.apiKey, ""), files=files, proxies=self.proxyDict)
        return resp
    
    def _deleteData(self, url):
        return requests.delete(url, auth=(self.apiKey, ""), proxies=self.proxyDict)