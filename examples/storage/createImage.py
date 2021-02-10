import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config
import image

if __name__ == '__main__':
    # 이미지를 바꾸시려면 testImage.jpg 대신
    # 사용하실 이미지가 있는 파일 경로를 넣어주세요
    res = image.createImage('./testImage.jpg', config.getUrl('/storage/v1/files'), auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
