import requests
import configparser
import json
import sys
import os.path

sys.path.append('../')

from auth import auth
import config

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    res = requests.post(config.getUrl('/messages/v4/groups/[INPUT_GROUP_ID]/send'),
                        headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
