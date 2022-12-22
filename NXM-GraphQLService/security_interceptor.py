# SecurityInterceptor
import logging
import requests
import json
from flask import request

# from module_init import app

class SecurityInterceptor:
  
    def __init__(self, ws_service_url):
        self.ws_service_url = ws_service_url
        
    def validate_token(self, token):
        """Validate token

        Args:
            token (string): token

        Returns:
            Boolean: True / False
        """
        # GET http://cs1wsi.srlglobal.local/api/context?token=A4E11882B4290EE16690642AD4AA46AABE168661A7AA74C3FBFB877C630CAB38
        prefix = '/api/context'        
        request_url = '{}{}'.format(self.ws_service_url, prefix)
        query_params = {}
        query_params['token'] = token
        # response = requests.get(request_url, params=query_params)
        logging.info('UserIP: {}'.format(request.remote_addr))
        # print(app.request.remote_addr)
        with requests.get(request_url, params=query_params, stream=True) as response:
            ip, port = response.raw._connection.sock.getpeername()
            logging.info('Remote IP: {} - PORT: {}'.format(ip, port))
            # print('IP: {}'.format(response.META.get('HTTP_X_FORWARDED_FOR')))
                    
            if (response.status_code == 200):                         
                return {'succeed': True, 'msg': '', 'data': response.json()}
            else :            
                return {'succeed': False, 'msg': response.json(), 'data': None}
               
        
        
    def user_login(self, user, pin, rsa):
        """[summary]

        Args:
            user_name ([type]): [description]
            pin ([type]): [description]
            token ([type]): [description]

        Returns:
            [type]: [description]
        """
        prefix = '/api/login'        
        request_url = '{}{}'.format(self.ws_service_url, prefix)
        query_params = {}
        query_params['user'] = user
        query_params['pin'] = pin
        query_params['rsa'] = rsa
        response = requests.get(request_url, params=query_params)       
        
        if (response.status_code == 200):                         
            return {'succeed': True, 'msg': '', 'data': response.json().get('data')}
        else :            
            return {'succeed': False, 'msg': response.json(), 'data': None}
        
       
    def user_logout(self, token):
        """[summary]

        Args:
            token ([type]): [description]

        Returns:
            [type]: [description]
        """
        prefix = '/api/logout'        
        request_url = '{}{}'.format(self.ws_service_url, prefix)
        query_params = {}
        query_params['token'] = token        
        response = requests.get(request_url, params=query_params)
        
        print('login info: {}'.format(response.json())) 
        
        # if (response.status_code == 200):                         
        #     return {'succeed': True, 'msg': '', 'data': response.json().get('data')}
        # else :            
        #     return {'succeed': False, 'msg': response.json(), 'data': None}
        
    def get_user_client_code(self, token):
        is_token_valid = None
        is_token_valid = self.validate_token(token)
        if (is_token_valid and is_token_valid.get('succeed')):            
            session = token
            ip = '172.20.11.111'
            user_agent = 'kranthikumar1111'
            ip_sc_result = ip_secure_checker.access(session, ip, user_agent)
            print('ip_sc_result: {}'.format(ip_sc_result))
            
            if not ip_sc_result:
                security_interceptor.user_logout(token)
                print('logout')
            else:
                print('go to next..')
        else :            
            return is_token_valid