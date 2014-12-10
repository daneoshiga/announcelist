# -*- coding: utf-8 -*-
import os
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
        key = os.environ.get('DREAMHOST_API_KEY', '6SHU5P2HLDAYECUM')
        params.update({
            'key': key,
            'format': 'json'
        })
        return requests.get(BASE_URL, params=params, verify=False)

    def test(self):
        params = {
            'cmd': 'user-list_users_no_pw',
        }

        return self.send_request(params)

    def list_lists(self):
        params = {
            'cmd': 'announcement_list-list_lists',
        }

        return self.send_request(params)

    def list_subscribers(self, listname, domain):
        params = {
            'cmd': 'announcement_list-list_subscribers',
            'listname': listname,
            'domain': domain,
        }

        return self.send_request(params)

    def add_subscriber(self, listname, domain, email, name=''):
        params = {
            'cmd': 'announcement_list-add_subscriber',
            'listname': listname,
            'domain': domain,
            'email': email,
            'name': name,  # optional
        }

        return self.send_request(params)

    def remove_subscriber(self, listname, domain, email):
        params = {
            'cmd': 'announcement_list-remove_subscriber',
            'listname': listname,
            'domain': domain,
            'email': email,
        }

        return self.send_request(params)

    def post_announcement(self, listname, domain, subject, message, name, **kwargs):

        params = {
            'cmd': 'announcement_list-post_announcement',
            'listname': listname,
            'domain': domain,
            'subject': subject,  # optional
            'message': message,
            'name': name,
            'stamp': kwargs.get('stamp'),  # optional the time to send the message, like 2009-05-28 19:40:00
            'charset': kwargs.get('charset'),  # optional
            'type': kwargs.get('type'),  # optional, the format of the message, either text or html (optional)
            'duplicate_ok': kwargs.get('duplicate_ok'),  # optional
        }

        return self.send_request(params)

if __name__ == "__main__":
    AnnounceList().enable_http_debug()
    list = AnnounceList()
    print list.test().text
