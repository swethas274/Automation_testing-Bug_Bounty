import json
import base64
from jwt_encode import encode_access_token
from typing import Dict, Any

def base64_encode_dict(cookie_dict: Dict[str, Any]) -> str:
    # work on a COPY to avoid mutation bugs
    cookie = json.loads(json.dumps(cookie_dict))

    if "access_token" in cookie:
        # encode JWT → MUST return a string
        encoded_jwt = encode_access_token(cookie["access_token"])

        if not isinstance(encoded_jwt, str):
            raise ValueError("encode_access_token() must return a JWT string")

        cookie["access_token"] = encoded_jwt

    # compact JSON (closer to real cookies)
    json_string = json.dumps(cookie, separators=(",", ":"))

    return base64.b64encode(json_string.encode("utf-8")).decode("utf-8")
