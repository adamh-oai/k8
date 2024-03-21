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
from pydantic import BaseModel, Field, conlist
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile

class V1DownwardAPIProjection(BaseModel):
    """
    Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.  # noqa: E501
    """
    items: Optional[list[V1DownwardAPIVolumeFile]] = Field(default=None, description="Items is a list of DownwardAPIVolume file")
    __properties = ["items"]

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
    def from_json(cls, json_str: str) -> V1DownwardAPIProjection:
        """Create an instance of V1DownwardAPIProjection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DownwardAPIProjection:
        """Create an instance of V1DownwardAPIProjection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DownwardAPIProjection.parse_obj(obj)

        _obj = V1DownwardAPIProjection.parse_obj({
            "items": [V1DownwardAPIVolumeFile.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj


