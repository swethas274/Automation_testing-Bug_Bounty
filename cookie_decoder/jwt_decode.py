import jwt # install PyJWT
from typing import Dict, Any
import json
from file_name import get_uniqune_filename
def decode_access_token(cookie_dict: Dict[str, Any]) -> Dict[str,Any]:
    if "access_token" not in cookie_dict:
        raise ValueError("No access_token found in the provided dictionary.")
    
    token =cookie_dict["access_token"]
    
    #basic JWT structure check
    if not isinstance(token, str) or token.count('.') != 2:
        raise ValueError("Invalid JWT token format.")
    
    try:
        decode_playload= jwt.decode(token, options={"verify_signature": False})
        decode_header=jwt.get_unverified_header(token)
        
        cookie_dict["access_token"]={"header": decode_header, "payload": decode_playload, "raw": token}
    except Exception as e:
        cookie_dict["access_token"] = {"error" : f"JWT decode failed: {e}", "original_token": token} 
    
    return cookie_dict

