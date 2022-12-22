from graphene import ObjectType, Schema

from module_init import crm_data_service

# Categories
from modules.categories.queries import CategoriesQuery

# Files
from modules.files.queries import FilesQuery
from modules.files.mutations import FilesMutate

class Query(
    CategoriesQuery, 
    FilesQuery, 
    ObjectType
    ):
    pass


class Mutation(
    FilesMutate,
    ObjectType
    ):
    pass




schema = Schema(query=Query, mutation=Mutation)