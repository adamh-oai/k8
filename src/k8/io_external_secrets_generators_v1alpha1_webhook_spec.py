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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from .io_external_secrets_generators_v1alpha1_webhook_spec_ca_provider import IoExternalSecretsGeneratorsV1alpha1WebhookSpecCaProvider
from .io_external_secrets_generators_v1alpha1_webhook_spec_result import IoExternalSecretsGeneratorsV1alpha1WebhookSpecResult
from .io_external_secrets_generators_v1alpha1_webhook_spec_secrets_inner import IoExternalSecretsGeneratorsV1alpha1WebhookSpecSecretsInner
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsGeneratorsV1alpha1WebhookSpec(BaseModel):
    """
    WebhookSpec controls the behavior of the external generator. Any body parameters should be passed to the server through the parameters field.
    """ # noqa: E501
    body: Optional[StrictStr] = Field(default=None, description="Body")
    ca_bundle: Optional[Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]]] = Field(default=None, description="PEM encoded CA bundle used to validate webhook server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection.", alias="caBundle")
    ca_provider: Optional[IoExternalSecretsGeneratorsV1alpha1WebhookSpecCaProvider] = Field(default=None, alias="caProvider")
    headers: Optional[Dict[str, StrictStr]] = Field(default=None, description="Headers")
    method: Optional[StrictStr] = Field(default=None, description="Webhook Method")
    result: IoExternalSecretsGeneratorsV1alpha1WebhookSpecResult
    secrets: Optional[List[IoExternalSecretsGeneratorsV1alpha1WebhookSpecSecretsInner]] = Field(default=None, description="Secrets to fill in templates These secrets will be passed to the templating function as key value pairs under the given name")
    timeout: Optional[StrictStr] = Field(default=None, description="Timeout")
    url: StrictStr = Field(description="Webhook url to call")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["body", "caBundle", "caProvider", "headers", "method", "result", "secrets", "timeout", "url"]

    @field_validator('ca_bundle')
    def ca_bundle_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
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
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1WebhookSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ca_provider
        if self.ca_provider:
            _dict['caProvider'] = self.ca_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secrets (list)
        _items = []
        if self.secrets:
            for _item in self.secrets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secrets'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsGeneratorsV1alpha1WebhookSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "caBundle": obj.get("caBundle"),
            "caProvider": IoExternalSecretsGeneratorsV1alpha1WebhookSpecCaProvider.from_dict(obj["caProvider"]) if obj.get("caProvider") is not None else None,
            "headers": obj.get("headers"),
            "method": obj.get("method"),
            "result": IoExternalSecretsGeneratorsV1alpha1WebhookSpecResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "secrets": [IoExternalSecretsGeneratorsV1alpha1WebhookSpecSecretsInner.from_dict(_item) for _item in obj["secrets"]] if obj.get("secrets") is not None else None,
            "timeout": obj.get("timeout"),
            "url": obj.get("url")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


