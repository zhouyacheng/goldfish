# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GeneralAttachmentSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allowed_types': 'str',
        'enabled': 'bool',
        'max_files': 'int',
        'max_size': 'int'
    }

    attribute_map = {
        'allowed_types': 'allowed_types',
        'enabled': 'enabled',
        'max_files': 'max_files',
        'max_size': 'max_size'
    }

    def __init__(self, allowed_types=None, enabled=None, max_files=None, max_size=None):  # noqa: E501
        """GeneralAttachmentSettings - a model defined in Swagger"""  # noqa: E501
        self._allowed_types = None
        self._enabled = None
        self._max_files = None
        self._max_size = None
        self.discriminator = None
        if allowed_types is not None:
            self.allowed_types = allowed_types
        if enabled is not None:
            self.enabled = enabled
        if max_files is not None:
            self.max_files = max_files
        if max_size is not None:
            self.max_size = max_size

    @property
    def allowed_types(self):
        """Gets the allowed_types of this GeneralAttachmentSettings.  # noqa: E501


        :return: The allowed_types of this GeneralAttachmentSettings.  # noqa: E501
        :rtype: str
        """
        return self._allowed_types

    @allowed_types.setter
    def allowed_types(self, allowed_types):
        """Sets the allowed_types of this GeneralAttachmentSettings.


        :param allowed_types: The allowed_types of this GeneralAttachmentSettings.  # noqa: E501
        :type: str
        """

        self._allowed_types = allowed_types

    @property
    def enabled(self):
        """Gets the enabled of this GeneralAttachmentSettings.  # noqa: E501


        :return: The enabled of this GeneralAttachmentSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GeneralAttachmentSettings.


        :param enabled: The enabled of this GeneralAttachmentSettings.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def max_files(self):
        """Gets the max_files of this GeneralAttachmentSettings.  # noqa: E501


        :return: The max_files of this GeneralAttachmentSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_files

    @max_files.setter
    def max_files(self, max_files):
        """Sets the max_files of this GeneralAttachmentSettings.


        :param max_files: The max_files of this GeneralAttachmentSettings.  # noqa: E501
        :type: int
        """

        self._max_files = max_files

    @property
    def max_size(self):
        """Gets the max_size of this GeneralAttachmentSettings.  # noqa: E501


        :return: The max_size of this GeneralAttachmentSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this GeneralAttachmentSettings.


        :param max_size: The max_size of this GeneralAttachmentSettings.  # noqa: E501
        :type: int
        """

        self._max_size = max_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GeneralAttachmentSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GeneralAttachmentSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
