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
from pydantic import BaseModel, Field, StrictStr, conlist

class V1beta1NamedRuleWithOperations(BaseModel):
    """
    NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.  # noqa: E501
    """
    api_groups: Optional[list[StrictStr]] = Field(default=None, alias="apiGroups", description="APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.")
    api_versions: Optional[list[StrictStr]] = Field(default=None, alias="apiVersions", description="APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.")
    operations: Optional[list[StrictStr]] = Field(default=None, description="Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.")
    resource_names: Optional[list[StrictStr]] = Field(default=None, alias="resourceNames", description="ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.")
    resources: Optional[list[StrictStr]] = Field(default=None, description="Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.")
    scope: Optional[StrictStr] = Field(default=None, description="scope specifies the scope of this rule. Valid values are \"Cluster\", \"Namespaced\", and \"*\" \"Cluster\" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \"Namespaced\" means that only namespaced resources will match this rule. \"*\" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \"*\".")
    __properties = ["apiGroups", "apiVersions", "operations", "resourceNames", "resources", "scope"]

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
    def from_json(cls, json_str: str) -> V1beta1NamedRuleWithOperations:
        """Create an instance of V1beta1NamedRuleWithOperations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta1NamedRuleWithOperations:
        """Create an instance of V1beta1NamedRuleWithOperations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta1NamedRuleWithOperations.parse_obj(obj)

        _obj = V1beta1NamedRuleWithOperations.parse_obj({
            "api_groups": obj.get("apiGroups"),
            "api_versions": obj.get("apiVersions"),
            "operations": obj.get("operations"),
            "resource_names": obj.get("resourceNames"),
            "resources": obj.get("resources"),
            "scope": obj.get("scope")
        })
        return _obj


