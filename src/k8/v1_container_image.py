# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class V1ContainerImage(BaseModel):
    """
    Describe a container image  # noqa: E501
    """
    names: Optional[list[StrictStr]] = Field(default=None, description="Names by which this image is known. e.g. [\"kubernetes.example/hyperkube:v1.0.7\", \"cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7\"]")
    size_bytes: Optional[StrictInt] = Field(default=None, alias="sizeBytes", description="The size of the image in bytes.")
    __properties = ["names", "sizeBytes"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1ContainerImage:
        """Create an instance of V1ContainerImage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ContainerImage:
        """Create an instance of V1ContainerImage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ContainerImage.parse_obj(obj)

        _obj = V1ContainerImage.parse_obj({
            "names": obj.get("names"),
            "size_bytes": obj.get("sizeBytes")
        })
        return _obj

