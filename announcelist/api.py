# -*- coding: utf-8 -*-
import ssl
ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1

import requests
import logging
import httplib

BASE_URL = 'https://api.dreamhost.com/'


def enable_http_debug():
    httplib.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def test():
    params = {
        'key': '6SHU5P2HLDAYECUM',
        'cmd': 'user-list_users_no_pw',
        'format': 'json'
    }

    return requests.get(BASE_URL, params=params, verify=False)


if __name__ == "__main__":
    print test()
