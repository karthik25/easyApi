import getopt
import sys
import os
from settings import Settings
from shell import Shell
from helptext import Helptext
from utils.stringutils import Stringutils


optlist, args = getopt.getopt(sys.argv[1:], 'shdc:o:')

oapi_url = ''
config_file = ''
ssl_disable = False
help_only = False
is_debug = False

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg
    if opt in ['-c']:
        config_file = arg
    if opt in ['-s']:
        ssl_disable = True
    if opt in ['-h']:
        help_only = True
    if opt in ['-d']:
        is_debug = True

if config_file != '' and not os.path.isfile(config_file):
    print("easyApi Shell: config file passed is not valid, use the 'set' command to set the required settings")

if oapi_url == "" or help_only:
    Helptext.print_help_text()
else:
    Settings.set_key_value("oapi_url", oapi_url)
    Settings.set_key_value("disable_ssl", ssl_disable)
    Settings.set_key_value("is_debug", is_debug)

    if config_file != '' and os.path.isfile(config_file):
        config_dict = Stringutils.config_file_to_dict(config_file)
        Settings.set_multiple_keys(config_dict)

    shell = Shell()
    shell.start()
