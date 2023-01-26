# gitea.MiscellaneousApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_signing_key**](MiscellaneousApi.md#get_signing_key) | **GET** /signing-key.gpg | Get default signing-key.gpg
[**get_version**](MiscellaneousApi.md#get_version) | **GET** /version | Returns the version of the Gitea application
[**render_markdown**](MiscellaneousApi.md#render_markdown) | **POST** /markdown | Render a markdown document as HTML
[**render_markdown_raw**](MiscellaneousApi.md#render_markdown_raw) | **POST** /markdown/raw | Render raw markdown as HTML

# **get_signing_key**
> str get_signing_key()

Get default signing-key.gpg

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
api_instance = gitea.MiscellaneousApi(gitea.ApiClient(configuration))

try:
    # Get default signing-key.gpg
    api_response = api_instance.get_signing_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_signing_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **get_version**
> ServerVersion get_version()

Returns the version of the Gitea application

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
api_instance = gitea.MiscellaneousApi(gitea.ApiClient(configuration))

try:
    # Returns the version of the Gitea application
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerVersion**](ServerVersion.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **render_markdown**
> str render_markdown(body=body)

Render a markdown document as HTML

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
api_instance = gitea.MiscellaneousApi(gitea.ApiClient(configuration))
body = gitea.MarkdownOption() # MarkdownOption |  (optional)

try:
    # Render a markdown document as HTML
    api_response = api_instance.render_markdown(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->render_markdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkdownOption**](MarkdownOption.md)|  | [optional] 

### Return type

**str**

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **render_markdown_raw**
> str render_markdown_raw(body)

Render raw markdown as HTML

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
api_instance = gitea.MiscellaneousApi(gitea.ApiClient(configuration))
body = 'body_example' # str | Request body to render

try:
    # Render raw markdown as HTML
    api_response = api_instance.render_markdown_raw(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->render_markdown_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Request body to render | 

### Return type

**str**

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

