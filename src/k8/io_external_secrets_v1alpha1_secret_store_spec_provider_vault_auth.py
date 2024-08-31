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
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_cert import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthCert
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_kubernetes import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_ldap import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap
from .io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_token_secret_ref import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthTokenSecretRef
from .io_external_secrets_v1alpha1_secret_store_spec_provider_vault_auth_app_role import IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthAppRole
from .io_external_secrets_v1alpha1_secret_store_spec_provider_vault_auth_jwt import IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthJwt
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuth(BaseModel):
    """
    Auth configures how secret-manager authenticates with the Vault server.
    """ # noqa: E501
    app_role: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthAppRole] = Field(default=None, alias="appRole")
    cert: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthCert] = None
    jwt: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthJwt] = None
    kubernetes: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes] = None
    ldap: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap] = None
    token_secret_ref: Optional[IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthTokenSecretRef] = Field(default=None, alias="tokenSecretRef")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["appRole", "cert", "jwt", "kubernetes", "ldap", "tokenSecretRef"]

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
        """Create an instance of IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuth from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_role
        if self.app_role:
            _dict['appRole'] = self.app_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cert
        if self.cert:
            _dict['cert'] = self.cert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jwt
        if self.jwt:
            _dict['jwt'] = self.jwt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kubernetes
        if self.kubernetes:
            _dict['kubernetes'] = self.kubernetes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ldap
        if self.ldap:
            _dict['ldap'] = self.ldap.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token_secret_ref
        if self.token_secret_ref:
            _dict['tokenSecretRef'] = self.token_secret_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appRole": IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthAppRole.from_dict(obj["appRole"]) if obj.get("appRole") is not None else None,
            "cert": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthCert.from_dict(obj["cert"]) if obj.get("cert") is not None else None,
            "jwt": IoExternalSecretsV1alpha1SecretStoreSpecProviderVaultAuthJwt.from_dict(obj["jwt"]) if obj.get("jwt") is not None else None,
            "kubernetes": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes.from_dict(obj["kubernetes"]) if obj.get("kubernetes") is not None else None,
            "ldap": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap.from_dict(obj["ldap"]) if obj.get("ldap") is not None else None,
            "tokenSecretRef": IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthTokenSecretRef.from_dict(obj["tokenSecretRef"]) if obj.get("tokenSecretRef") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

