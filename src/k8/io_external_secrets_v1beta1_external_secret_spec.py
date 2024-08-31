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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref import IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef
from .io_external_secrets_v1beta1_external_secret_spec_data_from_inner import IoExternalSecretsV1beta1ExternalSecretSpecDataFromInner
from .io_external_secrets_v1beta1_external_secret_spec_data_inner import IoExternalSecretsV1beta1ExternalSecretSpecDataInner
from .io_external_secrets_v1beta1_external_secret_spec_target import IoExternalSecretsV1beta1ExternalSecretSpecTarget
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsV1beta1ExternalSecretSpec(BaseModel):
    """
    ExternalSecretSpec defines the desired state of ExternalSecret.
    """ # noqa: E501
    data: Optional[List[IoExternalSecretsV1beta1ExternalSecretSpecDataInner]] = Field(default=None, description="Data defines the connection between the Kubernetes Secret keys and the Provider data")
    data_from: Optional[List[IoExternalSecretsV1beta1ExternalSecretSpecDataFromInner]] = Field(default=None, description="DataFrom is used to fetch all properties from a specific Provider data If multiple entries are specified, the Secret keys are merged in the specified order", alias="dataFrom")
    refresh_interval: Optional[StrictStr] = Field(default=None, description="RefreshInterval is the amount of time before the values are read again from the SecretStore provider Valid time units are \"ns\", \"us\" (or \"µs\"), \"ms\", \"s\", \"m\", \"h\" May be set to zero to fetch and create it once. Defaults to 1h.", alias="refreshInterval")
    secret_store_ref: Optional[IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef] = Field(default=None, alias="secretStoreRef")
    target: Optional[IoExternalSecretsV1beta1ExternalSecretSpecTarget] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["data", "dataFrom", "refreshInterval", "secretStoreRef", "target"]

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
        """Create an instance of IoExternalSecretsV1beta1ExternalSecretSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_from (list)
        _items = []
        if self.data_from:
            for _item in self.data_from:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataFrom'] = _items
        # override the default output from pydantic by calling `to_dict()` of secret_store_ref
        if self.secret_store_ref:
            _dict['secretStoreRef'] = self.secret_store_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsV1beta1ExternalSecretSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [IoExternalSecretsV1beta1ExternalSecretSpecDataInner.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "dataFrom": [IoExternalSecretsV1beta1ExternalSecretSpecDataFromInner.from_dict(_item) for _item in obj["dataFrom"]] if obj.get("dataFrom") is not None else None,
            "refreshInterval": obj.get("refreshInterval"),
            "secretStoreRef": IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef.from_dict(obj["secretStoreRef"]) if obj.get("secretStoreRef") is not None else None,
            "target": IoExternalSecretsV1beta1ExternalSecretSpecTarget.from_dict(obj["target"]) if obj.get("target") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

