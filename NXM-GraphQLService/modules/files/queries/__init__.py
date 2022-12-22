from graphene import ObjectType

from .get_file_system import GetFileSystem


    
class FilesQuery(GetFileSystem, ObjectType):
    pass
