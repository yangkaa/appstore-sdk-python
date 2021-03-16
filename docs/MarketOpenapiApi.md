# openapi_client.MarketOpenapiApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](MarketOpenapiApi.md#create_app) | **POST** /app-server/openapi/apps | 创建应用
[**create_app_version**](MarketOpenapiApi.md#create_app_version) | **POST** /app-server/openapi/apps/{appID}/versions | 创建应用版本
[**get_app_hub_info**](MarketOpenapiApi.md#get_app_hub_info) | **GET** /app-server/openapi/apps/{appID}/apphubinfo | 获取镜像仓库信息
[**get_market_info**](MarketOpenapiApi.md#get_market_info) | **GET** /app-server/openapi/info | 获取商店信息
[**get_orgs**](MarketOpenapiApi.md#get_orgs) | **GET** /app-server/openapi/organizations | 获取组织机构(行业)列表
[**get_user_app_detail**](MarketOpenapiApi.md#get_user_app_detail) | **GET** /app-server/openapi/apps/{appID} | 应用详情
[**get_user_app_list**](MarketOpenapiApi.md#get_user_app_list) | **GET** /app-server/openapi/apps | 应用列表
[**get_user_app_version_detail**](MarketOpenapiApi.md#get_user_app_version_detail) | **GET** /app-server/openapi/apps/{appID}/versions/{version} | 应用版本信息
[**get_user_app_versions**](MarketOpenapiApi.md#get_user_app_versions) | **GET** /app-server/openapi/apps/{appID}/versions | 应用版本列表
[**update_app**](MarketOpenapiApi.md#update_app) | **PUT** /app-server/openapi/apps/{appID} | 更新应用信息


# **create_app**
> V1AppDetailInfoResponse create_app(body, market_domain=market_domain)

创建应用

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    body = openapi_client.V1AppModelCreateRequest() # V1AppModelCreateRequest | 
market_domain = 'market_domain_example' # str | 商店域 (optional)

    try:
        # 创建应用
        api_response = api_instance.create_app(body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AppModelCreateRequest**](V1AppModelCreateRequest.md)|  | 
 **market_domain** | **str**| 商店域 | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Field validation |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_version**
> V1AppVersionBase create_app_version(app_id, body, market_domain=market_domain)

创建应用版本

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
body = openapi_client.V1CreateAppPaaSVersionRequest() # V1CreateAppPaaSVersionRequest | 
market_domain = 'market_domain_example' # str | 商店域 (optional)

    try:
        # 创建应用版本
        api_response = api_instance.create_app_version(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **body** | [**V1CreateAppPaaSVersionRequest**](V1CreateAppPaaSVersionRequest.md)|  | 
 **market_domain** | **str**| 商店域 | [optional] 

### Return type

[**V1AppVersionBase**](V1AppVersionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_hub_info**
> V1AppImageHubInfoResponse get_app_hub_info(app_id, market_domain=market_domain)

获取镜像仓库信息

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
market_domain = 'market_domain_example' # str | 商店域 (optional)

    try:
        # 获取镜像仓库信息
        api_response = api_instance.get_app_hub_info(app_id, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_app_hub_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **market_domain** | **str**| 商店域 | [optional] 

### Return type

[**V1AppImageHubInfoResponse**](V1AppImageHubInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_info**
> V1MarketInfoResponse get_market_info(market_domain=market_domain)

获取商店信息

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | 商店域 (optional)

    try:
        # 获取商店信息
        api_response = api_instance.get_market_info(market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_market_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| 商店域 | [optional] 

### Return type

[**V1MarketInfoResponse**](V1MarketInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orgs**
> list[V1Organization] get_orgs()

获取组织机构(行业)列表

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    
    try:
        # 获取组织机构(行业)列表
        api_response = api_instance.get_orgs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_orgs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1Organization]**](V1Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_detail**
> V1AppDetailInfoResponse get_user_app_detail(app_id, market_domain)

应用详情

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
market_domain = 'market_domain_example' # str | 商店域

    try:
        # 应用详情
        api_response = api_instance.get_user_app_detail(app_id, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **market_domain** | **str**| 商店域 | 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_list**
> V1UserAppListResponse get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)

应用列表

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | 商店域
query = 'query_example' # str | 搜索项 (optional)
query_all = True # bool | 是否查询全部 (optional)
page = 56 # int | 页码 (optional)
page_size = 56 # int | 每页的大小. -1 表示不限制 (optional)

    try:
        # 应用列表
        api_response = api_instance.get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| 商店域 | 
 **query** | **str**| 搜索项 | [optional] 
 **query_all** | **bool**| 是否查询全部 | [optional] 
 **page** | **int**| 页码 | [optional] 
 **page_size** | **int**| 每页的大小. -1 表示不限制 | [optional] 

### Return type

[**V1UserAppListResponse**](V1UserAppListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | market not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_version_detail**
> V1AppVersionDetailResponse get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)

应用版本信息

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
version = 'version_example' # str | 应用版本
market_domain = 'market_domain_example' # str | 商店域 (optional)
for_install = True # bool | 使用用于安装 (optional)
get_template = True # bool | 是否获取模板 (optional)

    try:
        # 应用版本信息
        api_response = api_instance.get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_version_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **version** | **str**| 应用版本 | 
 **market_domain** | **str**| 商店域 | [optional] 
 **for_install** | **bool**| 使用用于安装 | [optional] 
 **get_template** | **bool**| 是否获取模板 | [optional] 

### Return type

[**V1AppVersionDetailResponse**](V1AppVersionDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_versions**
> V1AppVersionListResponse get_user_app_versions(app_id, query_all, market_domain)

应用版本列表

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
query_all = True # bool | query all versions, must have write perm
market_domain = 'market_domain_example' # str | 商店域

    try:
        # 应用版本列表
        api_response = api_instance.get_user_app_versions(app_id, query_all, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **query_all** | **bool**| query all versions, must have write perm | 
 **market_domain** | **str**| 商店域 | 

### Return type

[**V1AppVersionListResponse**](V1AppVersionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> V1AppDetailInfoResponse update_app(app_id, body, market_domain=market_domain)

更新应用信息

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | 应用 ID
body = openapi_client.V1AppUpdateRequest() # V1AppUpdateRequest | 
market_domain = 'market_domain_example' # str | 商店域 (optional)

    try:
        # 更新应用信息
        api_response = api_instance.update_app(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| 应用 ID | 
 **body** | [**V1AppUpdateRequest**](V1AppUpdateRequest.md)|  | 
 **market_domain** | **str**| 商店域 | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

