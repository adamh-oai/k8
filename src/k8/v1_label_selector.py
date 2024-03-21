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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from .v1_label_selector_requirement import V1LabelSelectorRequirement

class V1LabelSelector(BaseModel):
    """
    A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.  # noqa: E501
    """
    match_expressions: Optional[list[V1LabelSelectorRequirement]] = Field(default=None, alias="matchExpressions", description="matchExpressions is a list of label selector requirements. The requirements are ANDed.")
    match_labels: Optional[Dict[str, StrictStr]] = Field(default=None, alias="matchLabels", description="matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.")
    __properties = ["matchExpressions", "matchLabels"]

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
    def from_json(cls, json_str: str) -> V1LabelSelector:
        """Create an instance of V1LabelSelector from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1LabelSelector:
        """Create an instance of V1LabelSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LabelSelector.parse_obj(obj)

        _obj = V1LabelSelector.parse_obj({
            "match_expressions": [V1LabelSelectorRequirement.from_dict(_item) for _item in obj.get("matchExpressions")] if obj.get("matchExpressions") is not None else None,
            "match_labels": obj.get("matchLabels")
        })
        return _obj


