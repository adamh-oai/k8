# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.29.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsV1alpha1ExternalSecretSpecDataInnerRemoteRef(BaseModel):
    """
    ExternalSecretDataRemoteRef defines Provider data location.
    """ # noqa: E501
    conversion_strategy: Optional[StrictStr] = Field(default=None, description="Used to define a conversion Strategy", alias="conversionStrategy")
    key: StrictStr = Field(description="Key is the key used in the Provider, mandatory")
    var_property: Optional[StrictStr] = Field(default=None, description="Used to select a specific property of the Provider value (if a map), if supported", alias="property")
    version: Optional[StrictStr] = Field(default=None, description="Used to select a specific version of the Provider value, if supported")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["conversionStrategy", "key", "property", "version"]

    @field_validator('conversion_strategy')
    def conversion_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Default', 'Unicode']):
            raise ValueError("must be one of enum values ('Default', 'Unicode')")
        return value

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
        """Create an instance of IoExternalSecretsV1alpha1ExternalSecretSpecDataInnerRemoteRef from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsV1alpha1ExternalSecretSpecDataInnerRemoteRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conversionStrategy": obj.get("conversionStrategy"),
            "key": obj.get("key"),
            "property": obj.get("property"),
            "version": obj.get("version")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


