from graphene import ObjectType, Mutation, String, Boolean
from graphql import GraphQLError

      
class FileRenameResponse(Mutation) :
         
    class Arguments:
        token = String(required=True)
        uid = String(required=True)
        newname = String(required=True)    
    
    succeed = Boolean()
    msg = String()
    entityId = String()
    jobId = String ()
    
    def mutate(self, info, token, uid, newname):
        
        try:
            # api call
            succeed = True
            msg = newname
            entityId = '0'
            jobId = uid
            
            
        except Exception as e:
            
            raise GraphQLError("Error creating User object.", e)
        
        else:
            
            return FileRenameResponse(succeed=succeed,msg=msg,entityId=entityId,jobId=jobId)
            