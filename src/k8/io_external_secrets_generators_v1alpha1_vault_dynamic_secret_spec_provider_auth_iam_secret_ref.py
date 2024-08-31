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
from .io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_access_key_id_secret_ref import IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef
from .io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_secret_access_key_secret_ref import IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef
from .io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_session_token_secret_ref import IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSessionTokenSecretRef
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthIamSecretRef(BaseModel):
    """
    Specify credentials in a Secret object
    """ # noqa: E501
    access_key_id_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef] = Field(default=None, alias="accessKeyIDSecretRef")
    secret_access_key_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef] = Field(default=None, alias="secretAccessKeySecretRef")
    session_token_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSessionTokenSecretRef] = Field(default=None, alias="sessionTokenSecretRef")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["accessKeyIDSecretRef", "secretAccessKeySecretRef", "sessionTokenSecretRef"]

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
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthIamSecretRef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key_id_secret_ref
        if self.access_key_id_secret_ref:
            _dict['accessKeyIDSecretRef'] = self.access_key_id_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_access_key_secret_ref
        if self.secret_access_key_secret_ref:
            _dict['secretAccessKeySecretRef'] = self.secret_access_key_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session_token_secret_ref
        if self.session_token_secret_ref:
            _dict['sessionTokenSecretRef'] = self.session_token_secret_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthIamSecretRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKeyIDSecretRef": IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefAccessKeyIDSecretRef.from_dict(obj["accessKeyIDSecretRef"]) if obj.get("accessKeyIDSecretRef") is not None else None,
            "secretAccessKeySecretRef": IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSecretAccessKeySecretRef.from_dict(obj["secretAccessKeySecretRef"]) if obj.get("secretAccessKeySecretRef") is not None else None,
            "sessionTokenSecretRef": IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthSecretRefSessionTokenSecretRef.from_dict(obj["sessionTokenSecretRef"]) if obj.get("sessionTokenSecretRef") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


