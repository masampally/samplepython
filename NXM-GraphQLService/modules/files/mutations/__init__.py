from graphene import AbstractType

from .rename_file import FileRenameResponse


class FilesMutate(AbstractType):
    renameFile = FileRenameResponse.Field()
