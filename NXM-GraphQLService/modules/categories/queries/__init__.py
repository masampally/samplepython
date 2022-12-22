from graphene import ObjectType

from .get_categories import GetCategories


class CategoriesQuery(GetCategories, ObjectType):
    pass
