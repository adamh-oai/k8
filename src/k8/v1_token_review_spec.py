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
from pydantic import BaseModel, Field, StrictStr, conlist

class V1TokenReviewSpec(BaseModel):
    """
    TokenReviewSpec is a description of the token authentication request.  # noqa: E501
    """
    audiences: Optional[list[StrictStr]] = Field(default=None, description="Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.")
    token: Optional[StrictStr] = Field(default=None, description="Token is the opaque bearer token.")
    __properties = ["audiences", "token"]

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
    def from_json(cls, json_str: str) -> V1TokenReviewSpec:
        """Create an instance of V1TokenReviewSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TokenReviewSpec:
        """Create an instance of V1TokenReviewSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TokenReviewSpec.parse_obj(obj)

        _obj = V1TokenReviewSpec.parse_obj({
            "audiences": obj.get("audiences"),
            "token": obj.get("token")
        })
        return _obj


