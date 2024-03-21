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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus

class V2HorizontalPodAutoscalerStatus(BaseModel):
    """
    HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.  # noqa: E501
    """
    conditions: Optional[list[V2HorizontalPodAutoscalerCondition]] = Field(default=None, description="conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.")
    current_metrics: Optional[list[V2MetricStatus]] = Field(default=None, alias="currentMetrics", description="currentMetrics is the last read state of the metrics used by this autoscaler.")
    current_replicas: Optional[StrictInt] = Field(default=None, alias="currentReplicas", description="currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.")
    desired_replicas: StrictInt = Field(..., alias="desiredReplicas", description="desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.")
    last_scale_time: Optional[datetime] = Field(default=None, alias="lastScaleTime", description="lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.")
    observed_generation: Optional[StrictInt] = Field(default=None, alias="observedGeneration", description="observedGeneration is the most recent generation observed by this autoscaler.")
    __properties = ["conditions", "currentMetrics", "currentReplicas", "desiredReplicas", "lastScaleTime", "observedGeneration"]

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
    def from_json(cls, json_str: str) -> V2HorizontalPodAutoscalerStatus:
        """Create an instance of V2HorizontalPodAutoscalerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in current_metrics (list)
        _items = []
        if self.current_metrics:
            for _item in self.current_metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['currentMetrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2HorizontalPodAutoscalerStatus:
        """Create an instance of V2HorizontalPodAutoscalerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2HorizontalPodAutoscalerStatus.parse_obj(obj)

        _obj = V2HorizontalPodAutoscalerStatus.parse_obj({
            "conditions": [V2HorizontalPodAutoscalerCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "current_metrics": [V2MetricStatus.from_dict(_item) for _item in obj.get("currentMetrics")] if obj.get("currentMetrics") is not None else None,
            "current_replicas": obj.get("currentReplicas"),
            "desired_replicas": obj.get("desiredReplicas"),
            "last_scale_time": obj.get("lastScaleTime"),
            "observed_generation": obj.get("observedGeneration")
        })
        return _obj


