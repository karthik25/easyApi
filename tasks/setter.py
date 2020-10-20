import urllib.request
import json
import urllib.parse


class Setter:
    key_value_dictionary = {
        "access_token": "",
        "token_endpoint": "",
        "client_id": "",
        "client_secret": "",
        "grant_type": "client_credentials",
        "scope": "",
        "token_type": "None"
    }

    @staticmethod
    def print_current_keys():
        for key in Setter.key_value_dictionary.keys():
            print("{0} => {1}".format(key, Setter.key_value_dictionary[key]))

    @staticmethod
    def get_current_keys():
        return Setter.key_value_dictionary.keys()

    @staticmethod
    def set_key_value(key, value):
        all_keys = Setter.key_value_dictionary.keys()
        if key not in all_keys:
            print("Unknown key {0}".format(key))  # raise an exception?
            return
        Setter.key_value_dictionary[key] = value

    @staticmethod
    def set_multiple_keys(dict):
        for key in dict.keys():
            if key in Setter.key_value_dictionary.keys():
                Setter.key_value_dictionary[key] = dict[key]

    @staticmethod
    def generate_access_token():
        full_url = Setter.key_value_dictionary["token_endpoint"]

        post_data = {
            "grant_type": Setter.key_value_dictionary["grant_type"],
            "scope": Setter.key_value_dictionary["scope"],
            "client_id": Setter.key_value_dictionary["client_id"],
            "client_secret": Setter.key_value_dictionary["client_secret"]
        }

        encoded_data = urllib.parse.urlencode(post_data).encode()
        req = urllib.request.Request(full_url, data=encoded_data)
        token_response = urllib.request.urlopen(req)

        response_content = token_response.read()
        parsed_response = json.loads(response_content)
        access_token = parsed_response["access_token"]
        return access_token

    @staticmethod
    def get_api_headers():
        if Setter.key_value_dictionary["token_type"] == "None":
            print("Setter: token type is None - returning empty headers")
            return {}

        if Setter.key_value_dictionary["token_type"] == "Bearer":
            if Setter.key_value_dictionary["access_token"] is not None or Setter.key_value_dictionary["access_token"] != "":
                print("Setter: using the access token")
                return { "Authorization", "Bearer {0}".format(Setter.key_value_dictionary["access_token"])}
            else:
                print("Setter: genreating the access token")
                accessToken = Setter.generate_access_token()
                return {"Authorization", "Bearer {0}".format(accessToken)}

        raise Exception("Do not know how to handle {0}".format(Setter.key_value_dictionary["token_type"]))
