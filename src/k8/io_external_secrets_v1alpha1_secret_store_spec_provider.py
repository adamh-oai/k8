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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from .io_external_secrets_v1alpha1_secret_store_spec_provider_akeyless import IoExternalSecretsV1alpha1SecretStoreSpecProviderAkeyless
from .io_external_secrets_v1alpha1_secret_store_spec_provider_alibaba import IoExternalSecretsV1alpha1SecretStoreSpecProviderAlibaba
from .io_external_secrets_v1alpha1_secret_store_spec_provider_aws import IoExternalSecretsV1alpha1SecretStoreSpecProviderAws
from .io_external_secrets_v1alpha1_secret_store_spec_provider_azurekv import IoExternalSecretsV1alpha1SecretStoreSpecProviderAzurekv
from .io_external_secrets_v1alpha1_secret_store_spec_provider_fake import IoExternalSecretsV1alpha1SecretStoreSpecProviderFake
from .io_external_secrets_v1alpha1_secret_store_spec_provider_gcpsm import IoExternalSecretsV1alpha1SecretStoreSpecProviderGcpsm
from .io_external_secrets_v1alpha1_secret_store_spec_provider_gitlab import IoExternalSecretsV1alpha1SecretStoreSpecProviderGitlab
from .io_external_secrets_v1alpha1_secret_store_spec_provider_ibm import IoExternalSecretsV1alpha1SecretStoreSpecProviderIbm
from .io_external_secrets_v1alpha1_secret_store_spec_provider_kubernetes import IoExternalSecretsV1alpha1SecretStoreSpecProviderKubernetes
from .io_external_secrets_v1alpha1_secret_store_spec_provider_oracle import IoExternalSecretsV1alpha1SecretStoreSpecProviderOracle
from .io_external_secrets_v1alpha1_secret_store_spec_provider_passworddepot import IoExternalSecretsV1alpha1SecretStoreSpecProviderPassworddepot
from .io_external_secrets_v1alpha1_secret_store_spec_provider_vault import IoExternalSecretsV1alpha1SecretStoreSpecProviderVault
from .io_external_secrets_v1alpha1_secret_store_spec_provider_webhook import IoExternalSecretsV1alpha1SecretStoreSpecProviderWebhook
from .io_external_secrets_v1alpha1_secret_store_spec_provider_yandexlockbox import IoExternalSecretsV1alpha1SecretStoreSpecProviderYandexlockbox
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsV1alpha1SecretStoreSpecProvider(BaseModel):
    """
    Used to configure the provider. Only one provider may be set
    """ # noqa: E501
    akeyless: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderAkeyless] = None
    alibaba: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderAlibaba] = None
    aws: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderAws] = None
    azurekv: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderAzurekv] = None
    fake: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderFake] = None
    gcpsm: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderGcpsm] = None
    gitlab: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderGitlab] = None
    ibm: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderIbm] = None
    kubernetes: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderKubernetes] = None
    oracle: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderOracle] = None
    passworddepot: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderPassworddepot] = None
    vault: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderVault] = None
    webhook: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderWebhook] = None
    yandexlockbox: Optional[IoExternalSecretsV1alpha1SecretStoreSpecProviderYandexlockbox] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["akeyless", "alibaba", "aws", "azurekv", "fake", "gcpsm", "gitlab", "ibm", "kubernetes", "oracle", "passworddepot", "vault", "webhook", "yandexlockbox"]

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
        """Create an instance of IoExternalSecretsV1alpha1SecretStoreSpecProvider from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of akeyless
        if self.akeyless:
            _dict['akeyless'] = self.akeyless.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alibaba
        if self.alibaba:
            _dict['alibaba'] = self.alibaba.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws
        if self.aws:
            _dict['aws'] = self.aws.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azurekv
        if self.azurekv:
            _dict['azurekv'] = self.azurekv.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fake
        if self.fake:
            _dict['fake'] = self.fake.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcpsm
        if self.gcpsm:
            _dict['gcpsm'] = self.gcpsm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gitlab
        if self.gitlab:
            _dict['gitlab'] = self.gitlab.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ibm
        if self.ibm:
            _dict['ibm'] = self.ibm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kubernetes
        if self.kubernetes:
            _dict['kubernetes'] = self.kubernetes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle
        if self.oracle:
            _dict['oracle'] = self.oracle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passworddepot
        if self.passworddepot:
            _dict['passworddepot'] = self.passworddepot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vault
        if self.vault:
            _dict['vault'] = self.vault.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yandexlockbox
        if self.yandexlockbox:
            _dict['yandexlockbox'] = self.yandexlockbox.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsV1alpha1SecretStoreSpecProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "akeyless": IoExternalSecretsV1alpha1SecretStoreSpecProviderAkeyless.from_dict(obj["akeyless"]) if obj.get("akeyless") is not None else None,
            "alibaba": IoExternalSecretsV1alpha1SecretStoreSpecProviderAlibaba.from_dict(obj["alibaba"]) if obj.get("alibaba") is not None else None,
            "aws": IoExternalSecretsV1alpha1SecretStoreSpecProviderAws.from_dict(obj["aws"]) if obj.get("aws") is not None else None,
            "azurekv": IoExternalSecretsV1alpha1SecretStoreSpecProviderAzurekv.from_dict(obj["azurekv"]) if obj.get("azurekv") is not None else None,
            "fake": IoExternalSecretsV1alpha1SecretStoreSpecProviderFake.from_dict(obj["fake"]) if obj.get("fake") is not None else None,
            "gcpsm": IoExternalSecretsV1alpha1SecretStoreSpecProviderGcpsm.from_dict(obj["gcpsm"]) if obj.get("gcpsm") is not None else None,
            "gitlab": IoExternalSecretsV1alpha1SecretStoreSpecProviderGitlab.from_dict(obj["gitlab"]) if obj.get("gitlab") is not None else None,
            "ibm": IoExternalSecretsV1alpha1SecretStoreSpecProviderIbm.from_dict(obj["ibm"]) if obj.get("ibm") is not None else None,
            "kubernetes": IoExternalSecretsV1alpha1SecretStoreSpecProviderKubernetes.from_dict(obj["kubernetes"]) if obj.get("kubernetes") is not None else None,
            "oracle": IoExternalSecretsV1alpha1SecretStoreSpecProviderOracle.from_dict(obj["oracle"]) if obj.get("oracle") is not None else None,
            "passworddepot": IoExternalSecretsV1alpha1SecretStoreSpecProviderPassworddepot.from_dict(obj["passworddepot"]) if obj.get("passworddepot") is not None else None,
            "vault": IoExternalSecretsV1alpha1SecretStoreSpecProviderVault.from_dict(obj["vault"]) if obj.get("vault") is not None else None,
            "webhook": IoExternalSecretsV1alpha1SecretStoreSpecProviderWebhook.from_dict(obj["webhook"]) if obj.get("webhook") is not None else None,
            "yandexlockbox": IoExternalSecretsV1alpha1SecretStoreSpecProviderYandexlockbox.from_dict(obj["yandexlockbox"]) if obj.get("yandexlockbox") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

