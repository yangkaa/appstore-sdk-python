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


class V1Organization(object):
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
        'desc': 'str',
        'eid': 'str',
        'name': 'str',
        'org_id': 'str'
    }

    attribute_map = {
        'desc': 'desc',
        'eid': 'eid',
        'name': 'name',
        'org_id': 'orgID'
    }

    def __init__(self, desc=None, eid=None, name=None, org_id=None, local_vars_configuration=None):  # noqa: E501
        """V1Organization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._desc = None
        self._eid = None
        self._name = None
        self._org_id = None
        self.discriminator = None

        self.desc = desc
        self.eid = eid
        self.name = name
        self.org_id = org_id

    @property
    def desc(self):
        """Gets the desc of this V1Organization.  # noqa: E501

        描述  # noqa: E501

        :return: The desc of this V1Organization.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this V1Organization.

        描述  # noqa: E501

        :param desc: The desc of this V1Organization.  # noqa: E501
        :type desc: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def eid(self):
        """Gets the eid of this V1Organization.  # noqa: E501

        企业 ID  # noqa: E501

        :return: The eid of this V1Organization.  # noqa: E501
        :rtype: str
        """
        return self._eid

    @eid.setter
    def eid(self, eid):
        """Sets the eid of this V1Organization.

        企业 ID  # noqa: E501

        :param eid: The eid of this V1Organization.  # noqa: E501
        :type eid: str
        """
        if self.local_vars_configuration.client_side_validation and eid is None:  # noqa: E501
            raise ValueError("Invalid value for `eid`, must not be `None`")  # noqa: E501

        self._eid = eid

    @property
    def name(self):
        """Gets the name of this V1Organization.  # noqa: E501

        名称  # noqa: E501

        :return: The name of this V1Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Organization.

        名称  # noqa: E501

        :param name: The name of this V1Organization.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this V1Organization.  # noqa: E501

        组织机构 ID  # noqa: E501

        :return: The org_id of this V1Organization.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this V1Organization.

        组织机构 ID  # noqa: E501

        :param org_id: The org_id of this V1Organization.  # noqa: E501
        :type org_id: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

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
        if not isinstance(other, V1Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Organization):
            return True

        return self.to_dict() != other.to_dict()
