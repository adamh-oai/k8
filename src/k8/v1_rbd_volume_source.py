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
from .v1_local_object_reference import V1LocalObjectReference

class V1RBDVolumeSource(BaseModel):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.  # noqa: E501
    """
    fs_type: Optional[StrictStr] = Field(default=None, alias="fsType", description="fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd")
    image: StrictStr = Field(..., description="image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    keyring: Optional[StrictStr] = Field(default=None, description="keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    monitors: list[StrictStr] = Field(..., description="monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    pool: Optional[StrictStr] = Field(default=None, description="pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly", description="readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    secret_ref: Optional[V1LocalObjectReference] = Field(default=None, alias="secretRef")
    user: Optional[StrictStr] = Field(default=None, description="user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it")
    __properties = ["fsType", "image", "keyring", "monitors", "pool", "readOnly", "secretRef", "user"]

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
    def from_json(cls, json_str: str) -> V1RBDVolumeSource:
        """Create an instance of V1RBDVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RBDVolumeSource:
        """Create an instance of V1RBDVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RBDVolumeSource.parse_obj(obj)

        _obj = V1RBDVolumeSource.parse_obj({
            "fs_type": obj.get("fsType"),
            "image": obj.get("image"),
            "keyring": obj.get("keyring"),
            "monitors": obj.get("monitors"),
            "pool": obj.get("pool"),
            "read_only": obj.get("readOnly"),
            "secret_ref": V1LocalObjectReference.from_dict(obj.get("secretRef")) if obj.get("secretRef") is not None else None,
            "user": obj.get("user")
        })
        return _obj


