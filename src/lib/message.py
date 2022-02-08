import requests
import platform
import src.lib.auth as auth
import src.lib.config as config

default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


def send_many(data):
    data['agent'] = default_agent
    return requests.post(config.get_url('/messages/v4/send-many'),
                         headers=auth.get_headers(config.api_key, config.api_secret), json=data)


def send_one(data):
    data['agent'] = default_agent
    return requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)


def post(path, data):
    return requests.post(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret), json=data)


def put(path, data, headers=None):
    if headers is None:
        headers = {}
    headers.update(auth.get_headers(config.api_key, config.api_secret))
    return requests.put(config.get_url(path), headers=headers, json=data)


def get(path, headers=None):
    if headers is None:
        headers = {}
    headers.update(auth.get_headers(config.api_key, config.api_secret))
    return requests.get(config.get_url(path), headers=headers)


def delete(path, data):
    if data is None:
        return requests.delete(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret))
    else:
        return requests.delete(config.get_url(path), headers=auth.get_headers(config.api_key, config.api_secret),
                               json=data)
