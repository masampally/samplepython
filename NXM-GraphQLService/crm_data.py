import logging
import requests
import time
import json

class GetCRMData:
    
    def __init__(self, crm_service_url):
        super().__init__()
        self.crm_service_url = crm_service_url
        self.url_prefix = '/crm'
    
    # get data from CRM
    def getData(self, client_code, router_path, query_params):
        
        request_url = '{}{}/{}/{}'.format(self.crm_service_url, self.url_prefix, client_code, router_path)
        resp_data = self.__safe_request_get(request_url, query_params)   
        return resp_data
    
    # get data with safe guard
    def __safe_request_get(self, request_url, query_params=None):

        response = None

        for retry_count in range(0, 5):
            try:
                # conditionally append the parameters
                if (query_params == None):
                    response = requests.get(request_url)
                else:
                    response = requests.get(request_url, params = query_params)

                # we only return if the response is 200 (success)
                if (response.status_code == 200):                   
                    return response.json()                
                    
            except:
                    time.sleep(1)

        # in the worst case, we return the last response if all requests fails
        return response
    
    # post data to CRM
    def postData(self, client_code, router_path, query_params, is_json):   
        
        request_url = '{}{}/{}/{}'.format(self.crm_service_url, self.url_prefix, client_code, router_path)
        resp_data = self.__safe_request_post(request_url, is_json, query_params)   
        return resp_data
    
    # post data with safe guard
    def __safe_request_post(self, request_url, is_json, query_params=None):       
        
        response = None

        for retry_count in range(0, 5):
            try:
                # conditionally append the parameters
                if (is_json):
                    response = requests.post(request_url, json=json.dump(query_params))                    
                else:
                    requests.post(request_url, params=query_params)

                # we only return if the response is 200 (success)
                if (response.status_code == 200):                   
                    return response.json()                
                    
            except:
                    time.sleep(1)

        # in the worst case, we return the last response if all requests fails
        return response
    
    
    # put data to CRM
    def putData(self, client_code, router_path, query_params, is_json, json_data):   
        
        request_url = '{}{}/{}/{}'.format(self.crm_service_url, self.url_prefix, client_code, router_path)
        resp_data = self.__safe_request_post(request_url, is_json, query_params)   
        return resp_data
    
    # put data with safe guard
    def __safe_request_put(self, request_url, is_json, query_params=None, json_data=None):       
        
        response = None

        for retry_count in range(0, 5):
            try:
                # conditionally append the parameters
                if (is_json):
                    response = requests.put(request_url, params=query_params, json=json.dump(json_data))                    
                else:
                    requests.put(request_url, params=query_params)

                # we only return if the response is 200 (success)
                if (response.status_code == 200):                   
                    return response.json()                
                    
            except:
                    time.sleep(1)

        # in the worst case, we return the last response if all requests fails
        return response
    
    