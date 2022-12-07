"""Generates data for mocking oracle cloud credentials"""
import string
import random
import uuid

OCID_CHARS = string.ascii_letters + '0123456789'
PRINTABLE_CHARS = OCID_CHARS + '+_:#()<>{};.[]-'

class OracleUserAuthToken:
    """Creates oracle user auth tokens"""
    def __init__(self):
        self.user_email = "clickcreds" + "".join(random.choices("0123456789", k=5)) + "@example.com"
        self.user_name = "clickcreds_" + "".join(random.choices("0123456789", k=5))
        self.ocid = "ocid1.user.oc1..aaaaaaaa" + "".join(random.choices(OCID_CHARS, k=53))
        self.request_id = str(uuid.uuid4())

    def generate_user_auth_token(self):
        """Creates payload with auth token information"""
        return {
            "UserEmail": self.user_email,
            "UserName": self.user_name,
            "OCID": self.ocid,
            "RequestId": self.request_id,
            "AuthToken": "".join(random.choices(PRINTABLE_CHARS, k=21))
        }
