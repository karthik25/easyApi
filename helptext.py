import textwrap


class Helptext:
    def __init__(self):
        pass

    @staticmethod
    def print_help_text():
        sample_text = '''
        usage: easyApi [options]

        Options:

        -h	: Display this help text
        -o	: OpenApi json url
        -c	: Initial settings (if you don't want to type it in everytime)
        -s 	: Disable ssl validation

        Sample usages:

        ***Option 1***

        easyApi -o https://someurl.com/swagger/v1/swagger.json -c c:/users/administrator/config.json

        [config.json sample]

        {
          "access_token": "",
          "token_endpoint": "https://idp/connect/token"
          "client_id": "SomeClientId",
          "client_secret": "SomeClientSecret",
          "grant_type": "client_credentials",
          "scope": "someApi"
          "token_type": "Bearer",
          "disable_ssl": False,
          "is_debug": False
        }

        ***Option 2***

        easyApi -o https://someurl/swagger/v1/swagger.json
            > list # to see the apis identified
            > set list # to list the current settings, to see the defaults
            > set multiple token_url=https://idp/connet/token,client_id=SomeClientId,client_secret=SomeClientSecret,grant_type=client_credentials,scope=someApi,token_type=Bearer
            > set is_debug True
        
        Executing Apis:
        
        Running the list command lists the API's (GET only)
        
           Id   |             Key     | Url
        --------------------------------------------------------------------------
            1   |            mine     | /api/values
            2   |          marble     | /api/values/name/{name}
            3   |          mellow     | /api/values/random/{count}
            
            
        To run the api with id 3, you can do the following:
        
            > exec mellow count=5
        
        As you can see, to execute an api, you have to use the exec command, followed by the key, which is then followed 
        by a dictionary of parameters to replace the variables in the uri (count in this case). Same effect can be achieved
        by running the following commands as well:
        
            > run mellow count=5
        
            > call mellow count=5
        
        Filtering results:
        
        You can use the filter command to filter the last result. This command would list the entries with the email address
        set to john.doe@mail.com
        
            > filter email john.doe@mail.com
        
        You can also pass modifiers to the filter command. As of now the only available modified is partial_match. This command
        would list all the items with a partial match of john
        
            > filter email john partial_match=1        

        '''

        print(textwrap.dedent(sample_text))
