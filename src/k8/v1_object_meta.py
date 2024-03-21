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
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from .v1_managed_fields_entry import V1ManagedFieldsEntry
from .v1_owner_reference import V1OwnerReference

class V1ObjectMeta(BaseModel):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.  # noqa: E501
    """
    annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations")
    creation_timestamp: Optional[datetime] = Field(default=None, alias="creationTimestamp", description="CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata")
    deletion_grace_period_seconds: Optional[StrictInt] = Field(default=None, alias="deletionGracePeriodSeconds", description="Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.")
    deletion_timestamp: Optional[datetime] = Field(default=None, alias="deletionTimestamp", description="DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata")
    finalizers: Optional[list[StrictStr]] = Field(default=None, description="Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.")
    generate_name: Optional[StrictStr] = Field(default=None, alias="generateName", description="GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will return a 409.  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency")
    generation: Optional[StrictInt] = Field(default=None, description="A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels")
    managed_fields: Optional[list[V1ManagedFieldsEntry]] = Field(default=None, alias="managedFields", description="ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.")
    name: Optional[StrictStr] = Field(default=None, description="Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names")
    namespace: Optional[StrictStr] = Field(default=None, description="Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces")
    owner_references: Optional[list[V1OwnerReference]] = Field(default=None, alias="ownerReferences", description="List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.")
    resource_version: Optional[StrictStr] = Field(default=None, alias="resourceVersion", description="An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency")
    self_link: Optional[StrictStr] = Field(default=None, alias="selfLink", description="Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.")
    uid: Optional[StrictStr] = Field(default=None, description="UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids")
    __properties = ["annotations", "creationTimestamp", "deletionGracePeriodSeconds", "deletionTimestamp", "finalizers", "generateName", "generation", "labels", "managedFields", "name", "namespace", "ownerReferences", "resourceVersion", "selfLink", "uid"]

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
    def from_json(cls, json_str: str) -> V1ObjectMeta:
        """Create an instance of V1ObjectMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in managed_fields (list)
        _items = []
        if self.managed_fields:
            for _item in self.managed_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['managedFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in owner_references (list)
        _items = []
        if self.owner_references:
            for _item in self.owner_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ownerReferences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ObjectMeta:
        """Create an instance of V1ObjectMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ObjectMeta.parse_obj(obj)

        _obj = V1ObjectMeta.parse_obj({
            "annotations": obj.get("annotations"),
            "creation_timestamp": obj.get("creationTimestamp"),
            "deletion_grace_period_seconds": obj.get("deletionGracePeriodSeconds"),
            "deletion_timestamp": obj.get("deletionTimestamp"),
            "finalizers": obj.get("finalizers"),
            "generate_name": obj.get("generateName"),
            "generation": obj.get("generation"),
            "labels": obj.get("labels"),
            "managed_fields": [V1ManagedFieldsEntry.from_dict(_item) for _item in obj.get("managedFields")] if obj.get("managedFields") is not None else None,
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "owner_references": [V1OwnerReference.from_dict(_item) for _item in obj.get("ownerReferences")] if obj.get("ownerReferences") is not None else None,
            "resource_version": obj.get("resourceVersion"),
            "self_link": obj.get("selfLink"),
            "uid": obj.get("uid")
        })
        return _obj


