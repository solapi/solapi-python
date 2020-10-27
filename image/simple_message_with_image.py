import requests
import json
import sys
import os.path
import image

sys.path.append('../')

from auth import auth
import config

if __name__ == '__main__':
    # 이미지를 바꾸시려면 testImage.jpg 대신
    # 사용하실 이미지가 있는 파일 경로를 넣어주세요
    imageInfo = json.loads(image.createImage('./testImage.jpg', config.getUrl('/storage/v1/files'), auth.get_headers(config.apiKey, config.apiSecret)).text)
    print(imageInfo)
    data = {
        'message': {
            'to': '수신번호 입력',
            'from': '발신번호 입력',
            'text': '발송 예제',
            'imageId': imageInfo['fileId']
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'), headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
