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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from .v1_local_object_reference import V1LocalObjectReference

class V1ISCSIVolumeSource(BaseModel):
    """
    Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.  # noqa: E501
    """
    chap_auth_discovery: Optional[StrictBool] = Field(default=None, alias="chapAuthDiscovery", description="chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication")
    chap_auth_session: Optional[StrictBool] = Field(default=None, alias="chapAuthSession", description="chapAuthSession defines whether support iSCSI Session CHAP authentication")
    fs_type: Optional[StrictStr] = Field(default=None, alias="fsType", description="fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi")
    initiator_name: Optional[StrictStr] = Field(default=None, alias="initiatorName", description="initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.")
    iqn: StrictStr = Field(..., description="iqn is the target iSCSI Qualified Name.")
    iscsi_interface: Optional[StrictStr] = Field(default=None, alias="iscsiInterface", description="iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).")
    lun: StrictInt = Field(..., description="lun represents iSCSI Target Lun number.")
    portals: Optional[list[StrictStr]] = Field(default=None, description="portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).")
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly", description="readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.")
    secret_ref: Optional[V1LocalObjectReference] = Field(default=None, alias="secretRef")
    target_portal: StrictStr = Field(..., alias="targetPortal", description="targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).")
    __properties = ["chapAuthDiscovery", "chapAuthSession", "fsType", "initiatorName", "iqn", "iscsiInterface", "lun", "portals", "readOnly", "secretRef", "targetPortal"]

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
    def from_json(cls, json_str: str) -> V1ISCSIVolumeSource:
        """Create an instance of V1ISCSIVolumeSource from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1ISCSIVolumeSource:
        """Create an instance of V1ISCSIVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ISCSIVolumeSource.parse_obj(obj)

        _obj = V1ISCSIVolumeSource.parse_obj({
            "chap_auth_discovery": obj.get("chapAuthDiscovery"),
            "chap_auth_session": obj.get("chapAuthSession"),
            "fs_type": obj.get("fsType"),
            "initiator_name": obj.get("initiatorName"),
            "iqn": obj.get("iqn"),
            "iscsi_interface": obj.get("iscsiInterface"),
            "lun": obj.get("lun"),
            "portals": obj.get("portals"),
            "read_only": obj.get("readOnly"),
            "secret_ref": V1LocalObjectReference.from_dict(obj.get("secretRef")) if obj.get("secretRef") is not None else None,
            "target_portal": obj.get("targetPortal")
        })
        return _obj


