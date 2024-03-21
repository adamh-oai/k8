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
from .v1_attached_volume import V1AttachedVolume
from .v1_container_image import V1ContainerImage
from .v1_node_address import V1NodeAddress
from .v1_node_condition import V1NodeCondition
from .v1_node_config_status import V1NodeConfigStatus
from .v1_node_daemon_endpoints import V1NodeDaemonEndpoints
from .v1_node_system_info import V1NodeSystemInfo

class V1NodeStatus(BaseModel):
    """
    NodeStatus is information about the current status of a node.  # noqa: E501
    """
    addresses: Optional[list[V1NodeAddress]] = Field(default=None, description="List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP).")
    allocatable: Optional[Dict[str, StrictStr]] = Field(default=None, description="Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.")
    capacity: Optional[Dict[str, StrictStr]] = Field(default=None, description="Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity")
    conditions: Optional[list[V1NodeCondition]] = Field(default=None, description="Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition")
    config: Optional[V1NodeConfigStatus] = None
    daemon_endpoints: Optional[V1NodeDaemonEndpoints] = Field(default=None, alias="daemonEndpoints")
    images: Optional[list[V1ContainerImage]] = Field(default=None, description="List of container images on this node")
    node_info: Optional[V1NodeSystemInfo] = Field(default=None, alias="nodeInfo")
    phase: Optional[StrictStr] = Field(default=None, description="NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.")
    volumes_attached: Optional[list[V1AttachedVolume]] = Field(default=None, alias="volumesAttached", description="List of volumes that are attached to the node.")
    volumes_in_use: Optional[list[StrictStr]] = Field(default=None, alias="volumesInUse", description="List of attachable volumes in use (mounted) by the node.")
    __properties = ["addresses", "allocatable", "capacity", "conditions", "config", "daemonEndpoints", "images", "nodeInfo", "phase", "volumesAttached", "volumesInUse"]

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
    def from_json(cls, json_str: str) -> V1NodeStatus:
        """Create an instance of V1NodeStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of daemon_endpoints
        if self.daemon_endpoints:
            _dict['daemonEndpoints'] = self.daemon_endpoints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of node_info
        if self.node_info:
            _dict['nodeInfo'] = self.node_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volumes_attached (list)
        _items = []
        if self.volumes_attached:
            for _item in self.volumes_attached:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumesAttached'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NodeStatus:
        """Create an instance of V1NodeStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NodeStatus.parse_obj(obj)

        _obj = V1NodeStatus.parse_obj({
            "addresses": [V1NodeAddress.from_dict(_item) for _item in obj.get("addresses")] if obj.get("addresses") is not None else None,
            "allocatable": obj.get("allocatable"),
            "capacity": obj.get("capacity"),
            "conditions": [V1NodeCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "config": V1NodeConfigStatus.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "daemon_endpoints": V1NodeDaemonEndpoints.from_dict(obj.get("daemonEndpoints")) if obj.get("daemonEndpoints") is not None else None,
            "images": [V1ContainerImage.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "node_info": V1NodeSystemInfo.from_dict(obj.get("nodeInfo")) if obj.get("nodeInfo") is not None else None,
            "phase": obj.get("phase"),
            "volumes_attached": [V1AttachedVolume.from_dict(_item) for _item in obj.get("volumesAttached")] if obj.get("volumesAttached") is not None else None,
            "volumes_in_use": obj.get("volumesInUse")
        })
        return _obj


