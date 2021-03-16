# openapi-client
Resource for managing app-server

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    body = openapi_client.V1AppModelCreateRequest() # V1AppModelCreateRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # create an app model
        api_response = api_instance.create_app(body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MarketOpenapiApi* | [**create_app**](docs/MarketOpenapiApi.md#create_app) | **POST** /app-server/openapi/apps | create an app model
*MarketOpenapiApi* | [**create_app_version**](docs/MarketOpenapiApi.md#create_app_version) | **POST** /app-server/openapi/apps/{appID}/versions | post an app version
*MarketOpenapiApi* | [**get_app_hub_info**](docs/MarketOpenapiApi.md#get_app_hub_info) | **GET** /app-server/openapi/apps/{appID}/apphubinfo | get app image save info
*MarketOpenapiApi* | [**get_market_info**](docs/MarketOpenapiApi.md#get_market_info) | **GET** /app-server/openapi/info | get mrket info
*MarketOpenapiApi* | [**get_user_app_detail**](docs/MarketOpenapiApi.md#get_user_app_detail) | **GET** /app-server/openapi/apps/{appID} | Query the specified application details
*MarketOpenapiApi* | [**get_user_app_list**](docs/MarketOpenapiApi.md#get_user_app_list) | **GET** /app-server/openapi/apps | A list of installable applications
*MarketOpenapiApi* | [**get_user_app_version_detail**](docs/MarketOpenapiApi.md#get_user_app_version_detail) | **GET** /app-server/openapi/apps/{appID}/versions/{version} | Query the specified version details of the specified application
*MarketOpenapiApi* | [**get_user_app_versions**](docs/MarketOpenapiApi.md#get_user_app_versions) | **GET** /app-server/openapi/apps/{appID}/versions | Query the specified application version list
*MarketOpenapiApi* | [**update_app**](docs/MarketOpenapiApi.md#update_app) | **PUT** /app-server/openapi/apps/{appID} | update app model base info
*RegistryApiApi* | [**do_auth**](docs/RegistryApiApi.md#do_auth) | **GET** /app-server/v1/registry/auth | image registry auth server


## Documentation For Models

 - [ControllerResult](docs/ControllerResult.md)
 - [RestfulutilResult](docs/RestfulutilResult.md)
 - [V1AppBaseInfo](docs/V1AppBaseInfo.md)
 - [V1AppDetailInfoResponse](docs/V1AppDetailInfoResponse.md)
 - [V1AppImageHubInfoResponse](docs/V1AppImageHubInfoResponse.md)
 - [V1AppModelCreateRequest](docs/V1AppModelCreateRequest.md)
 - [V1AppUpdateRequest](docs/V1AppUpdateRequest.md)
 - [V1AppVersionBase](docs/V1AppVersionBase.md)
 - [V1AppVersionDetailResponse](docs/V1AppVersionDetailResponse.md)
 - [V1AppVersionListResponse](docs/V1AppVersionListResponse.md)
 - [V1CreateAppPaaSVersionRequest](docs/V1CreateAppPaaSVersionRequest.md)
 - [V1ImageInfo](docs/V1ImageInfo.md)
 - [V1MarketInfoResponse](docs/V1MarketInfoResponse.md)
 - [V1MarketUIAppTagsResponse](docs/V1MarketUIAppTagsResponse.md)
 - [V1StoreAppVersionTemplate](docs/V1StoreAppVersionTemplate.md)
 - [V1StoreAppVersionTempleteApp](docs/V1StoreAppVersionTempleteApp.md)
 - [V1StoreAppVersionTempleteAppDepService](docs/V1StoreAppVersionTempleteAppDepService.md)
 - [V1StoreAppVersionTempleteAppEnv](docs/V1StoreAppVersionTempleteAppEnv.md)
 - [V1StoreAppVersionTempleteAppExtendMethodRule](docs/V1StoreAppVersionTempleteAppExtendMethodRule.md)
 - [V1StoreAppVersionTempleteAppPluginConfig](docs/V1StoreAppVersionTempleteAppPluginConfig.md)
 - [V1StoreAppVersionTempleteAppPort](docs/V1StoreAppVersionTempleteAppPort.md)
 - [V1StoreAppVersionTempleteAppProbe](docs/V1StoreAppVersionTempleteAppProbe.md)
 - [V1StoreAppVersionTempleteAppShareVolume](docs/V1StoreAppVersionTempleteAppShareVolume.md)
 - [V1StoreAppVersionTempleteAppVolume](docs/V1StoreAppVersionTempleteAppVolume.md)
 - [V1StoreAppVersionTempletePlugin](docs/V1StoreAppVersionTempletePlugin.md)
 - [V1StoreAppVersionTempletePluginConfigGroup](docs/V1StoreAppVersionTempletePluginConfigGroup.md)
 - [V1StoreAppVersionTempletePluginConfigGroupOption](docs/V1StoreAppVersionTempletePluginConfigGroupOption.md)
 - [V1UserAppListResponse](docs/V1UserAppListResponse.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

huangrh@goodrain.com


