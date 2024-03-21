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
from pydantic import BaseModel, Field, StrictInt, conlist
from .v1_deployment_condition import V1DeploymentCondition

class V1DeploymentStatus(BaseModel):
    """
    DeploymentStatus is the most recently observed status of the Deployment.  # noqa: E501
    """
    available_replicas: Optional[StrictInt] = Field(default=None, alias="availableReplicas", description="Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.")
    collision_count: Optional[StrictInt] = Field(default=None, alias="collisionCount", description="Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.")
    conditions: Optional[list[V1DeploymentCondition]] = Field(default=None, description="Represents the latest available observations of a deployment's current state.")
    observed_generation: Optional[StrictInt] = Field(default=None, alias="observedGeneration", description="The generation observed by the deployment controller.")
    ready_replicas: Optional[StrictInt] = Field(default=None, alias="readyReplicas", description="readyReplicas is the number of pods targeted by this Deployment with a Ready Condition.")
    replicas: Optional[StrictInt] = Field(default=None, description="Total number of non-terminated pods targeted by this deployment (their labels match the selector).")
    unavailable_replicas: Optional[StrictInt] = Field(default=None, alias="unavailableReplicas", description="Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.")
    updated_replicas: Optional[StrictInt] = Field(default=None, alias="updatedReplicas", description="Total number of non-terminated pods targeted by this deployment that have the desired template spec.")
    __properties = ["availableReplicas", "collisionCount", "conditions", "observedGeneration", "readyReplicas", "replicas", "unavailableReplicas", "updatedReplicas"]

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
    def from_json(cls, json_str: str) -> V1DeploymentStatus:
        """Create an instance of V1DeploymentStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DeploymentStatus:
        """Create an instance of V1DeploymentStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DeploymentStatus.parse_obj(obj)

        _obj = V1DeploymentStatus.parse_obj({
            "available_replicas": obj.get("availableReplicas"),
            "collision_count": obj.get("collisionCount"),
            "conditions": [V1DeploymentCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "observed_generation": obj.get("observedGeneration"),
            "ready_replicas": obj.get("readyReplicas"),
            "replicas": obj.get("replicas"),
            "unavailable_replicas": obj.get("unavailableReplicas"),
            "updated_replicas": obj.get("updatedReplicas")
        })
        return _obj


