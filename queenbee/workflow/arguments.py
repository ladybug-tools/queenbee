from typing import Union, List
from pydantic import Field

from ..base.basemodel import BaseModel
from ..io.common import IOBase

from ..recipe.artifact_source import HTTP, S3, ProjectFolder


class ArgumentArtifact(BaseModel):
    """A workflow Artifact Argument"""

    name: str = Field(
        ...,
        description='The name of the artifact'
    )

    source: Union[HTTP, S3, ProjectFolder] = Field(
        ...,
        description='The source to pull the artifact from'
    )


class ArgumentParameter(BaseModel):
    """A workflow Parameter Argument"""

    name: str = Field(
        ...,
        description='The name of the parameter'
    )

    value: str = Field(
        ...,
        description='The value of the parameter'
    )


class Arguments(IOBase):
    """Workflow Arguments"""

    artifacts: List[ArgumentArtifact] = Field(
        [],
        description='A list of input artifacts'
    )

    parameters: List[ArgumentParameter] = Field(
        [],
        description='A list of input parameters'
    )
