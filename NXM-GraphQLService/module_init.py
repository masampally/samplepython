from flask import Flask
from idgen import IdGen
from crm_data import GetCRMData
from security_interceptor import SecurityInterceptor
from ip_secure_checker import IpSecureChecker

import yaml
import logging


# initialise logging service
logging.basicConfig(filename='graphql.log', level=logging.DEBUG, format='%(asctime)s - %(threadName)s - %(levelname)-8s - %(message)s')


# initialise the configuration
# ############################################################################
# LOAD CLIENT CONFIGURATION
# ############################################################################
# loading configuration contents
config_file_handler = open("./application.yml", "r")
config = yaml.safe_load(config_file_handler)
# print(config)
config_file_handler.close()

# nid service URL
id_service_url = config['service']['id']
crm_service_url = config['service']['crm']
graphql_mapping = config['settings']['mapping']
debug = config['settings']['debug']
ws_service_url = config['service']['ws']
ip_service_url = config['service']['ipsecure']


# id generation service
idgen = IdGen(id_service_url)

# initialize crm api data service
crm_data_service = GetCRMData(crm_service_url)

# initialize ws api data service
security_interceptor = SecurityInterceptor(ws_service_url)

# 
ip_secure_checker = IpSecureChecker(ip_service_url, ws_service_url)

nid = idgen.getId()

# j_data = {}
# j_data['widgettype'] = 'default'
# j_data['displayname'] = 'title2'
# j_data['content'] = 'content'

# crm_data_service.putData('c996', 'widgets/91?user=srl.kranthi.saala', j_data)

# user_name = "srl.c2074.kranthi.saala"
# pin = 'pass'
# g_token = '619458' 
# # user login
# user_login = security_interceptor.user_login(user_name, pin, g_token)
# is_user_valid = user_login.get('succeed')
# print('user_login : {}'.format(user_login))
# token = None
# is_token_valid = None
# is_user_valid = True
# # validate token
# if (is_user_valid):       
#     # token = user_login.get('data')
#     token = 'D125D94ABA832107E4EFEC88CDB9B9FE6D4724CD7CF34377262E1E1FF2C2885D'
#     is_token_valid = security_interceptor.validate_token(token)
    
#     print(is_token_valid)

#     if (is_token_valid.get('succeed')):
#         print('is token valid')
#         session = token
#         ip = '172.20.11.111'
#         user_agent = 'kranthikumar1111'
#         ip_sc_result = ip_secure_checker.access(session, ip, user_agent)
#         print('ip_sc_result: {}'.format(ip_sc_result))
        
#         if not ip_sc_result:
#             security_interceptor.user_logout(token)
#             print('logout')
#         else:
#             print('go to next..')
            
    

# enable only development mode
app = Flask(__name__)