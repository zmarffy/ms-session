import random
import re

import requests
from bs4 import BeautifulSoup

POST_URL_RE = 'urlPost:\\\'([A-Za-z0-9:\?_\-\.&/=]+)'
PPFT_URL_RE = 'sFTTag:\\\'.*value="(.*)"/>'
REQUIRED_LOGIN_POST_KEYS = ("pprid", "t", "NAP", "ANON")
LOGIN_KEY = "https://login.live.com/"


class MSSessionLoginError(Exception):
    pass


class MSSession(requests.Session):

    """Basically a `requests.Session` object that logs you into your Microsoft account

    Args:
        email (str): Account email
        password (str): Account password
    """

    def __init__(self, email: str, password: str) -> None:
        super().__init__()
        self._login(email, password)

    def _login(self, email: str, password: str) -> None:
        """Log into your Microsoft account in the session

        Args:
            email (str): Account email
            password (str): Account password

        Raises:
            MSSessionLoginError: If the login failed in some way
        """
        next_url = LOGIN_KEY
        r = self.get(next_url)

        next_url = re.search(POST_URL_RE, r.text).group(1)
        ppft = re.search(PPFT_URL_RE, r.text).groups(1)[0]
        # This is a thing for some reason
        ppsx = "Passport"[0:random.randrange(9)]
        # Make it super realistic
        time_spent = random.randrange(1000, 15000)

        data = {
            "i13": "0",
            "login": email,
            "loginfmt": email,
            "type": "11",
            "LoginOptions": "3",
            "lrt": None,
            "lrtPartition": None,
            "hisRegion": None,
            "hisScaleUnit": None,
            "passwd": password,
            "ps": "2",
            "psRNGCDefaultType": None,
            "psRNGCEntropy": None,
            "psRNGCSLK": None,
            "canary": None,
            "ctx": None,
            "hpgrequestid": None,
            "PPFT": ppft,
            "PPSX": ppsx,
            "NewUser": "1",
            "FoundMSAs": None,
            "fspost": "0",
            "i21": "0",
            "CookieDisclosure": "0",
            "IsFidoSupported": "1",
            "isSignupPost": "0",
            "i2": "1",
            "i17": "0",
            "i18": None,
            "i19": time_spent
        }
        r = self.post(next_url, data=data, allow_redirects=True)
        if "sErrTxt:'Your account or password is incorrect." in r.text:
            raise MSSessionLoginError(
                None, f"Incorrect creds for {email}")

        s = BeautifulSoup(r.text, "html.parser")

        next_url = s.find(id="fmHF")
        if next_url is None:
            raise MSSessionLoginError(None, "Incorrect creds")
        next_url = next_url.get("action")
        data = {}
        for key in REQUIRED_LOGIN_POST_KEYS:
            value = s.find(id=key)
            if value is None:
                raise MSSessionLoginError(
                    f"{key} value missing from response. Possibly try to manually login to your account, and then try again")
            data[key] = value.get("value")

        r = self.post(next_url, data=data, allow_redirects=True)
