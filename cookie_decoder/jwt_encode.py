import jwt 
import json 
from typing import Dict, Any, Optional

def encode_access_token(access_token: Dict[str, Any], secret: Optional[str] = None) -> str:
    algo= access_token.get("header", {}).get("alg", "HS256")
    header = access_token.get("header", {})
    payload = access_token.get("payload", {})
    original_jwt = access_token.get("raw")
    
    if not original_jwt:
        raise ValueError("No original JWT token found in the provided dictionary.")
    
    if algo == "none":
        return jwt.encode(payload, key=None, algorithm=None, headers=header)
    
    if algo and algo.startswith("HS"):
        if not secret:
            return original_jwt
        return jwt.encode(payload, key=secret, algorithm=algo, headers=header)
    
    return original_jwt
        