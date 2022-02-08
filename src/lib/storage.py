import requests
import base64
import src.lib.config as config
import src.lib.auth as auth


def upload_image(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'file': str(encoded_string)[2:-1],
        'type': 'MMS'
    }
    headers = auth.get_headers(config.api_key, config.api_secret)
    return requests.post(config.get_url('/storage/v1/files'), headers=headers, json=data)


def upload_rcs_image(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'file': str(encoded_string)[2:-1],
        'type': 'RCS'
    }
    headers = auth.get_headers(config.api_key, config.api_secret)
    return requests.post(config.get_url('/storage/v1/files'), headers=headers, json=data)


def upload_kakao_image(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'file': str(encoded_string)[2:-1],
        'type': 'KAKAO'
    }
    headers = auth.get_headers(config.api_key, config.api_secret)
    return requests.post(config.get_url('/storage/v1/files'), headers=headers, json=data)
