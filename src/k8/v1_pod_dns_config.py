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
from .v1_pod_dns_config_option import V1PodDNSConfigOption

class V1PodDNSConfig(BaseModel):
    """
    PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.  # noqa: E501
    """
    nameservers: Optional[list[StrictStr]] = Field(default=None, description="A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.")
    options: Optional[list[V1PodDNSConfigOption]] = Field(default=None, description="A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.")
    searches: Optional[list[StrictStr]] = Field(default=None, description="A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.")
    __properties = ["nameservers", "options", "searches"]

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
    def from_json(cls, json_str: str) -> V1PodDNSConfig:
        """Create an instance of V1PodDNSConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodDNSConfig:
        """Create an instance of V1PodDNSConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodDNSConfig.parse_obj(obj)

        _obj = V1PodDNSConfig.parse_obj({
            "nameservers": obj.get("nameservers"),
            "options": [V1PodDNSConfigOption.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None,
            "searches": obj.get("searches")
        })
        return _obj


