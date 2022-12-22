# Ip Secure Checker


import logging
import requests

class IpSecureChecker:
    
    def __init__(self, ip_service_url, ws_service_url):
      self.ip_service_url = ip_service_url
      
    def access(self, session, ip, user_agent):
        """[Verify the user agent is secure]

        Args:
            session (string): token
            ip (string): ip address
            user_agent (string): browser information (ip and agent)

        Returns:
            [Boolean]: [Response of user access True or False]
        """
        # "session": "A4E11882B4290EE16690642AD4AA46AABE168661A7AA74C3FBFB877C630CAB38",
        # "ipv4": "172.17.0.178",
        # "user_agent": "kranthikumar1"
        prefix = '/access'        
        request_url = '{}{}'.format(self.ip_service_url, prefix)
        query_params = {}        
        query_params['session'] = session
        query_params['ipv4'] = ip
        query_params['user_agent'] = user_agent
        
        response = requests.post(request_url, json=query_params)
        print(response)
        
        if (response.status_code == 200):
            # print(response.json())              
            return True
        else :       
            # call logout from web service  
            return False
        
        
        
       