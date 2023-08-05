"""
An IndexNow URL submitter for Python.

To submit the pages you need to have a Bing known file at the root of your website.

https://www.indexnow.org/faq
"""

import logging
from typing import List

import requests

logger = logging.getLogger(__name__)


class IndexNow:

    def __init__(self, key: str, host: str):
        self.key = key
        self.host = host

        # HTTP 1.1 keep-alive
        self.session = requests.Session()

    def index(self, urls: List[str]) -> int:
        """
        Index a list of URLs.

        :param urls: A list of URLs to index
        :return: status from IndexNow
        """

        payload = {
            "key": self.key,
            "host": self.host,
            "urlList": list(urls),
            "keyLocation": f"https://{self.host}/{self.key}.txt",
        }

        endpoint = "https://api.indexnow.org/indexnow"
        response = self.session.post(endpoint, json=payload)

        # Handle any error responses
        response.raise_for_status()

        logger.error(f"IndexNow Response: {response.status_code}")

        return  response.status_code
