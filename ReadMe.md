## Getting Started :: easyApi

The **easyApi** project is intended to provide an environment to call and test apis without jumping across multiple applications. All you have to do is pass the swagger json url of a hosted api (OpenAPI) and easyApi will do the rest. It builds a list of all the `GET` apis offered and lets you run them with a veriety of shortcuts. Read through the read me to know more!

**usage:** easyApi [options]

**Options:**

    -h	: Display this help text
    -o	: OpenApi json url
    -c	: Initial settings (if you don't want to type it in every time)
    -s 	: Disable ssl validation
    -d 	: Enable debug mode

##### Sample usages:

***Option 1***

```
easyApi -o https://someurl.com/swagger/v1/swagger.json -c c:/users/administrator/config.json
```

The configuration file passed has the resemble the sample below. If the `token_type` is `Bearer`, 
either the `access_token` should be provided or the `client_id`,`client_secret`,`scope`, `token_endpoint`
should be provided. 

```json
{
  "token_endpoint": "https://idp/connect/token",
  "client_id": "SomeClientId",
  "client_secret": "SomeClientSecret",
  "grant_type": "client_credentials",
  "scope": "someApi",
  "token_type": "Bearer",
  "disable_ssl": false,
  "is_debug": false
}
```

The settings in this file is used to generate an access token using [RFC 6749](https://tools.ietf.org/html/rfc6749) (tested using the [identity server](https://docs.identityserver.io/en/dev/endpoints/token.html))

(or)

```json
{
  "access_token": "abc",
  "token_type": "Bearer",
  "disable_ssl": false,
  "is_debug": false
}
```

***Option 2***

```
easyApi -o https://someurl/swagger/v1/swagger.json
```

    # to see the apis identified
    > list
    # to list the current settings, to see the defaults
    > set list
    # to set multiple values at the same time 
    > set multiple token_url=https://idp/connet/token,client_id=SomeClientId,client_secret=SomeClientSecret,grant_type=client_credentials,scope=someApi,token_type=Bearer
    # to enable the debug mode
    > set is_debug True

#### Inspecting Apis:
        
The 'list' command can be used to inspect the apis discovered. Running list without any parameters would list all the apis discovered. 
This behavior can be modified by passing a number or a string. 
        
        # list all the apis
        > list
        # list the top 5 apis alone
        > list 5
        # list the apis that has the word users as part of it
        > list users

##### Executing Apis:

Running the list command lists the API's (GET only)

```text
   Id   |             Key     | Url
--------------------------------------------------------------------------
    1   |            mine     | /api/values
    2   |          marble     | /api/values/name/{name}
    3   |          mellow     | /api/values/random/{count}
```

To run the api with id 3, you can do the following:

    > exec mellow count=5

As you can see, to execute an api, you have to use the exec command, followed by the key, which is then followed 
by a dictionary of parameters to replace the variables in the uri (count in this case). Same effect can be achieved
by running the following commands as well:

    > run mellow count=5

    > call mellow count=5

You can also use the index to execute an api, for example

    > exec 3 count=5

***Filtering results:***

You can use the filter command to filter the last result. This command would list the entries with the email address
set to john.doe@mail.com

    > filter email john.doe@mail.com

You can also pass modifiers to the filter command. As of now the only available modified is partial_match. This command
would list all the items with a partial match of john

    > filter email john partial_match=1


***Using access tokens directly:***

If you are not using a configuration json file or using the set command to set the client id, secret etc, you can just
set the access token and token type as shown below to call apis

```
easyApi -s https://someurl/swagger/v1/swagger.json
```

    > set token_type=Bearer,access_token=abc

***No authorization headers:***

By default, token type is set to None. So no authentication headers sent because of this        

##### Building an Executable

In order to build an executable, you can do the following:

* Install `pyinstaller` using `pip`

```
> pip install pyinstaller
```

* Run `pyinstaller` as shown below

```
c:\easyApi> pyinstaller --onefile --onedir -n easyApi --distpath C:\easyApi\easyApi main.py
```
