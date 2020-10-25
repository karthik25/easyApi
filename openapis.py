import urllib.request
import ssl
import json
from settings import Settings
from urllib.parse import urlparse


class Openapis:
    api_listing = []

    api_short_words = ["mine", "marble", "mellow", "futuristic", "zippy", "cap", "fragile", "torpid", "debt","exuberant",
                       "lovely", "subsequent", "advertisement", "fence", "steady", "impulse", "alive", "back", "overrated",
                       "romantic", "office", "entertain", "employ", "knowledgeable", "church", "follow", "amazing","watery",
                       "embarrassed", "curved", "rely", "chilly", "domineering", "elastic", "influence", "appear", "squirrel",
                       "breakable", "distance", "snow", "truthful", "wriggle", "merciful", "bustling", "wool", "stare", "tap",
                       "sticky", "honey", "analyze", "load", "acidic", "happen", "hallowed", "humdrum", "glistening", "step",
                       "advise", "chemical", "tomatoes", "spiders", "nice", "bulb", "memory", "suspend", "royal", "hill",
                       "abashed", "suppose", "stereotyped", "wax", "surprise", "cup", "lazy", "astonishing", "crabby", "festive",
                       "fasten", "calendar", "adorable", "country", "wistful", "tenuous", "sloppy", "jazzy", "sister", "horses",
                       "towering", "illustrious", "fall", "spotless", "eye", "system", "thick"]

    @staticmethod
    def get_all_apis():
        return Openapis.api_listing

    @staticmethod
    def get_base_url():
        oapi_url = Settings.get_value_by_key("oapi_url")
        parsed_uri = urlparse(oapi_url)
        result = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return result

    # todo: add try...except
    @staticmethod
    def populate_all_apis(url):
        print("easyApi Shell: getting the apis...please wait")

        try:
            ctx = ssl.create_default_context()
            if Settings.is_ssl_enabled():
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE

            oapi_json = urllib.request.urlopen(url, context=ctx).read()
            oapi_config = json.loads(oapi_json)
            i = 1
            for path in oapi_config["paths"]:
                api_details = oapi_config["paths"][path]
                if "get" in api_details.keys():
                    getter = api_details["get"]
                    if getter is not None:
                        Openapis.api_listing.append({
                            "id": str(i),
                            "key": Openapis.api_short_words[i - 1],
                            "url": path,
                            "method": "get"
                        })
                        i = i + 1

            print("easyApi Shell: processed the apis")
            return True
        except:
            print("easyApi Shell: unable to read the api spec")
            return False

    @staticmethod
    def print_all_apis():
        print("{0: >5}   | {1: >15}     | {2}".format("Id", "Key", "Url"))
        print("--------------------------------------------------------------------------")
        for api in Openapis.api_listing:
            print("{0: >5}   | {1: >15}     | {2}".format(api["id"],api["key"],api["url"]))

    @staticmethod
    def print_selected_apis(apis):
        print("{0: >5}   | {1: >15}     | {2}".format("Id", "Key", "Url"))
        print("--------------------------------------------------------------------------")
        for api in apis:
            print("{0: >5}   | {1: >15}     | {2}".format(api["id"],api["key"],api["url"]))