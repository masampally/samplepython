from graphene import ObjectType, String, List, Int
from graphql import GraphQLError
from module_init import crm_data_service
from module_init import security_interceptor

class FileSystem(ObjectType):
    fileid = Int()
    folderid  = String()
    name =  String()
    ext = String()
    uploadedby = String()
    uploadedon = String()
    filesize = Int()
    path = String()
    description = String()
    
class GetFileSystem(ObjectType):
    getFileSystem = List(FileSystem, token=String(required=True), folderId=Int(required=True))
    
    def resolve_getFileSystem(self, request, token, folderId):  
        is_token_valid = None
        is_token_valid = security_interceptor.validate_token(token)
        # if (is_token_valid):
            # print(token)
               
        client_code = 'c996'
        # folder_id = 0
        router_path = 'folders/{}/files'.format(folderId)
        query_params = {}
        query_params['user'] = 'srl.nas.kranthi.saala'
        query_params['type'] = 'file'
        crm_data = crm_data_service.getData(client_code, router_path, query_params)
        api_data = crm_data
        data = [dict(zip(api_data[0], row)) for row in api_data[1:]]
        
        if data:
            return data
        else:
              raise GraphQLError("Error note!!")

