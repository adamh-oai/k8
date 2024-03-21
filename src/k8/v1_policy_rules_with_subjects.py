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
from .flowcontrol_v1_subject import FlowcontrolV1Subject
from .v1_non_resource_policy_rule import V1NonResourcePolicyRule
from .v1_resource_policy_rule import V1ResourcePolicyRule

class V1PolicyRulesWithSubjects(BaseModel):
    """
    PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.  # noqa: E501
    """
    non_resource_rules: Optional[list[V1NonResourcePolicyRule]] = Field(default=None, alias="nonResourceRules", description="`nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.")
    resource_rules: Optional[list[V1ResourcePolicyRule]] = Field(default=None, alias="resourceRules", description="`resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.")
    subjects: list[FlowcontrolV1Subject] = Field(..., description="subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.")
    __properties = ["nonResourceRules", "resourceRules", "subjects"]

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
    def from_json(cls, json_str: str) -> V1PolicyRulesWithSubjects:
        """Create an instance of V1PolicyRulesWithSubjects from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in non_resource_rules (list)
        _items = []
        if self.non_resource_rules:
            for _item in self.non_resource_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nonResourceRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_rules (list)
        _items = []
        if self.resource_rules:
            for _item in self.resource_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subjects (list)
        _items = []
        if self.subjects:
            for _item in self.subjects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PolicyRulesWithSubjects:
        """Create an instance of V1PolicyRulesWithSubjects from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PolicyRulesWithSubjects.parse_obj(obj)

        _obj = V1PolicyRulesWithSubjects.parse_obj({
            "non_resource_rules": [V1NonResourcePolicyRule.from_dict(_item) for _item in obj.get("nonResourceRules")] if obj.get("nonResourceRules") is not None else None,
            "resource_rules": [V1ResourcePolicyRule.from_dict(_item) for _item in obj.get("resourceRules")] if obj.get("resourceRules") is not None else None,
            "subjects": [FlowcontrolV1Subject.from_dict(_item) for _item in obj.get("subjects")] if obj.get("subjects") is not None else None
        })
        return _obj


