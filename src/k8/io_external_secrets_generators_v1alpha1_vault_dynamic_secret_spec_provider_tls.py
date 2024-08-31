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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_tls_cert_secret_ref import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsCertSecretRef
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_tls_key_secret_ref import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsKeySecretRef
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTls(BaseModel):
    """
    The configuration used for client side related TLS communication, when the Vault server requires mutual authentication. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. It's worth noting this configuration is different from the \"TLS certificates auth method\", which is available under the `auth.cert` section.
    """ # noqa: E501
    cert_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsCertSecretRef] = Field(default=None, alias="certSecretRef")
    key_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsKeySecretRef] = Field(default=None, alias="keySecretRef")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["certSecretRef", "keySecretRef"]

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
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTls from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cert_secret_ref
        if self.cert_secret_ref:
            _dict['certSecretRef'] = self.cert_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of key_secret_ref
        if self.key_secret_ref:
            _dict['keySecretRef'] = self.key_secret_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTls from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certSecretRef": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsCertSecretRef.from_dict(obj["certSecretRef"]) if obj.get("certSecretRef") is not None else None,
            "keySecretRef": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderTlsKeySecretRef.from_dict(obj["keySecretRef"]) if obj.get("keySecretRef") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

