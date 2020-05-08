"""Queenbee utility functions."""
import hashlib
import json
import collections
from typing import List, Dict

import yaml
from pydantic import BaseModel as PydanticBaseModel

from .parser import parse_file
from .variable import get_ref_variable


# set up yaml.dump to keep the order of the input dictionary
# from https://stackoverflow.com/a/31609484/4394669
def _keep_name_order_in_yaml():
    represent_dict_order = \
        lambda self, data:  self.represent_mapping(
            'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(dict, represent_dict_order)


_keep_name_order_in_yaml()


class BaseModel(PydanticBaseModel):
    """BaseModel with functionality to return the object as a yaml string."""

    def yaml(self, exclude_unset=False):
        return yaml.dump(
            json.loads(self.json(by_alias=True, exclude_unset=exclude_unset)),
            default_flow_style=False
        )

    def to_dict(self, exclude_unset=False, by_alias=True):
        return self.dict(exclude_unset=exclude_unset, by_alias=by_alias)

    def to_json(self, filepath, indent=None):
        """Write workflow to a JSON file.

        Args:
            filepath(str): Full path to JSON file.
        """
        # workflow = self.to_dict(by_alias=True)
        with open(filepath, 'w') as file:
            file.write(self.json(by_alias=True, exclude_unset=False, indent=indent))

    def to_yaml(self, filepath):
        """Write workflow to a yaml file."""
        content = self.yaml(exclude_unset=True)

        with open(filepath, 'w') as out_file:
            out_file.write(content)

    @classmethod
    def from_file(cls, filepath):
        """Create an object from YAML or JSON file."""
        # load file with place_holders
        data = parse_file(filepath)
        # now use pydantic to load all the info
        return cls.parse_obj(data)

    def __repr__(self):
        return self.yaml()

    @property
    def __hash__(self):
        return hashlib.sha256(
            self.json(by_alias=True, exclude_unset=False).encode('utf-8')
            ).hexdigest()

    def _referenced_values(self, var_names: List[str]) -> Dict[str, List[str]]:
        """Get all referenced values specified by var name"""
        ref_values = {}

        for name in var_names:
            value = getattr(self, name, None)

            if isinstance(value, str):
                ref_var = get_ref_variable(value)

                if ref_var != []:
                    ref_values[name] = ref_var
        
        return ref_values


def find_dup_items(values: List) -> List:
    """Find duplicate items in a list."""
    dup = [t for t, c in collections.Counter(values).items() if c > 1]
    return dup