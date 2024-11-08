import os
from warnings import filterwarnings

import urllib3
from dotenv import load_dotenv

from app.core.dir import get_basepath

basedir = get_basepath(__file__)
IS_PROD = os.environ.get("IS_PROD", False)

# Load .env
load_dotenv()

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filterwarnings("ignore")


class BaseConfig(object):
    # Test
    IS_TEST = True if os.environ.get("IS_TEST", "") else False
    MONGO_URI = "mongodb://admin:ha-sd9hplejf@localhost:27017/osv"