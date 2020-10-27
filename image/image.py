import requests
import base64

def createImage(image_path, image_url, headers):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'file': str(encoded_string)[2:-1],
        'type': 'MMS'
    }
    return requests.post(image_url, headers=headers, json=data)
