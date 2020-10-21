import re
import shlex
import urllib.request
import ssl
import json
from tasks.setter import Setter
from openapis import Openapis
from result import Result


class Exec:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "exec"

    def get_replaced_url(self, url, dict):
        get_params = re.findall(r'\{.*?\}', url)
        param_dict = {

        }
        for param in get_params:
            new_key = re.sub(r'[\{\}]', '', param)
            param_dict[new_key] = ""

        for key in dict.keys():
            if key in param_dict.keys():
                param_dict[key] = dict[key]

        new_url = url
        for key_value in param_dict:
            new_url = new_url.replace("{{{0}}}".format(key_value), param_dict[key_value])

        return new_url

    def get_param_dict(self, arguments):
        lexer = shlex.shlex(arguments, posix=True)
        lexer.whitespace_split = True
        lexer.whitespace = ','
        props = dict(pair.split('=', 1) for pair in lexer)
        return props

    def run(self, args):
        if len(args) != 1 and len(args) != 2:
            print("usage: exec <identifier> [<dictionary>]")

        identifier = args[0]
        arguments = args[1] if len(args) == 2 else ""

        all_apis = Openapis.get_all_apis()

        for api in all_apis:
            if api["key"] == identifier:
                param_dict = self.get_param_dict(arguments)
                url = self.get_replaced_url(api["url"], param_dict)

                # todo: if url still has {} stop proceeding

                print("calling {0}".format(url))

                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE

                full_url = "{0}{1}".format(Openapis.get_base_url(), url)
                req_headers = Setter.get_api_headers()

                req = urllib.request.Request(full_url, headers=req_headers)
                api_response = urllib.request.urlopen(req, context=ctx)

                response_info = api_response.info()
                response_content = api_response.read()
                response_type = response_info.get_content_type()
                if response_type == "application/json":
                    content_json = json.loads(response_content)
                    Result.store_result(content_json)
                    print(json.dumps(content_json, indent=4))
                else:
                    print(response_content)