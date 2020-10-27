import requests
import configparser
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

if __name__ == '__main__':
    res = requests.get(config.getUrl('/messages/v4/groups'),
                       headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
