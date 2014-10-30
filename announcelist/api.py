# -*- coding: utf-8 -*-
import ssl
ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1

import requests
import logging
import httplib
httplib.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

BASE_URL = 'https://api.dreamhost.com/'


def test():
    params = {
        'key': '6SHU5P2HLDAYECUM',
        'cmd': 'user-list_users_no_pw',
        'unique_id': '4082432',
        'format': 'python'
    }

    # return requests.get(BASE_URL, params=params, verify=False)
    return requests.get('https://api.dreamhost.com/?key=6SHU5P2HLDAYECUM&cmd=user-list_users_no_pw&unique_id=914082432&format=python')


if __name__ == "__main__":
    print test()
