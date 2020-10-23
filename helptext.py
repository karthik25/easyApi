import textwrap


class Helptext:
    def __init__(self):
        pass

    @staticmethod
    def get_help_text():
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

        '''

        print(textwrap.dedent(sample_text))
