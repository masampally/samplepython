import logging
import requests
import time

class IdGen:
    
    def __init__(self, id_service_url):
        super().__init__()
        self.id_service_url = id_service_url
    

    # create a unique file / folder Id for this process
    def getId(self, inc=1, key='nexusstorage'):

        # we need to make sure the file name generated is unique, therefore
        # invoke the process from cnid service
        nid_params = {"key" : key, "inc" : str(inc)}
        # nid_resp = requests.get(config["service"]["id"] + "api/id", params=nid_params)
        request_url = self.id_service_url + "/api/id"
        nid_resp = self.__safe_request_get(request_url, query_params=nid_params, jsoncast=False)
        config_id = nid_resp.json()
        unique_id = str(config_id)

        return unique_id
    
    # INX-4000 : INFRA - PDF service generation failure when under load
    # retry to fetch a data from a URL for a limit time until succeed. 
    # if the request fails, continue until run out of retries
    #
    # request_url : request url
    # query_params : optional query parameters
    # jsoncast : if the result should be cast to json
    #
    def __safe_request_get(self, request_url, query_params = None, jsoncast=True):

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
                    if (jsoncast):
                        result = response.json()
                        return result
                    else:
                        return response
            except:
                    time.sleep(1)

        # in the worst case, we return the last response if all requests fails
        return response