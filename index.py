#main.py
import os.path
from mod_python import apache
import yaml

def handler(req):
    req.content_type = "text/plain"
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')) as configStream:
	try:
            parsed = yaml.load(configStream)
	    req.write(str(parsed))
	    return apache.OK
	except yaml.YAMLError as exc:
            req.write(str(exc))
            #return apache.HTTP_INTERNAL_SERVER_ERROR
            return apache.OK
