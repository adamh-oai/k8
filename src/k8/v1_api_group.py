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
from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR

class V1APIGroup(BaseModel):
    """
    APIGroup contains the name, the supported versions, and the preferred version of a group.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    name: StrictStr = Field(..., description="name is the name of the group.")
    preferred_version: Optional[V1GroupVersionForDiscovery] = Field(default=None, alias="preferredVersion")
    server_address_by_client_cidrs: Optional[list[V1ServerAddressByClientCIDR]] = Field(default=None, alias="serverAddressByClientCIDRs", description="a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.")
    versions: list[V1GroupVersionForDiscovery] = Field(..., description="versions are the versions supported in this group.")
    __properties = ["apiVersion", "kind", "name", "preferredVersion", "serverAddressByClientCIDRs", "versions"]

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
    def from_json(cls, json_str: str) -> V1APIGroup:
        """Create an instance of V1APIGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of preferred_version
        if self.preferred_version:
            _dict['preferredVersion'] = self.preferred_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in server_address_by_client_cidrs (list)
        _items = []
        if self.server_address_by_client_cidrs:
            for _item in self.server_address_by_client_cidrs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serverAddressByClientCIDRs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['versions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1APIGroup:
        """Create an instance of V1APIGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1APIGroup.parse_obj(obj)

        _obj = V1APIGroup.parse_obj({
            "api_version": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "preferred_version": V1GroupVersionForDiscovery.from_dict(obj.get("preferredVersion")) if obj.get("preferredVersion") is not None else None,
            "server_address_by_client_cidrs": [V1ServerAddressByClientCIDR.from_dict(_item) for _item in obj.get("serverAddressByClientCIDRs")] if obj.get("serverAddressByClientCIDRs") is not None else None,
            "versions": [V1GroupVersionForDiscovery.from_dict(_item) for _item in obj.get("versions")] if obj.get("versions") is not None else None
        })
        return _obj

