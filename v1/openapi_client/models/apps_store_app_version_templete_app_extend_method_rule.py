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


class AppsStoreAppVersionTempleteAppExtendMethodRule(object):
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
        'is_restart': 'int',
        'max_memory': 'int',
        'max_node': 'int',
        'min_memory': 'int',
        'min_node': 'int',
        'step_memory': 'int',
        'step_node': 'int'
    }

    attribute_map = {
        'is_restart': 'is_restart',
        'max_memory': 'max_memory',
        'max_node': 'max_node',
        'min_memory': 'min_memory',
        'min_node': 'min_node',
        'step_memory': 'step_memory',
        'step_node': 'step_node'
    }

    def __init__(self, is_restart=None, max_memory=None, max_node=None, min_memory=None, min_node=None, step_memory=None, step_node=None, local_vars_configuration=None):  # noqa: E501
        """AppsStoreAppVersionTempleteAppExtendMethodRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_restart = None
        self._max_memory = None
        self._max_node = None
        self._min_memory = None
        self._min_node = None
        self._step_memory = None
        self._step_node = None
        self.discriminator = None

        self.is_restart = is_restart
        self.max_memory = max_memory
        self.max_node = max_node
        self.min_memory = min_memory
        self.min_node = min_node
        self.step_memory = step_memory
        self.step_node = step_node

    @property
    def is_restart(self):
        """Gets the is_restart of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The is_restart of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._is_restart

    @is_restart.setter
    def is_restart(self, is_restart):
        """Sets the is_restart of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param is_restart: The is_restart of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type is_restart: int
        """
        if self.local_vars_configuration.client_side_validation and is_restart is None:  # noqa: E501
            raise ValueError("Invalid value for `is_restart`, must not be `None`")  # noqa: E501

        self._is_restart = is_restart

    @property
    def max_memory(self):
        """Gets the max_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The max_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param max_memory: The max_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type max_memory: int
        """
        if self.local_vars_configuration.client_side_validation and max_memory is None:  # noqa: E501
            raise ValueError("Invalid value for `max_memory`, must not be `None`")  # noqa: E501

        self._max_memory = max_memory

    @property
    def max_node(self):
        """Gets the max_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The max_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._max_node

    @max_node.setter
    def max_node(self, max_node):
        """Sets the max_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param max_node: The max_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type max_node: int
        """
        if self.local_vars_configuration.client_side_validation and max_node is None:  # noqa: E501
            raise ValueError("Invalid value for `max_node`, must not be `None`")  # noqa: E501

        self._max_node = max_node

    @property
    def min_memory(self):
        """Gets the min_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The min_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._min_memory

    @min_memory.setter
    def min_memory(self, min_memory):
        """Sets the min_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param min_memory: The min_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type min_memory: int
        """
        if self.local_vars_configuration.client_side_validation and min_memory is None:  # noqa: E501
            raise ValueError("Invalid value for `min_memory`, must not be `None`")  # noqa: E501

        self._min_memory = min_memory

    @property
    def min_node(self):
        """Gets the min_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The min_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._min_node

    @min_node.setter
    def min_node(self, min_node):
        """Sets the min_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param min_node: The min_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type min_node: int
        """
        if self.local_vars_configuration.client_side_validation and min_node is None:  # noqa: E501
            raise ValueError("Invalid value for `min_node`, must not be `None`")  # noqa: E501

        self._min_node = min_node

    @property
    def step_memory(self):
        """Gets the step_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The step_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._step_memory

    @step_memory.setter
    def step_memory(self, step_memory):
        """Sets the step_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param step_memory: The step_memory of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type step_memory: int
        """
        if self.local_vars_configuration.client_side_validation and step_memory is None:  # noqa: E501
            raise ValueError("Invalid value for `step_memory`, must not be `None`")  # noqa: E501

        self._step_memory = step_memory

    @property
    def step_node(self):
        """Gets the step_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501


        :return: The step_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :rtype: int
        """
        return self._step_node

    @step_node.setter
    def step_node(self, step_node):
        """Sets the step_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.


        :param step_node: The step_node of this AppsStoreAppVersionTempleteAppExtendMethodRule.  # noqa: E501
        :type step_node: int
        """
        if self.local_vars_configuration.client_side_validation and step_node is None:  # noqa: E501
            raise ValueError("Invalid value for `step_node`, must not be `None`")  # noqa: E501

        self._step_node = step_node

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
        if not isinstance(other, AppsStoreAppVersionTempleteAppExtendMethodRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppsStoreAppVersionTempleteAppExtendMethodRule):
            return True

        return self.to_dict() != other.to_dict()
