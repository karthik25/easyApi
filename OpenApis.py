import urllib.request
import ssl
import json


class Openapis:
    api_listing = []

    base_url = "https://localhost:44391"

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
    def populate_all_apis(url):
        print("Openapis: getting the apis")

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        oapi_json = urllib.request.urlopen(url, context=ctx).read()
        oapi_config = json.loads(oapi_json)
        i = 1
        for path in oapi_config["paths"]:
            api_details = oapi_config["paths"][path]
            getter = api_details["get"]
            if getter is not None:
                Openapis.api_listing.append({
                    "id": i,
                    "key": Openapis.api_short_words[i - 1],
                    "url": path,
                    "method": "get"
                })
                i = i + 1

    @staticmethod
    def print_all_apis():
        print("{0: >5}   | {1: >15}     | {2}".format("Id", "Key", "Url"))
        print("--------------------------------------------------------------------------")
        for api in Openapis.api_listing:
            print("{0: >5}   | {1: >15}     | {2}".format(api["id"],api["key"],api["url"]))