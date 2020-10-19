class Setter:
    key_value_dictionary = {
        "access_token": "",
        "token_url": "",
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
    def get_api_headers():
        if Setter.key_value_dictionary["token_type"] == "None":
            return {}

        raise Exception("do not know how to handle {0}".format(Setter.key_value_dictionary["token_type"]))
