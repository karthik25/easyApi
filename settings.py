import urllib.request
import json
import urllib.parse
import ssl


class Settings:
    key_value_dictionary = {
        "oapi_url": "",
        "access_token": "",
        "token_endpoint": "",
        "client_id": "",
        "client_secret": "",
        "grant_type": "client_credentials",
        "scope": "",
        "token_type": "None",
        "disable_ssl": False,
        "is_debug": False
    }

    @staticmethod
    def print_current_keys():
        for key in Settings.key_value_dictionary.keys():
            print("{0} => {1}".format(key, Settings.key_value_dictionary[key]))

    @staticmethod
    def get_current_keys():
        return Settings.key_value_dictionary.keys()

    @staticmethod
    def get_value_by_key(key):
        return Settings.key_value_dictionary[key]

    @staticmethod
    def is_ssl_enabled():
        return Settings.key_value_dictionary["disable_ssl"] == True

    @staticmethod
    def is_debug():
        return Settings.key_value_dictionary["is_debug"] == True

    @staticmethod
    def set_key_value(key, value):
        all_keys = Settings.key_value_dictionary.keys()
        if key not in all_keys:
            print("Unknown key {0}".format(key))  # raise an exception?
            return
        if type(Settings.key_value_dictionary[key]) == str:
            Settings.key_value_dictionary[key] = value
        else:
            Settings.key_value_dictionary[key] = bool(value) # find a safer way?

    @staticmethod
    def set_multiple_keys(dict):
        for key in dict.keys():
            if key in Settings.key_value_dictionary.keys():
                Settings.key_value_dictionary[key] = dict[key]

    @staticmethod
    def generate_access_token():
        full_url = Settings.key_value_dictionary["token_endpoint"]

        post_data = {
            "grant_type": Settings.key_value_dictionary["grant_type"],
            "scope": Settings.key_value_dictionary["scope"],
            "client_id": Settings.key_value_dictionary["client_id"],
            "client_secret": Settings.key_value_dictionary["client_secret"]
        }

        ctx = ssl.create_default_context()
        if Settings.is_ssl_enabled():
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

        encoded_data = urllib.parse.urlencode(post_data).encode()
        req = urllib.request.Request(full_url, data=encoded_data)
        token_response = urllib.request.urlopen(req,context=ctx)

        response_content = token_response.read()
        parsed_response = json.loads(response_content)
        access_token = parsed_response["access_token"]
        return access_token

    @staticmethod
    def get_api_headers():
        if Settings.key_value_dictionary["token_type"] == "None":
            print("Setter: token type is None - returning empty headers")
            return {}

        if Settings.key_value_dictionary["token_type"] == "Bearer":
            if Settings.key_value_dictionary["access_token"] != "":
                print("Setter: using the access token")
                return { "Authorization": "Bearer {0}".format(Settings.key_value_dictionary["access_token"])}
            else:
                if Settings.is_debug():
                    print("Setter: genreating the access token")
                accessToken = Settings.generate_access_token()
                if Settings.is_debug():
                    print("Setter: genreated the access token")
                return {"Authorization": "Bearer {0}".format(accessToken)}

        raise Exception("Do not know how to handle {0}".format(Settings.key_value_dictionary["token_type"]))
