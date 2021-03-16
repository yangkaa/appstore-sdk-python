# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ModelsAppAttachment(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'app_id': 'str',
        'attach_id': 'str',
        'create_time': 'datetime',
        'name': 'str',
        'update_time': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'app_id': 'appID',
        'attach_id': 'attachID',
        'create_time': 'createTime',
        'name': 'name',
        'update_time': 'updateTime',
        'url': 'url'
    }

    def __init__(self, app_id=None, attach_id=None, create_time=None, name=None, update_time=None, url=None, local_vars_configuration=None):  # noqa: E501
        """ModelsAppAttachment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._attach_id = None
        self._create_time = None
        self._name = None
        self._update_time = None
        self._url = None
        self.discriminator = None

        self.app_id = app_id
        self.attach_id = attach_id
        self.create_time = create_time
        self.name = name
        self.update_time = update_time
        self.url = url

    @property
    def app_id(self):
        """Gets the app_id of this ModelsAppAttachment.  # noqa: E501


        :return: The app_id of this ModelsAppAttachment.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ModelsAppAttachment.


        :param app_id: The app_id of this ModelsAppAttachment.  # noqa: E501
        :type app_id: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def attach_id(self):
        """Gets the attach_id of this ModelsAppAttachment.  # noqa: E501


        :return: The attach_id of this ModelsAppAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attach_id

    @attach_id.setter
    def attach_id(self, attach_id):
        """Sets the attach_id of this ModelsAppAttachment.


        :param attach_id: The attach_id of this ModelsAppAttachment.  # noqa: E501
        :type attach_id: str
        """
        if self.local_vars_configuration.client_side_validation and attach_id is None:  # noqa: E501
            raise ValueError("Invalid value for `attach_id`, must not be `None`")  # noqa: E501

        self._attach_id = attach_id

    @property
    def create_time(self):
        """Gets the create_time of this ModelsAppAttachment.  # noqa: E501


        :return: The create_time of this ModelsAppAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ModelsAppAttachment.


        :param create_time: The create_time of this ModelsAppAttachment.  # noqa: E501
        :type create_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this ModelsAppAttachment.  # noqa: E501


        :return: The name of this ModelsAppAttachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsAppAttachment.


        :param name: The name of this ModelsAppAttachment.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def update_time(self):
        """Gets the update_time of this ModelsAppAttachment.  # noqa: E501


        :return: The update_time of this ModelsAppAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ModelsAppAttachment.


        :param update_time: The update_time of this ModelsAppAttachment.  # noqa: E501
        :type update_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def url(self):
        """Gets the url of this ModelsAppAttachment.  # noqa: E501


        :return: The url of this ModelsAppAttachment.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ModelsAppAttachment.


        :param url: The url of this ModelsAppAttachment.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelsAppAttachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsAppAttachment):
            return True

        return self.to_dict() != other.to_dict()
