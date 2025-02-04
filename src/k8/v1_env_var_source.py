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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector
from typing import Optional, Set
from typing_extensions import Self

class V1EnvVarSource(BaseModel):
    """
    EnvVarSource represents a source for the value of an EnvVar.
    """ # noqa: E501
    config_map_key_ref: Optional[V1ConfigMapKeySelector] = Field(default=None, alias="configMapKeyRef")
    field_ref: Optional[V1ObjectFieldSelector] = Field(default=None, alias="fieldRef")
    resource_field_ref: Optional[V1ResourceFieldSelector] = Field(default=None, alias="resourceFieldRef")
    secret_key_ref: Optional[V1SecretKeySelector] = Field(default=None, alias="secretKeyRef")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["configMapKeyRef", "fieldRef", "resourceFieldRef", "secretKeyRef"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1EnvVarSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config_map_key_ref
        if self.config_map_key_ref:
            _dict['configMapKeyRef'] = self.config_map_key_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of field_ref
        if self.field_ref:
            _dict['fieldRef'] = self.field_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_field_ref
        if self.resource_field_ref:
            _dict['resourceFieldRef'] = self.resource_field_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_key_ref
        if self.secret_key_ref:
            _dict['secretKeyRef'] = self.secret_key_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1EnvVarSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configMapKeyRef": V1ConfigMapKeySelector.from_dict(obj["configMapKeyRef"]) if obj.get("configMapKeyRef") is not None else None,
            "fieldRef": V1ObjectFieldSelector.from_dict(obj["fieldRef"]) if obj.get("fieldRef") is not None else None,
            "resourceFieldRef": V1ResourceFieldSelector.from_dict(obj["resourceFieldRef"]) if obj.get("resourceFieldRef") is not None else None,
            "secretKeyRef": V1SecretKeySelector.from_dict(obj["secretKeyRef"]) if obj.get("secretKeyRef") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


