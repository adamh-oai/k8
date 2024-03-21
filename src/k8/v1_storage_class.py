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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm

class V1StorageClass(BaseModel):
    """
    StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.  StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.  # noqa: E501
    """
    allow_volume_expansion: Optional[StrictBool] = Field(default=None, alias="allowVolumeExpansion", description="allowVolumeExpansion shows whether the storage class allow volume expand.")
    allowed_topologies: Optional[list[V1TopologySelectorTerm]] = Field(default=None, alias="allowedTopologies", description="allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.")
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    mount_options: Optional[list[StrictStr]] = Field(default=None, alias="mountOptions", description="mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. [\"ro\", \"soft\"]. Not validated - mount of the PVs will simply fail if one is invalid.")
    parameters: Optional[Dict[str, StrictStr]] = Field(default=None, description="parameters holds the parameters for the provisioner that should create volumes of this storage class.")
    provisioner: StrictStr = Field(..., description="provisioner indicates the type of the provisioner.")
    reclaim_policy: Optional[StrictStr] = Field(default=None, alias="reclaimPolicy", description="reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.")
    volume_binding_mode: Optional[StrictStr] = Field(default=None, alias="volumeBindingMode", description="volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.")
    __properties = ["allowVolumeExpansion", "allowedTopologies", "apiVersion", "kind", "metadata", "mountOptions", "parameters", "provisioner", "reclaimPolicy", "volumeBindingMode"]

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
    def from_json(cls, json_str: str) -> V1StorageClass:
        """Create an instance of V1StorageClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_topologies (list)
        _items = []
        if self.allowed_topologies:
            for _item in self.allowed_topologies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allowedTopologies'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1StorageClass:
        """Create an instance of V1StorageClass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1StorageClass.parse_obj(obj)

        _obj = V1StorageClass.parse_obj({
            "allow_volume_expansion": obj.get("allowVolumeExpansion"),
            "allowed_topologies": [V1TopologySelectorTerm.from_dict(_item) for _item in obj.get("allowedTopologies")] if obj.get("allowedTopologies") is not None else None,
            "api_version": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "mount_options": obj.get("mountOptions"),
            "parameters": obj.get("parameters"),
            "provisioner": obj.get("provisioner"),
            "reclaim_policy": obj.get("reclaimPolicy"),
            "volume_binding_mode": obj.get("volumeBindingMode")
        })
        return _obj


