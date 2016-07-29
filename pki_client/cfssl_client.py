import requests
import os
import socket
import json
import logging

logger = logging.getLogger('cfssl_client')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

CERT_PATH = "C:\WS\cert.pem"
KEY_PATH = "C:\WS\key.pem"
CFSSL_URL = "http://192.168.99.100:8888"
MODE = True


def main():
    cert_path = CERT_PATH
    key_path = KEY_PATH
    mode = MODE
    cfssl_url = CFSSL_URL
    common_name = get_hostname()
    hosts = get_ip()
    names = [{
        "C" : "US",
        "L" : "San Francisco",
        "O" : "Example Company, LLC",
        "OU": "Operations",
        "ST": "California"
    }]
    logger.info('Starting')
    if not os.path.exists(cert_path):
        logger.info('Checking path')
        if mode:
            logger.info('Checking mode')
            url = '{0}/api/v1/cfssl/newcert'.format(cfssl_url)

            data = {
                'request': {
                    'CN'   : common_name,
                    'names': names,
                    'hosts': hosts,
                }
            }

            response = requests.post(url, data=json.dumps(data)).json()

            logger.debug('Response: {}'.format(str(response)))
            with open(cert_path, 'w') as fp:
                fp.write(response['result']['certificate'])

            with open(key_path, 'w') as fp:
                fp.write(response['result']['private_key'])


def get_ip():
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if not ip.startswith("127."):
            return ip


def get_hostname():
    return socket.getfqdn(socket.gethostname())


def execute():
    print get_ip()
    print get_hostname()


if __name__ == '__main__':
    main()
