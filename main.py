import getopt
import sys
from shell import Shell

optlist, args = getopt.getopt(sys.argv[1:], 'o:')

oapi_url = 'https://localhost:44391/swagger/v1/swagger.json'

for opt, arg in optlist:
    if opt in ['-o']:
        oapi_url = arg

shell = Shell()
shell.start(oapi_url=oapi_url)
