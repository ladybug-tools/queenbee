import os
from typing import List, Union, Dict
from datetime import datetime
from pydantic import Field, validator

from ..base.basemodel import BaseModel
from ..operator.metadata import MetaData as OperatorMetadata
from ..recipe.metadata import MetaData as RecipeMetadata

from ..operator import Operator
from ..recipe import Recipe

from .package import OperatorVersion, RecipeVersion


class RepositoryIndex(BaseModel):
    
    generated: datetime = Field(
        None,
        description='The timestamp at which the index was generated'
    )

    operator: Dict[str, List[OperatorVersion]] = Field(
        {},
        description='A dict of operators accessible by name. Each name key points to a list of operator versions'
    )

    recipe: Dict[str, List[RecipeVersion]] = Field(
        {},
        description='A dict of recipes accessible by name. Each name key points to a list of recipesversions'
    )


    @classmethod
    def from_folder(cls, folder_path):

        index = cls.parse_obj({})
        
        for package in os.listdir(os.path.join(folder_path, 'operators')):
            package_path = os.path.join(folder_path, 'operators', package)
            resource_version = OperatorVersion.from_package(package_path)
            index.index_operator_version(resource_version)

        for package in os.listdir(os.path.join(folder_path, 'recipes')):
            package_path = os.path.join(folder_path, 'recipes', package)
            resource_version = RecipeVersion.from_package(package_path)
            index.index_recipe_version(resource_version)

        return index

    @classmethod
    def index_resource(
        cls,
        index_folder: str,
        resource: Union[Operator, Recipe],
        path_to_readme: str = None,
        overwrite: bool = False,
    ):
        """Package an Operator or Workflow and add it to an existing index.json file

        Arguments:
            index_folder {str} -- The folder where the repository index is located
            resource {Union[Operator, Recipe]} -- The Operator or Recipe to package

        Keyword Arguments:
            overwrite {bool} -- Indicate whether overwriting an existing package or index entry is allowed (default: {False})

        Raises:
            ValueError: Error raised if the package already exists in the index file or directory
        """
        index_folder = os.path.abspath(index_folder)

        index_path = os.path.join(index_folder, 'index.json')

        index = cls.from_file(os.path.join(index_folder, 'index.json'))

        if isinstance(resource, Operator):
            type_path = 'operators'
            resource_version_class = OperatorVersion
        elif isinstance(resource, Recipe):
            type_path = 'recipes'
            resource_version_class = RecipeVersion
        else:
            raise ValueError(f"Resource should be an Operator or a Recipe")
        
        resource_version = resource_version_class.package_resource(
            resource=resource,
            repo_folder=index_folder,
            path_to_readme=path_to_readme,
        )

        try:        
            if isinstance(resource, Operator):
                index.index_operator_version(resource_version, overwrite)
            elif isinstance(resource, Recipe):
                index.index_recipe_version(resource_version, overwrite)
        except ValueError as error:
            # os.remove(package_abs_path)
            raise error

        index.to_json(index_path)


    @staticmethod
    def _index_resource_version(
        resource_dict: Dict[str, List[Union[RecipeVersion, OperatorVersion]]],
        resource_version: Union[RecipeVersion, OperatorVersion],
        overwrite: bool = False,
        skip: bool = False
    ):
        resource_list = resource_dict.get(resource_version.name, [])

        if not overwrite:
            match = filter(lambda x: x.version == resource_version.version, resource_list)
            if next(match, None) is not None:
                raise ValueError(f'Resource {resource_version.name} already has a version {resource_version.version} in the index')

        resource_list = list(filter(lambda x: x.version != resource_version.version, resource_list))

        resource_list.append(resource_version)
        resource_dict[resource_version.name] = resource_list

        return resource_dict

    def index_recipe_version(self, recipe_version: RecipeVersion, overwrite: bool = False):
        self.recipe = self._index_resource_version(self.recipe, recipe_version, overwrite)
        self.generated = datetime.utcnow()

    def index_operator_version(self, operator_version: OperatorVersion, overwrite: bool = False):
        self.operator = self._index_resource_version(self.operator, operator_version, overwrite)
        self.generated = datetime.utcnow()


    def merge_folder(self, folder_path, overwrite: bool = False, skip: bool = False):
        
        for package in os.listdir(os.path.join(folder_path, 'operators')):
            package_path = os.path.join(folder_path, 'operators', package)
            resource_version = OperatorVersion.from_package(package_path)
            try:
                self.index_operator_version(resource_version, overwrite)
            except ValueError as error:
                if 'already has a version ' in str(error):
                    if skip:
                        continue
                raise error

        for package in os.listdir(os.path.join(folder_path, 'recipes')):
            package_path = os.path.join(folder_path, 'recipes', package)
            resource_version = RecipeVersion.from_package(package_path)
            try:
                self.index_recipe_version(resource_version, overwrite)
            except ValueError as error:
                if 'already has a version ' in str(error):
                    if skip:
                        continue
                raise error


    def package_by_version(
        self,
        package_type: str,
        package_name: str,
        package_version: str
    ) -> Union[OperatorVersion, RecipeVersion]:
        package_dict = getattr(self, package_type)

        package_list = package_dict.get(package_name)

        if package_list is None:
            raise ValueError(f'No {package_type} package with name {package_name} exists in this index')

        res = next(filter(lambda x: x.version == package_version, package_list), None)

        if res is None:
            raise ValueError(f'No {package_type} package with name {package_name} and version {package_version} exists in this index')

        return res

    def package_by_digest(
        self,
        package_type: str,
        package_name: str,
        package_digest: str
    ) -> Union[OperatorVersion, RecipeVersion]:
        package_dict = getattr(self, package_type)

        package_list = package_dict.get(package_name)

        if package_list is None:
            raise ValueError(f'No {package_type} package with name {package_name} exists in this index')

        res = next(filter(lambda x: x.digest == package_digest, package_list), None)

        if res is None:
            raise ValueError(f'No {package_type} package with name {package_name} and digest {package_digest} exists in this index')

        return res