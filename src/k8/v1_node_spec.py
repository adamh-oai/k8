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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint

class V1NodeSpec(BaseModel):
    """
    NodeSpec describes the attributes that a node is created with.  # noqa: E501
    """
    config_source: Optional[V1NodeConfigSource] = Field(default=None, alias="configSource")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalID", description="Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966")
    pod_cidr: Optional[StrictStr] = Field(default=None, alias="podCIDR", description="PodCIDR represents the pod IP range assigned to the node.")
    pod_cidrs: Optional[list[StrictStr]] = Field(default=None, alias="podCIDRs", description="podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.")
    provider_id: Optional[StrictStr] = Field(default=None, alias="providerID", description="ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>")
    taints: Optional[list[V1Taint]] = Field(default=None, description="If specified, the node's taints.")
    unschedulable: Optional[StrictBool] = Field(default=None, description="Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration")
    __properties = ["configSource", "externalID", "podCIDR", "podCIDRs", "providerID", "taints", "unschedulable"]

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
    def from_json(cls, json_str: str) -> V1NodeSpec:
        """Create an instance of V1NodeSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of config_source
        if self.config_source:
            _dict['configSource'] = self.config_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in taints (list)
        _items = []
        if self.taints:
            for _item in self.taints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NodeSpec:
        """Create an instance of V1NodeSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NodeSpec.parse_obj(obj)

        _obj = V1NodeSpec.parse_obj({
            "config_source": V1NodeConfigSource.from_dict(obj.get("configSource")) if obj.get("configSource") is not None else None,
            "external_id": obj.get("externalID"),
            "pod_cidr": obj.get("podCIDR"),
            "pod_cidrs": obj.get("podCIDRs"),
            "provider_id": obj.get("providerID"),
            "taints": [V1Taint.from_dict(_item) for _item in obj.get("taints")] if obj.get("taints") is not None else None,
            "unschedulable": obj.get("unschedulable")
        })
        return _obj


