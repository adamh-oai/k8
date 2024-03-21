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
from .v1_scoped_resource_selector_requirement import V1ScopedResourceSelectorRequirement

class V1ScopeSelector(BaseModel):
    """
    A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.  # noqa: E501
    """
    match_expressions: Optional[list[V1ScopedResourceSelectorRequirement]] = Field(default=None, alias="matchExpressions", description="A list of scope selector requirements by scope of the resources.")
    __properties = ["matchExpressions"]

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
    def from_json(cls, json_str: str) -> V1ScopeSelector:
        """Create an instance of V1ScopeSelector from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in match_expressions (list)
        _items = []
        if self.match_expressions:
            for _item in self.match_expressions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchExpressions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ScopeSelector:
        """Create an instance of V1ScopeSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ScopeSelector.parse_obj(obj)

        _obj = V1ScopeSelector.parse_obj({
            "match_expressions": [V1ScopedResourceSelectorRequirement.from_dict(_item) for _item in obj.get("matchExpressions")] if obj.get("matchExpressions") is not None else None
        })
        return _obj


