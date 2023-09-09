"""
This module provides a class for interacting with
the Bored API to retrieve random activities.
"""

import json
import urllib.parse
import urllib.request

# import requests

# For information on how this module works, I recommend visiting:
# https://docs.python-requests.org/en/latest/index.html - request
# https://docs.python.org/3/library/urllib.html - urllib


class BoredApi:
    """A class used to represent the Bored API."""

    def __init__(self):
        """Constructs all the necessary attributes for the BoredApi object."""
        self.base_url = "https://www.boredapi.com/api/activity"

    def get_random_activity(
        self,
        type=None,
        participants=None,
        price_min=None,
        price_max=None,
        accessibility_min=None,
        accessibility_max=None,
    ):
        """Retrieves a random activity from the Bored API with the specified filters."""
        params = {}
        if type:
            params["type"] = type
        if participants:
            params["participants"] = participants
        if price_min:
            params["price_min"] = price_min
        if price_max:
            params["price_max"] = price_max
        if accessibility_min:
            params["accessibility_min"] = accessibility_min
        if accessibility_max:
            params["accessibility_max"] = accessibility_max

        # urllib version
        query_string = urllib.parse.urlencode(params)
        url = self.base_url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())

        # # request version
        # response = requests.get(self.base_url, params=params, timeout=None)

        # return response.json()
