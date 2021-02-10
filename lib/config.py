import os
import configparser

libdir = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(libdir + '/config.ini')
apiKey = config['AUTH']['api_key']
apiSecret = config['AUTH']['api_secret']
protocol = config['SERVER']['protocol']
domain = config['SERVER']['domain']
prefix = config['SERVER']['prefix'] and config['SERVER']['prefix'] or ''

def getUrl(path):
  url = '%s://%s' % (protocol, domain)
  if prefix != '':
    url = url + prefix
  url = url + path
  return url
