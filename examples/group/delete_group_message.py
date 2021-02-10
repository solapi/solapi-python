import requests
import configparser
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # [INPUT_MESSAGE_ID] 에 메세지 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    data = {'messageIds':
        [
            # 배열로 id를 입력하여 한 요청에 여러개의 메세지를 제거할 수 있습니다.
            '[INPUT_MESSAGE_ID]',
            '[INPUT_MESSAGE_ID]'
        ]
    }
    res = requests.delete(config.getUrl('/messages/v4/groups/[INPUT_GROUP_ID]/messages',
                          headers=auth.get_headers(config.apiKey, config.apiSecret),
                          json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
