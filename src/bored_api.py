"""
This module provides a class for interacting with
the Bored API to retrieve random activities.
"""

import json
import urllib.parse
import urllib.request

# For information on how this module works, I recommend visiting:
# https://docs.python.org/3/library/urllib.html


class BoredApi:
    """A class used to represent the Bored API."""

    def __init__(self):
        """Constructs all the necessary attributes for the BoredApi object."""
        self.base_url = "https://www.boredapi.com/api/activity"

    def get_random_activity(self, **kwargs):
        """Retrieves a random activity from the Bored API with the specified filters."""
        params = kwargs

        query_string = urllib.parse.urlencode(params)
        url = self.base_url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
