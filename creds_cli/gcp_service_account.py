"""Generates credential generation payload to mock GCP service accounts."""
import random
import string
from OpenSSL import crypto

NUMBERS = "0123456789"


class GcpServiceAccount:
    """Creates mock service account features and tokens."""
    def __init__(self):
        self.user_name = "creds-user-" + "".join(random.choices(NUMBERS, k=4))
        self.project_id = "click-creds-" + "".join(random.choices(NUMBERS, k=6))
        self.client_id = "1" + "".join(random.choices(NUMBERS, k=21))
        self.private_key_id = "".join(
            random.choices(NUMBERS + string.ascii_lowercase, k=41)
        )

    def generate_service_account_payload(self):
        """Creates payload for keys for service accounts."""
        return {
            "type": "service_account",
            "project_id": self.project_id,
            "private_key_id": self.private_key_id,
            "private_key": GcpServiceAccount.private_key_generated(),
            "client_email": f"{self.user_name}@{self.project_id}.iam.gserviceaccount.com",
            "client_id": self.client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{self.user_name}%40{self.project_id}.iam.gserviceaccount.com",
        }

    @staticmethod
    def private_key_generated():
        """Creates private key for appearance in payload."""
        private_key = crypto.PKey()
        private_key.generate_key(crypto.TYPE_RSA, 2048)
        return str(crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key))[2:-1]
