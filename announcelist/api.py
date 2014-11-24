# -*- coding: utf-8 -*-
import ssl
ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1

import requests
import logging
import httplib

BASE_URL = 'https://api.dreamhost.com/'


class AnnounceList(object):

    def enable_http_debug(self):
        httplib.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def send_request(self, params):
        return requests.get(BASE_URL, params=params, verify=False)

    @classmethod
    def test(self):
        params = {
            'key': '6SHU5P2HLDAYECUM',
            'cmd': 'user-list_users_no_pw',
            'format': 'json'
        }

        return self.send_request(params)

    def list_lists(self):
        params = {
            'cmd': 'announcement_list-list_lists',
        }

        return self.send_request(params)

    def list_subscribers(self):
        params = {
            'cmd': 'announcement_list-list_subscribers',
            'listname': '',
            'domain': '',
        }

        return self.send_request(params)

    def add_subscriber(self):
        params = {
            'cmd': 'announcement_list-add_subscriber',
            'listname': '',
            'domain': '',
            'email': '',
            'name': '',  # optional
        }

        return self.send_request(params)

    def remove_subscriber(self):
        params = {
            'cmd': 'announcement_list-remove_subscriber',
            'listname': '',
            'domain': '',
            'email': '',
        }

        return self.send_request(params)

    def post_announcement(self):
        params = {
            'cmd': 'announcement_list-post_announcement',
            'listname': '',
            'domain': '',
            'subject': '',  # optional
            'message': '',
            'name': '',
            'stamp': '',  # optional
            'charset': '',  # optional
            'type': '',  # optional
            'duplicate_ok': '',
        }

        return self.send_request(params)

if __name__ == "__main__":
    AnnounceList().enable_http_debug()
    print AnnounceList().test().text
