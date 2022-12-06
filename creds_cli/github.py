"""Module that creates github focused secrets and credentials"""
import random
import uuid
import string

POSSIBLE_CHARS = string.ascii_letters + "0123456789"


class Github:
    """Creates Github token formats with mocked information."""

    def __init__(self):
        self.request_id = str(uuid.uuid4())
        self.user_name = "clickcreds_" + "".join(random.choices("0123456789", k=5))

    def personal_access_token_payload(self):
        """Creates PAT payload token"""
        return {
            "UserName": self.user_name,
            "RequestId": self.request_id,
            "PersonalAccessToken": "ghp_"
            + "".join(random.choices(POSSIBLE_CHARS, k=36)),
        }
