# gitea.UserApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_current_user_repo**](UserApi.md#create_current_user_repo) | **POST** /user/repos | Create a repository
[**user_add_email**](UserApi.md#user_add_email) | **POST** /user/emails | Add email addresses
[**user_check_following**](UserApi.md#user_check_following) | **GET** /users/{follower}/following/{followee} | Check if one user is following another user
[**user_create_o_auth2_application**](UserApi.md#user_create_o_auth2_application) | **POST** /user/applications/oauth2 | creates a new OAuth2 application
[**user_create_token**](UserApi.md#user_create_token) | **POST** /users/{username}/tokens | Create an access token
[**user_current_check_following**](UserApi.md#user_current_check_following) | **GET** /user/following/{username} | Check whether a user is followed by the authenticated user
[**user_current_check_starring**](UserApi.md#user_current_check_starring) | **GET** /user/starred/{owner}/{repo} | Whether the authenticated is starring the repo
[**user_current_delete_follow**](UserApi.md#user_current_delete_follow) | **DELETE** /user/following/{username} | Unfollow a user
[**user_current_delete_gpg_key**](UserApi.md#user_current_delete_gpg_key) | **DELETE** /user/gpg_keys/{id} | Remove a GPG key
[**user_current_delete_key**](UserApi.md#user_current_delete_key) | **DELETE** /user/keys/{id} | Delete a public key
[**user_current_delete_star**](UserApi.md#user_current_delete_star) | **DELETE** /user/starred/{owner}/{repo} | Unstar the given repo
[**user_current_get_gpg_key**](UserApi.md#user_current_get_gpg_key) | **GET** /user/gpg_keys/{id} | Get a GPG key
[**user_current_get_key**](UserApi.md#user_current_get_key) | **GET** /user/keys/{id} | Get a public key
[**user_current_list_followers**](UserApi.md#user_current_list_followers) | **GET** /user/followers | List the authenticated user&#x27;s followers
[**user_current_list_following**](UserApi.md#user_current_list_following) | **GET** /user/following | List the users that the authenticated user is following
[**user_current_list_gpg_keys**](UserApi.md#user_current_list_gpg_keys) | **GET** /user/gpg_keys | List the authenticated user&#x27;s GPG keys
[**user_current_list_keys**](UserApi.md#user_current_list_keys) | **GET** /user/keys | List the authenticated user&#x27;s public keys
[**user_current_list_repos**](UserApi.md#user_current_list_repos) | **GET** /user/repos | List the repos that the authenticated user owns or has access to
[**user_current_list_starred**](UserApi.md#user_current_list_starred) | **GET** /user/starred | The repos that the authenticated user has starred
[**user_current_list_subscriptions**](UserApi.md#user_current_list_subscriptions) | **GET** /user/subscriptions | List repositories watched by the authenticated user
[**user_current_post_gpg_key**](UserApi.md#user_current_post_gpg_key) | **POST** /user/gpg_keys | Create a GPG key
[**user_current_post_key**](UserApi.md#user_current_post_key) | **POST** /user/keys | Create a public key
[**user_current_put_follow**](UserApi.md#user_current_put_follow) | **PUT** /user/following/{username} | Follow a user
[**user_current_put_star**](UserApi.md#user_current_put_star) | **PUT** /user/starred/{owner}/{repo} | Star the given repo
[**user_current_tracked_times**](UserApi.md#user_current_tracked_times) | **GET** /user/times | List the current user&#x27;s tracked times
[**user_delete_access_token**](UserApi.md#user_delete_access_token) | **DELETE** /users/{username}/tokens/{token} | delete an access token
[**user_delete_email**](UserApi.md#user_delete_email) | **DELETE** /user/emails | Delete email addresses
[**user_delete_o_auth2_application**](UserApi.md#user_delete_o_auth2_application) | **DELETE** /user/applications/oauth2/{id} | delete an OAuth2 Application
[**user_get**](UserApi.md#user_get) | **GET** /users/{username} | Get a user
[**user_get_current**](UserApi.md#user_get_current) | **GET** /user | Get the authenticated user
[**user_get_heatmap_data**](UserApi.md#user_get_heatmap_data) | **GET** /users/{username}/heatmap | Get a user&#x27;s heatmap
[**user_get_o_auth2_application**](UserApi.md#user_get_o_auth2_application) | **GET** /user/applications/oauth2/{id} | get an OAuth2 Application
[**user_get_oauth2_application**](UserApi.md#user_get_oauth2_application) | **GET** /user/applications/oauth2 | List the authenticated user&#x27;s oauth2 applications
[**user_get_stop_watches**](UserApi.md#user_get_stop_watches) | **GET** /user/stopwatches | Get list of all existing stopwatches
[**user_get_tokens**](UserApi.md#user_get_tokens) | **GET** /users/{username}/tokens | List the authenticated user&#x27;s access tokens
[**user_list_emails**](UserApi.md#user_list_emails) | **GET** /user/emails | List the authenticated user&#x27;s email addresses
[**user_list_followers**](UserApi.md#user_list_followers) | **GET** /users/{username}/followers | List the given user&#x27;s followers
[**user_list_following**](UserApi.md#user_list_following) | **GET** /users/{username}/following | List the users that the given user is following
[**user_list_gpg_keys**](UserApi.md#user_list_gpg_keys) | **GET** /users/{username}/gpg_keys | List the given user&#x27;s GPG keys
[**user_list_keys**](UserApi.md#user_list_keys) | **GET** /users/{username}/keys | List the given user&#x27;s public keys
[**user_list_repos**](UserApi.md#user_list_repos) | **GET** /users/{username}/repos | List the repos owned by the given user
[**user_list_starred**](UserApi.md#user_list_starred) | **GET** /users/{username}/starred | The repos that the given user has starred
[**user_list_subscriptions**](UserApi.md#user_list_subscriptions) | **GET** /users/{username}/subscriptions | List the repositories watched by a user
[**user_list_teams**](UserApi.md#user_list_teams) | **GET** /user/teams | List all the teams a user belongs to
[**user_search**](UserApi.md#user_search) | **GET** /users/search | Search for users
[**user_update_o_auth2_application**](UserApi.md#user_update_o_auth2_application) | **PATCH** /user/applications/oauth2/{id} | update an OAuth2 Application, this includes regenerating the client secret

# **create_current_user_repo**
> Repository create_current_user_repo(body=body)

Create a repository

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateRepoOption() # CreateRepoOption |  (optional)

try:
    # Create a repository
    api_response = api_instance.create_current_user_repo(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_current_user_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_add_email**
> list[Email] user_add_email(body=body)

Add email addresses

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateEmailOption() # CreateEmailOption |  (optional)

try:
    # Add email addresses
    api_response = api_instance.user_add_email(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_add_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEmailOption**](CreateEmailOption.md)|  | [optional] 

### Return type

[**list[Email]**](Email.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_check_following**
> user_check_following(follower, followee)

Check if one user is following another user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
follower = 'follower_example' # str | username of following user
followee = 'followee_example' # str | username of followed user

try:
    # Check if one user is following another user
    api_instance.user_check_following(follower, followee)
except ApiException as e:
    print("Exception when calling UserApi->user_check_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **follower** | **str**| username of following user | 
 **followee** | **str**| username of followed user | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_create_o_auth2_application**
> OAuth2Application user_create_o_auth2_application(body)

creates a new OAuth2 application

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateOAuth2ApplicationOptions() # CreateOAuth2ApplicationOptions | 

try:
    # creates a new OAuth2 application
    api_response = api_instance.user_create_o_auth2_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_create_o_auth2_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOAuth2ApplicationOptions**](CreateOAuth2ApplicationOptions.md)|  | 

### Return type

[**OAuth2Application**](OAuth2Application.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_create_token**
> user_create_token(username, body=body)

Create an access token

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
body = gitea.UsernameTokensBody() # UsernameTokensBody |  (optional)

try:
    # Create an access token
    api_instance.user_create_token(username, body=body)
except ApiException as e:
    print("Exception when calling UserApi->user_create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **body** | [**UsernameTokensBody**](UsernameTokensBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_check_following**
> user_current_check_following(username)

Check whether a user is followed by the authenticated user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of followed user

try:
    # Check whether a user is followed by the authenticated user
    api_instance.user_current_check_following(username)
except ApiException as e:
    print("Exception when calling UserApi->user_current_check_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of followed user | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_check_starring**
> user_current_check_starring(owner, repo)

Whether the authenticated is starring the repo

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo

try:
    # Whether the authenticated is starring the repo
    api_instance.user_current_check_starring(owner, repo)
except ApiException as e:
    print("Exception when calling UserApi->user_current_check_starring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_delete_follow**
> user_current_delete_follow(username)

Unfollow a user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user to unfollow

try:
    # Unfollow a user
    api_instance.user_current_delete_follow(username)
except ApiException as e:
    print("Exception when calling UserApi->user_current_delete_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user to unfollow | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_delete_gpg_key**
> user_current_delete_gpg_key(id)

Remove a GPG key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | id of key to delete

try:
    # Remove a GPG key
    api_instance.user_current_delete_gpg_key(id)
except ApiException as e:
    print("Exception when calling UserApi->user_current_delete_gpg_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of key to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_delete_key**
> user_current_delete_key(id)

Delete a public key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | id of key to delete

try:
    # Delete a public key
    api_instance.user_current_delete_key(id)
except ApiException as e:
    print("Exception when calling UserApi->user_current_delete_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of key to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_delete_star**
> user_current_delete_star(owner, repo)

Unstar the given repo

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to unstar
repo = 'repo_example' # str | name of the repo to unstar

try:
    # Unstar the given repo
    api_instance.user_current_delete_star(owner, repo)
except ApiException as e:
    print("Exception when calling UserApi->user_current_delete_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to unstar | 
 **repo** | **str**| name of the repo to unstar | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_get_gpg_key**
> GPGKey user_current_get_gpg_key(id)

Get a GPG key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | id of key to get

try:
    # Get a GPG key
    api_response = api_instance.user_current_get_gpg_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_get_gpg_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of key to get | 

### Return type

[**GPGKey**](GPGKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_get_key**
> PublicKey user_current_get_key(id)

Get a public key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | id of key to get

try:
    # Get a public key
    api_response = api_instance.user_current_get_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_get_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of key to get | 

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_followers**
> list[User] user_current_list_followers(page=page, limit=limit)

List the authenticated user's followers

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the authenticated user's followers
    api_response = api_instance.user_current_list_followers(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_following**
> list[User] user_current_list_following(page=page, limit=limit)

List the users that the authenticated user is following

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the users that the authenticated user is following
    api_response = api_instance.user_current_list_following(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_gpg_keys**
> list[GPGKey] user_current_list_gpg_keys(page=page, limit=limit)

List the authenticated user's GPG keys

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the authenticated user's GPG keys
    api_response = api_instance.user_current_list_gpg_keys(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_gpg_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[GPGKey]**](GPGKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_keys**
> list[PublicKey] user_current_list_keys(fingerprint=fingerprint, page=page, limit=limit)

List the authenticated user's public keys

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
fingerprint = 'fingerprint_example' # str | fingerprint of the key (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the authenticated user's public keys
    api_response = api_instance.user_current_list_keys(fingerprint=fingerprint, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| fingerprint of the key | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[PublicKey]**](PublicKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_repos**
> list[Repository] user_current_list_repos(page=page, limit=limit)

List the repos that the authenticated user owns or has access to

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the repos that the authenticated user owns or has access to
    api_response = api_instance.user_current_list_repos(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_starred**
> list[Repository] user_current_list_starred(page=page, limit=limit)

The repos that the authenticated user has starred

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # The repos that the authenticated user has starred
    api_response = api_instance.user_current_list_starred(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_starred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_list_subscriptions**
> list[Repository] user_current_list_subscriptions(page=page, limit=limit)

List repositories watched by the authenticated user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List repositories watched by the authenticated user
    api_response = api_instance.user_current_list_subscriptions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_post_gpg_key**
> GPGKey user_current_post_gpg_key(body=body)

Create a GPG key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateGPGKeyOption() # CreateGPGKeyOption |  (optional)

try:
    # Create a GPG key
    api_response = api_instance.user_current_post_gpg_key(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_post_gpg_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGPGKeyOption**](CreateGPGKeyOption.md)|  | [optional] 

### Return type

[**GPGKey**](GPGKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_post_key**
> PublicKey user_current_post_key(body=body)

Create a public key

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateKeyOption() # CreateKeyOption |  (optional)

try:
    # Create a public key
    api_response = api_instance.user_current_post_key(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_post_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKeyOption**](CreateKeyOption.md)|  | [optional] 

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_put_follow**
> user_current_put_follow(username)

Follow a user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user to follow

try:
    # Follow a user
    api_instance.user_current_put_follow(username)
except ApiException as e:
    print("Exception when calling UserApi->user_current_put_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user to follow | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_put_star**
> user_current_put_star(owner, repo)

Star the given repo

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo to star
repo = 'repo_example' # str | name of the repo to star

try:
    # Star the given repo
    api_instance.user_current_put_star(owner, repo)
except ApiException as e:
    print("Exception when calling UserApi->user_current_put_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to star | 
 **repo** | **str**| name of the repo to star | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_current_tracked_times**
> list[TrackedTime] user_current_tracked_times(since=since, before=before)

List the current user's tracked times

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
since = '2013-10-20T19:20:30+01:00' # datetime | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)

try:
    # List the current user's tracked times
    api_response = api_instance.user_current_tracked_times(since=since, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_current_tracked_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only show times updated after the given time. This is a timestamp in RFC 3339 format | [optional] 
 **before** | **datetime**| Only show times updated before the given time. This is a timestamp in RFC 3339 format | [optional] 

### Return type

[**list[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_delete_access_token**
> user_delete_access_token(username, token)

delete an access token

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
token = 'token_example' # str | token to be deleted, identified by ID and if not available by name

try:
    # delete an access token
    api_instance.user_delete_access_token(username, token)
except ApiException as e:
    print("Exception when calling UserApi->user_delete_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **token** | **str**| token to be deleted, identified by ID and if not available by name | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_delete_email**
> user_delete_email(body=body)

Delete email addresses

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.DeleteEmailOption() # DeleteEmailOption |  (optional)

try:
    # Delete email addresses
    api_instance.user_delete_email(body=body)
except ApiException as e:
    print("Exception when calling UserApi->user_delete_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteEmailOption**](DeleteEmailOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_delete_o_auth2_application**
> user_delete_o_auth2_application(id)

delete an OAuth2 Application

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | token to be deleted

try:
    # delete an OAuth2 Application
    api_instance.user_delete_o_auth2_application(id)
except ApiException as e:
    print("Exception when calling UserApi->user_delete_o_auth2_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| token to be deleted | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get**
> User user_get(username)

Get a user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user to get

try:
    # Get a user
    api_response = api_instance.user_get(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user to get | 

### Return type

[**User**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_current**
> User user_get_current()

Get the authenticated user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))

try:
    # Get the authenticated user
    api_response = api_instance.user_get_current()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_heatmap_data**
> list[UserHeatmapData] user_get_heatmap_data(username)

Get a user's heatmap

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user to get

try:
    # Get a user's heatmap
    api_response = api_instance.user_get_heatmap_data(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_heatmap_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user to get | 

### Return type

[**list[UserHeatmapData]**](UserHeatmapData.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_o_auth2_application**
> OAuth2Application user_get_o_auth2_application(id)

get an OAuth2 Application

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
id = 789 # int | Application ID to be found

try:
    # get an OAuth2 Application
    api_response = api_instance.user_get_o_auth2_application(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_o_auth2_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application ID to be found | 

### Return type

[**OAuth2Application**](OAuth2Application.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_oauth2_application**
> list[OAuth2Application] user_get_oauth2_application(page=page, limit=limit)

List the authenticated user's oauth2 applications

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the authenticated user's oauth2 applications
    api_response = api_instance.user_get_oauth2_application(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_oauth2_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[OAuth2Application]**](OAuth2Application.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_stop_watches**
> list[StopWatch] user_get_stop_watches(page=page, limit=limit)

Get list of all existing stopwatches

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # Get list of all existing stopwatches
    api_response = api_instance.user_get_stop_watches(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_stop_watches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[StopWatch]**](StopWatch.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_get_tokens**
> list[AccessToken] user_get_tokens(username, page=page, limit=limit)

List the authenticated user's access tokens

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the authenticated user's access tokens
    api_response = api_instance.user_get_tokens(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[AccessToken]**](AccessToken.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_emails**
> list[Email] user_list_emails()

List the authenticated user's email addresses

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))

try:
    # List the authenticated user's email addresses
    api_response = api_instance.user_list_emails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_emails: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Email]**](Email.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_followers**
> list[User] user_list_followers(username, page=page, limit=limit)

List the given user's followers

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the given user's followers
    api_response = api_instance.user_list_followers(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_following**
> list[User] user_list_following(username, page=page, limit=limit)

List the users that the given user is following

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the users that the given user is following
    api_response = api_instance.user_list_following(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_gpg_keys**
> list[GPGKey] user_list_gpg_keys(username, page=page, limit=limit)

List the given user's GPG keys

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the given user's GPG keys
    api_response = api_instance.user_list_gpg_keys(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_gpg_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[GPGKey]**](GPGKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_keys**
> list[PublicKey] user_list_keys(username, fingerprint=fingerprint, page=page, limit=limit)

List the given user's public keys

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
fingerprint = 'fingerprint_example' # str | fingerprint of the key (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the given user's public keys
    api_response = api_instance.user_list_keys(username, fingerprint=fingerprint, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **fingerprint** | **str**| fingerprint of the key | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[PublicKey]**](PublicKey.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_repos**
> list[Repository] user_list_repos(username, page=page, limit=limit)

List the repos owned by the given user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the repos owned by the given user
    api_response = api_instance.user_list_repos(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_starred**
> list[Repository] user_list_starred(username, page=page, limit=limit)

The repos that the given user has starred

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # The repos that the given user has starred
    api_response = api_instance.user_list_starred(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_starred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_subscriptions**
> list[Repository] user_list_subscriptions(username, page=page, limit=limit)

List the repositories watched by a user

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
username = 'username_example' # str | username of the user
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List the repositories watched by a user
    api_response = api_instance.user_list_subscriptions(username, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of the user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_list_teams**
> list[Team] user_list_teams(page=page, limit=limit)

List all the teams a user belongs to

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List all the teams a user belongs to
    api_response = api_instance.user_list_teams(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_search**
> InlineResponse2001 user_search(q=q, uid=uid, page=page, limit=limit)

Search for users

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
q = 'q_example' # str | keyword (optional)
uid = 789 # int | ID of the user to search for (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # Search for users
    api_response = api_instance.user_search(q=q, uid=uid, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword | [optional] 
 **uid** | **int**| ID of the user to search for | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

# **user_update_o_auth2_application**
> OAuth2Application user_update_o_auth2_application(body, id)

update an OAuth2 Application, this includes regenerating the client secret

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
api_instance = gitea.UserApi(gitea.ApiClient(configuration))
body = gitea.CreateOAuth2ApplicationOptions() # CreateOAuth2ApplicationOptions | 
id = 789 # int | application to be updated

try:
    # update an OAuth2 Application, this includes regenerating the client secret
    api_response = api_instance.user_update_o_auth2_application(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_update_o_auth2_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOAuth2ApplicationOptions**](CreateOAuth2ApplicationOptions.md)|  | 
 **id** | **int**| application to be updated | 

### Return type

[**OAuth2Application**](OAuth2Application.md)

### Authorization

[AccessToken](../gitea/docs/README.md#AccessToken), [AuthorizationHeaderToken](../gitea/docs/README.md#AuthorizationHeaderToken), [BasicAuth](../gitea/docs/README.md#BasicAuth), [SudoHeader](../gitea/docs/README.md#SudoHeader), [SudoParam](../gitea/docs/README.md#SudoParam), [TOTPHeader](../gitea/docs/README.md#TOTPHeader), [Token](../gitea/docs/README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../gitea/docs/README.md#documentation-for-api-endpoints) [[Back to Model list]](../gitea/docs/README.md#documentation-for-models) [[Back to README]](../gitea/docs/README.md)

