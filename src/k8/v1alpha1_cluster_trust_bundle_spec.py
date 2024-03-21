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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class V1alpha1ClusterTrustBundleSpec(BaseModel):
    """
    ClusterTrustBundleSpec contains the signer and trust anchors.  # noqa: E501
    """
    signer_name: Optional[StrictStr] = Field(default=None, alias="signerName", description="signerName indicates the associated signer, if any.  In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.  If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.  If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.  List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.")
    trust_bundle: StrictStr = Field(..., alias="trustBundle", description="trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.")
    __properties = ["signerName", "trustBundle"]

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
    def from_json(cls, json_str: str) -> V1alpha1ClusterTrustBundleSpec:
        """Create an instance of V1alpha1ClusterTrustBundleSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1alpha1ClusterTrustBundleSpec:
        """Create an instance of V1alpha1ClusterTrustBundleSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1alpha1ClusterTrustBundleSpec.parse_obj(obj)

        _obj = V1alpha1ClusterTrustBundleSpec.parse_obj({
            "signer_name": obj.get("signerName"),
            "trust_bundle": obj.get("trustBundle")
        })
        return _obj

