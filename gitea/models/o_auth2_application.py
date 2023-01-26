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

class OAuth2Application(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'created': 'datetime',
        'id': 'int',
        'name': 'str',
        'redirect_uris': 'list[str]'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'created': 'created',
        'id': 'id',
        'name': 'name',
        'redirect_uris': 'redirect_uris'
    }

    def __init__(self, client_id=None, client_secret=None, created=None, id=None, name=None, redirect_uris=None):  # noqa: E501
        """OAuth2Application - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._client_secret = None
        self._created = None
        self._id = None
        self._name = None
        self._redirect_uris = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris

    @property
    def client_id(self):
        """Gets the client_id of this OAuth2Application.  # noqa: E501


        :return: The client_id of this OAuth2Application.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuth2Application.


        :param client_id: The client_id of this OAuth2Application.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this OAuth2Application.  # noqa: E501


        :return: The client_secret of this OAuth2Application.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OAuth2Application.


        :param client_secret: The client_secret of this OAuth2Application.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def created(self):
        """Gets the created of this OAuth2Application.  # noqa: E501


        :return: The created of this OAuth2Application.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OAuth2Application.


        :param created: The created of this OAuth2Application.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this OAuth2Application.  # noqa: E501


        :return: The id of this OAuth2Application.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2Application.


        :param id: The id of this OAuth2Application.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OAuth2Application.  # noqa: E501


        :return: The name of this OAuth2Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2Application.


        :param name: The name of this OAuth2Application.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this OAuth2Application.  # noqa: E501


        :return: The redirect_uris of this OAuth2Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this OAuth2Application.


        :param redirect_uris: The redirect_uris of this OAuth2Application.  # noqa: E501
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

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
        if issubclass(OAuth2Application, dict):
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
        if not isinstance(other, OAuth2Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
