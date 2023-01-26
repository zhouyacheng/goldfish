# gitea.SettingsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_general_api_settings**](SettingsApi.md#get_general_api_settings) | **GET** /settings/api | Get instance&#x27;s global settings for api
[**get_general_attachment_settings**](SettingsApi.md#get_general_attachment_settings) | **GET** /settings/attachment | Get instance&#x27;s global settings for Attachment
[**get_general_repository_settings**](SettingsApi.md#get_general_repository_settings) | **GET** /settings/repository | Get instance&#x27;s global settings for repositories
[**get_general_ui_settings**](SettingsApi.md#get_general_ui_settings) | **GET** /settings/ui | Get instance&#x27;s global settings for ui

# **get_general_api_settings**
> GeneralAPISettings get_general_api_settings()

Get instance's global settings for api

### Example
```python
from __future__ import print_function
import time
import gitea
from gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = gitea.SettingsApi(gitea.ApiClient(configuration))

try:
    # Get instance's global settings for api
    api_response = api_instance.get_general_api_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_general_api_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralAPISettings**](GeneralAPISettings.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **get_general_attachment_settings**
> GeneralAttachmentSettings get_general_attachment_settings()

Get instance's global settings for Attachment

### Example
```python
from __future__ import print_function
import time
import gitea
from gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = gitea.SettingsApi(gitea.ApiClient(configuration))

try:
    # Get instance's global settings for Attachment
    api_response = api_instance.get_general_attachment_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_general_attachment_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralAttachmentSettings**](GeneralAttachmentSettings.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **get_general_repository_settings**
> GeneralRepoSettings get_general_repository_settings()

Get instance's global settings for repositories

### Example
```python
from __future__ import print_function
import time
import gitea
from gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = gitea.SettingsApi(gitea.ApiClient(configuration))

try:
    # Get instance's global settings for repositories
    api_response = api_instance.get_general_repository_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_general_repository_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralRepoSettings**](GeneralRepoSettings.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **get_general_ui_settings**
> GeneralUISettings get_general_ui_settings()

Get instance's global settings for ui

### Example
```python
from __future__ import print_function
import time
import gitea
from gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = gitea.SettingsApi(gitea.ApiClient(configuration))

try:
    # Get instance's global settings for ui
    api_response = api_instance.get_general_ui_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_general_ui_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralUISettings**](GeneralUISettings.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

