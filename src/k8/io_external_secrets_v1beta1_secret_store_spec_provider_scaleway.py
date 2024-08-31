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
from .io_external_secrets_v1beta1_secret_store_spec_provider_scaleway_access_key import IoExternalSecretsV1beta1SecretStoreSpecProviderScalewayAccessKey
from .io_external_secrets_v1beta1_secret_store_spec_provider_scaleway_secret_key import IoExternalSecretsV1beta1SecretStoreSpecProviderScalewaySecretKey
from typing import Optional, Set
from typing_extensions import Self

class IoExternalSecretsV1beta1SecretStoreSpecProviderScaleway(BaseModel):
    """
    Scaleway
    """ # noqa: E501
    access_key: IoExternalSecretsV1beta1SecretStoreSpecProviderScalewayAccessKey = Field(alias="accessKey")
    api_url: Optional[StrictStr] = Field(default=None, description="APIURL is the url of the api to use. Defaults to https://api.scaleway.com", alias="apiUrl")
    project_id: StrictStr = Field(description="ProjectID is the id of your project, which you can find in the console: https://console.scaleway.com/project/settings", alias="projectId")
    region: StrictStr = Field(description="Region where your secrets are located: https://developers.scaleway.com/en/quickstart/#region-and-zone")
    secret_key: IoExternalSecretsV1beta1SecretStoreSpecProviderScalewaySecretKey = Field(alias="secretKey")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["accessKey", "apiUrl", "projectId", "region", "secretKey"]

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
        """Create an instance of IoExternalSecretsV1beta1SecretStoreSpecProviderScaleway from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_key
        if self.access_key:
            _dict['accessKey'] = self.access_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_key
        if self.secret_key:
            _dict['secretKey'] = self.secret_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoExternalSecretsV1beta1SecretStoreSpecProviderScaleway from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": IoExternalSecretsV1beta1SecretStoreSpecProviderScalewayAccessKey.from_dict(obj["accessKey"]) if obj.get("accessKey") is not None else None,
            "apiUrl": obj.get("apiUrl"),
            "projectId": obj.get("projectId"),
            "region": obj.get("region"),
            "secretKey": IoExternalSecretsV1beta1SecretStoreSpecProviderScalewaySecretKey.from_dict(obj["secretKey"]) if obj.get("secretKey") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


