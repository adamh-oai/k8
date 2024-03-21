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
from .discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from .v1_endpoint import V1Endpoint
from .v1_object_meta import V1ObjectMeta

class V1EndpointSlice(BaseModel):
    """
    EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.  # noqa: E501
    """
    address_type: StrictStr = Field(..., alias="addressType", description="addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.")
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    endpoints: list[V1Endpoint] = Field(..., description="endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    ports: Optional[list[DiscoveryV1EndpointPort]] = Field(default=None, description="ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates \"all ports\". Each slice may include a maximum of 100 ports.")
    __properties = ["addressType", "apiVersion", "endpoints", "kind", "metadata", "ports"]

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
    def from_json(cls, json_str: str) -> V1EndpointSlice:
        """Create an instance of V1EndpointSlice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EndpointSlice:
        """Create an instance of V1EndpointSlice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EndpointSlice.parse_obj(obj)

        _obj = V1EndpointSlice.parse_obj({
            "address_type": obj.get("addressType"),
            "api_version": obj.get("apiVersion"),
            "endpoints": [V1Endpoint.from_dict(_item) for _item in obj.get("endpoints")] if obj.get("endpoints") is not None else None,
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "ports": [DiscoveryV1EndpointPort.from_dict(_item) for _item in obj.get("ports")] if obj.get("ports") is not None else None
        })
        return _obj

