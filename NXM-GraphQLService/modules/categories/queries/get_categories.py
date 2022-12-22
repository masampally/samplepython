from graphene import ObjectType, String, List
from graphql import GraphQLError
from module_init import crm_data_service

class Category(ObjectType):
    name = String()
    description = String()
    owner = String()
    createdon = String()
    
class GetCategories(ObjectType):
    getCategories = List(Category)
    
    def resolve_getCategories(self, request):          
        
        client_code = 'c996'
        router_path = 'categories'
        query_params = {}
        query_params['user'] = 'srl.nas.kranthi.saala'
        query_params['template'] = 'false'
        crm_data = crm_data_service.getData(client_code, router_path, query_params)
        api_data = crm_data
        data = [dict(zip(api_data[0], row)) for row in api_data[1:]]
        
        if data:
            return data
        else:
              raise GraphQLError("Error note!")
        

        