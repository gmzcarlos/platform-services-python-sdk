# coding: utf-8

# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Manage your tags with the Tagging API in IBM Cloud. You can attach, detach, delete a tag
or list all tags in your billing account with the Tagging API. The tag name must be unique
within a billing account. You can create tags in two formats: `key:value` or `label`.
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class GlobalTaggingV1(BaseService):
    """The global_tagging V1 service."""

    DEFAULT_SERVICE_URL = 'https://tags.global-search-tagging.cloud.ibm.com/'
    DEFAULT_SERVICE_NAME = 'global_tagging'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalTaggingV1':
        """
        Return a new client for the global_tagging service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the global_tagging service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # tags
    #########################


    def list_tags(self, *, providers: List[str] = None, attached_to: str = None, full_data: bool = None, offset: int = None, limit: int = None, order_by_name: str = None, timeout: int = None, attached_only: bool = None, **kwargs) -> DetailedResponse:
        """
        Get all tags.

        Lists all tags in a billing account. Use the `attached_to` parameter to return the
        list of tags attached to the specified resource.

        :param List[str] providers: (optional) Select a provider. Supported values
               are `ghost` and `ims`. To list GhoST tags and infrastructure tags use
               `ghost,ims`.
        :param str attached_to: (optional) If you want to return only the list of
               tags attached to a specified resource, pass here the ID of the resource.
               For GhoST onboarded resources, the resource ID is the CRN; for IMS
               resources, it is the IMS ID. When using this parameter it is mandatory to
               specify the appropriate provider (`ims` or `ghost`).
        :param bool full_data: (optional) If set to `true`, this query returns the
               provider, `ghost`, `ims` or `ghost,ims`, where the tag exists and the
               number of attached resources.
        :param int offset: (optional) The offset is the index of the item from
               which you want to start returning data from.
        :param int limit: (optional) The number of tags to return.
        :param str order_by_name: (optional) Order the output by tag name.
        :param int timeout: (optional) The search timeout bounds the search request
               to be executed within the specified time value. It returns the hits
               accumulated until time runs out.
        :param bool attached_only: (optional) Filter on attached tags. If true,
               returns only tags that are attached to one or more resources. If false
               returns all tags.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TagList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_tags')
        headers.update(sdk_headers)

        params = {
            'providers': convert_list(providers),
            'attached_to': attached_to,
            'full_data': full_data,
            'offset': offset,
            'limit': limit,
            'order_by_name': order_by_name,
            'timeout': timeout,
            'attached_only': attached_only
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/tags'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_tag_all(self, *, providers: str = None, **kwargs) -> DetailedResponse:
        """
        Delete unused tags.

        Delete the tags that are not attatched to any resource.

        :param str providers: (optional) Select a provider. Supported values are
               `ghost` and `ims`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteTagsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_tag_all')
        headers.update(sdk_headers)

        params = {
            'providers': providers
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/tags'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_tag(self, tag_name: str, *, providers: List[str] = None, **kwargs) -> DetailedResponse:
        """
        Delete a tag.

        Delete an existing tag. A tag can be deleted only if it is not attached to any
        resource.

        :param str tag_name: The name of tag to be deleted.
        :param List[str] providers: (optional) Select a provider. Supported values
               are `ghost` and `ims`. To delete tag both in GhoST in IMS, use `ghost,ims`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteTagResults` object
        """

        if tag_name is None:
            raise ValueError('tag_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_tag')
        headers.update(sdk_headers)

        params = {
            'providers': convert_list(providers)
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/tags/{0}'.format(*self.encode_path_vars(tag_name))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def attach_tag(self, resources: List['Resource'], *, tag_name: str = None, tag_names: List[str] = None, **kwargs) -> DetailedResponse:
        """
        Attach one or more tags.

        Attaches one or more tags to one or more resources. To attach a tag to a resource
        managed by the Resource Controller, you must be an editor on the resource. To
        attach a tag to a Cloud Foundry resource, you must have space developer role. To
        attach a tag to IMS resources, depending on the resource, you need either `view
        hardware details`, `view virtual server details` or `manage storage` permission.

        :param List[Resource] resources: List of resources on which the tag or tags
               should be attached.
        :param str tag_name: (optional) The name of the tag to attach.
        :param List[str] tag_names: (optional) An array of tag names to attach.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TagResults` object
        """

        if resources is None:
            raise ValueError('resources must be provided')
        resources = [ convert_model(x) for x in resources ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='attach_tag')
        headers.update(sdk_headers)

        data = {
            'resources': resources,
            'tag_name': tag_name,
            'tag_names': tag_names
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/tags/attach'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def detach_tag(self, resources: List['Resource'], *, tag_name: str = None, tag_names: List[str] = None, **kwargs) -> DetailedResponse:
        """
        Detach one or more tags.

        Detach one or more tags from one or more resources. To detach a tag from a
        Resource Controller managed resource, you must be an editor on the resource. To
        detach a tag to a Cloud Foundry resource, you must have `space developer` role.
          To detach a tag to IMS resources, depending on the resource, you need either
        `view hardware details`, `view virtual server details` or `storage manage`
        permission.

        :param List[Resource] resources: List of resources on which the tag or tags
               should be detached.
        :param str tag_name: (optional) The name of the tag to detach.
        :param List[str] tag_names: (optional) An array of tag names to detach.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TagResults` object
        """

        if resources is None:
            raise ValueError('resources must be provided')
        resources = [ convert_model(x) for x in resources ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='detach_tag')
        headers.update(sdk_headers)

        data = {
            'resources': resources,
            'tag_name': tag_name,
            'tag_names': tag_names
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/tags/detach'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class ListTagsEnums:
    """
    Enums for list_tags parameters.
    """

    class Providers(Enum):
        """
        Select a provider. Supported values are `ghost` and `ims`. To list GhoST tags and
        infrastructure tags use `ghost,ims`.
        """
        GHOST = 'ghost'
        IMS = 'ims'
    class OrderByName(Enum):
        """
        Order the output by tag name.
        """
        ASC = 'asc'
        DESC = 'desc'


class DeleteTagAllEnums:
    """
    Enums for delete_tag_all parameters.
    """

    class Providers(Enum):
        """
        Select a provider. Supported values are `ghost` and `ims`.
        """
        GHOST = 'ghost'
        IMS = 'ims'


class DeleteTagEnums:
    """
    Enums for delete_tag parameters.
    """

    class Providers(Enum):
        """
        Select a provider. Supported values are `ghost` and `ims`. To delete tag both in
        GhoST in IMS, use `ghost,ims`.
        """
        GHOST = 'ghost'
        IMS = 'ims'


##############################################################################
# Models
##############################################################################


class DeleteTagResults():
    """
    Results of a delete_tag request.

    :attr List[DeleteTagResultsItem] results: (optional) Array of results of a
          delete_tag request.
    """

    def __init__(self, *, results: List['DeleteTagResultsItem'] = None) -> None:
        """
        Initialize a DeleteTagResults object.

        :param List[DeleteTagResultsItem] results: (optional) Array of results of a
               delete_tag request.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteTagResults':
        """Initialize a DeleteTagResults object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [DeleteTagResultsItem.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteTagResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteTagResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteTagResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteTagResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteTagResultsItem():
    """
    Result of a delete_tag request.

    :attr str provider: (optional) The provider of the tag.
    :attr bool is_error: (optional) It is `true` if the operation exits with an
          error.
    """

    # The set of defined properties for the class
    _properties = frozenset(['provider', 'is_error'])

    def __init__(self, *, provider: str = None, is_error: bool = None, **kwargs) -> None:
        """
        Initialize a DeleteTagResultsItem object.

        :param str provider: (optional) The provider of the tag.
        :param bool is_error: (optional) It is `true` if the operation exits with
               an error.
        :param **kwargs: (optional) Any additional properties.
        """
        self.provider = provider
        self.is_error = is_error
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteTagResultsItem':
        """Initialize a DeleteTagResultsItem object from a json dictionary."""
        args = {}
        if 'provider' in _dict:
            args['provider'] = _dict.get('provider')
        if 'is_error' in _dict:
            args['is_error'] = _dict.get('is_error')
        args.update({k:v for (k,v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteTagResultsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider') and self.provider is not None:
            _dict['provider'] = self.provider
        if hasattr(self, 'is_error') and self.is_error is not None:
            _dict['is_error'] = self.is_error
        for _key in [k for k in vars(self).keys() if k not in DeleteTagResultsItem._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteTagResultsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteTagResultsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteTagResultsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class ProviderEnum(Enum):
        """
        The provider of the tag.
        """
        GHOST = "ghost"
        IMS = "ims"


class DeleteTagsResult():
    """
    The results of a deleting unattatched tags.

    :attr int total_count: (optional) The number of tags deleted in the account.
    :attr bool errors: (optional) An indicator that is set to true if there was an
          error deleting some of the tags.
    :attr List[DeleteTagsResultItem] items: (optional)
    """

    def __init__(self, *, total_count: int = None, errors: bool = None, items: List['DeleteTagsResultItem'] = None) -> None:
        """
        Initialize a DeleteTagsResult object.

        :param int total_count: (optional) The number of tags deleted in the
               account.
        :param bool errors: (optional) An indicator that is set to true if there
               was an error deleting some of the tags.
        :param List[DeleteTagsResultItem] items: (optional)
        """
        self.total_count = total_count
        self.errors = errors
        self.items = items

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteTagsResult':
        """Initialize a DeleteTagsResult object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'items' in _dict:
            args['items'] = [DeleteTagsResultItem.from_dict(x) for x in _dict.get('items')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteTagsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'items') and self.items is not None:
            _dict['items'] = [x.to_dict() for x in self.items]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteTagsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteTagsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteTagsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteTagsResultItem():
    """
    Result of deleting one unattached tag.

    :attr str tag_name: (optional) The name of the tag that was deleted.
    :attr bool is_error: (optional) An indicator that is set to true if there was an
          error deleting the tag.
    """

    def __init__(self, *, tag_name: str = None, is_error: bool = None) -> None:
        """
        Initialize a DeleteTagsResultItem object.

        :param str tag_name: (optional) The name of the tag that was deleted.
        :param bool is_error: (optional) An indicator that is set to true if there
               was an error deleting the tag.
        """
        self.tag_name = tag_name
        self.is_error = is_error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteTagsResultItem':
        """Initialize a DeleteTagsResultItem object from a json dictionary."""
        args = {}
        if 'tag_name' in _dict:
            args['tag_name'] = _dict.get('tag_name')
        if 'is_error' in _dict:
            args['is_error'] = _dict.get('is_error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteTagsResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tag_name') and self.tag_name is not None:
            _dict['tag_name'] = self.tag_name
        if hasattr(self, 'is_error') and self.is_error is not None:
            _dict['is_error'] = self.is_error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteTagsResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteTagsResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteTagsResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Resource():
    """
    A resource that may have attached tags.

    :attr str resource_id: The CRN or IMS ID of the resource.
    :attr str resource_type: (optional) The IMS resource type of the resource.
    """

    def __init__(self, resource_id: str, *, resource_type: str = None) -> None:
        """
        Initialize a Resource object.

        :param str resource_id: The CRN or IMS ID of the resource.
        :param str resource_type: (optional) The IMS resource type of the resource.
        """
        self.resource_id = resource_id
        self.resource_type = resource_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        else:
            raise ValueError('Required property \'resource_id\' not present in Resource JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Resource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Tag():
    """
    A tag.

    :attr str name: This is the name of the tag.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Tag object.

        :param str name: This is the name of the tag.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tag':
        """Initialize a Tag object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Tag JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tag object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tag object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tag') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tag') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TagList():
    """
    A list of tags.

    :attr int total_count: (optional) The number of tags defined in the account.
    :attr int offset: (optional) The offset specific at input time.
    :attr int limit: (optional) The limit specified at input time.
    :attr List[Tag] items: (optional) This is an array of output results.
    """

    def __init__(self, *, total_count: int = None, offset: int = None, limit: int = None, items: List['Tag'] = None) -> None:
        """
        Initialize a TagList object.

        :param int total_count: (optional) The number of tags defined in the
               account.
        :param int offset: (optional) The offset specific at input time.
        :param int limit: (optional) The limit specified at input time.
        :param List[Tag] items: (optional) This is an array of output results.
        """
        self.total_count = total_count
        self.offset = offset
        self.limit = limit
        self.items = items

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TagList':
        """Initialize a TagList object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'items' in _dict:
            args['items'] = [Tag.from_dict(x) for x in _dict.get('items')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TagList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'items') and self.items is not None:
            _dict['items'] = [x.to_dict() for x in self.items]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TagList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TagList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TagList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TagResults():
    """
    Results of an attach_tag or detach_tag request.

    :attr List[TagResultsItem] results: (optional) Array of results of an attach_tag
          or detach_tag request.
    """

    def __init__(self, *, results: List['TagResultsItem'] = None) -> None:
        """
        Initialize a TagResults object.

        :param List[TagResultsItem] results: (optional) Array of results of an
               attach_tag or detach_tag request.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TagResults':
        """Initialize a TagResults object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [TagResultsItem.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TagResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TagResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TagResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TagResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TagResultsItem():
    """
    Result of an attach_tag or detach_tag request for a tagged resource.

    :attr str resource_id: The CRN or IMS ID of the resource.
    :attr bool is_error: (optional) It is `true` if the operation exits with an
          error.
    """

    def __init__(self, resource_id: str, *, is_error: bool = None) -> None:
        """
        Initialize a TagResultsItem object.

        :param str resource_id: The CRN or IMS ID of the resource.
        :param bool is_error: (optional) It is `true` if the operation exits with
               an error.
        """
        self.resource_id = resource_id
        self.is_error = is_error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TagResultsItem':
        """Initialize a TagResultsItem object from a json dictionary."""
        args = {}
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        else:
            raise ValueError('Required property \'resource_id\' not present in TagResultsItem JSON')
        if 'is_error' in _dict:
            args['is_error'] = _dict.get('is_error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TagResultsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'is_error') and self.is_error is not None:
            _dict['is_error'] = self.is_error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TagResultsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TagResultsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TagResultsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


