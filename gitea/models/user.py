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

class User(object):
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
        'avatar_url': 'str',
        'created': 'datetime',
        'email': 'str',
        'full_name': 'str',
        'id': 'int',
        'is_admin': 'bool',
        'language': 'str',
        'last_login': 'datetime',
        'login': 'str',
        'restricted': 'bool'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'created': 'created',
        'email': 'email',
        'full_name': 'full_name',
        'id': 'id',
        'is_admin': 'is_admin',
        'language': 'language',
        'last_login': 'last_login',
        'login': 'login',
        'restricted': 'restricted'
    }

    def __init__(self, avatar_url=None, created=None, email=None, full_name=None, id=None, is_admin=None, language=None, last_login=None, login=None, restricted=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._avatar_url = None
        self._created = None
        self._email = None
        self._full_name = None
        self._id = None
        self._is_admin = None
        self._language = None
        self._last_login = None
        self._login = None
        self._restricted = None
        self.discriminator = None
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if created is not None:
            self.created = created
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if is_admin is not None:
            self.is_admin = is_admin
        if language is not None:
            self.language = language
        if last_login is not None:
            self.last_login = last_login
        if login is not None:
            self.login = login
        if restricted is not None:
            self.restricted = restricted

    @property
    def avatar_url(self):
        """Gets the avatar_url of this User.  # noqa: E501

        URL to the user's avatar  # noqa: E501

        :return: The avatar_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this User.

        URL to the user's avatar  # noqa: E501

        :param avatar_url: The avatar_url of this User.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def created(self):
        """Gets the created of this User.  # noqa: E501


        :return: The created of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this User.


        :param created: The created of this User.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501

        the user's full name  # noqa: E501

        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.

        the user's full name  # noqa: E501

        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        the user's id  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        the user's id  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_admin(self):
        """Gets the is_admin of this User.  # noqa: E501

        Is the user an administrator  # noqa: E501

        :return: The is_admin of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this User.

        Is the user an administrator  # noqa: E501

        :param is_admin: The is_admin of this User.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def language(self):
        """Gets the language of this User.  # noqa: E501

        User locale  # noqa: E501

        :return: The language of this User.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this User.

        User locale  # noqa: E501

        :param language: The language of this User.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501


        :return: The last_login of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.


        :param last_login: The last_login of this User.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def login(self):
        """Gets the login of this User.  # noqa: E501

        the user's username  # noqa: E501

        :return: The login of this User.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this User.

        the user's username  # noqa: E501

        :param login: The login of this User.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def restricted(self):
        """Gets the restricted of this User.  # noqa: E501

        Is user restricted  # noqa: E501

        :return: The restricted of this User.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this User.

        Is user restricted  # noqa: E501

        :param restricted: The restricted of this User.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
