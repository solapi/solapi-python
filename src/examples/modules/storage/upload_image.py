import json
import src.lib.storage as storage

'''
이미지 파일 업로드 예제
'''
if __name__ == '__main__':
    # 이미지를 바꾸시려면 testImage.jpg 대신 사용하실 이미지가 있는 파일 경로를 넣어주세요
    res = storage.upload_image('testImage.jpg')
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
