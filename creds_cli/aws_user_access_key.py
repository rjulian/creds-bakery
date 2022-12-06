""" Utility to mock out payload of creating AWS access keys. """
import datetime
import uuid
import json
import random
import base64
import string

POSSIBLE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
POSSIBLE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ23456"


class AwsAccessKey:
    """Creates AWS access keys with mocked information."""

    def __init__(self):
        self.user_name = "clickcreds_" + "".join(random.choices("0123456789", k=5))
        self.create_date = str(datetime.datetime.utcnow().isoformat()) + "Z"
        self.request_id = str(uuid.uuid4())

    @staticmethod
    def generate_access_key_random():
        """Creates specific format for access_keys, namely 16 random upcase characters."""
        random_start_letter = [random.choice(POSSIBLE_LETTERS)]
        random_suffix_characters = random.choices(POSSIBLE_CHARS, k=15)
        random_characters = random_start_letter + random_suffix_characters
        return "".join(random_characters)

    @staticmethod
    def generate_secret_access_key():
        """Creates specific format for secret keys,
        creating a b64encoded value and return 41 characters."""
        randomness = "".join(random.choices(string.printable, k=300))
        encoded = base64.b64encode(bytes(randomness, "utf-8"))
        encoded_string = encoded.decode("ascii")
        return encoded_string[:41]

    def access_key_payload(self):
        """Creates payload for access key values"""
        return {
            "UserName": self.user_name,
            "AccessKeyId": "AKIA" + AwsAccessKey.generate_access_key_random(),
            "Status": "Active",
            "SecretAccessKey": AwsAccessKey.generate_secret_access_key(),
            "CreateDate": self.create_date,
        }

    def response_metadata_payload(self):
        """Creates payload for respones metadata."""
        return {
            "RequestId": self.request_id,
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": self.request_id,
                "content-type": "text/xml",
                "content-length": "599",
                "date": self.create_date,
            },
            "RetryAttempts": 0,
        }

    def generate_create_aws_access_key_payload(self):
        """Combines payloads to create correct dictionary payload for access key generation."""
        return {
            "AccessKey": self.access_key_payload(),
            "ResponseMetadata": self.response_metadata_payload(),
        }
