import base64 
import json 
from jwt_decode import decode_access_token
from typing import Dict, Any

def decode_base64_to_dict(encoded_str: str) -> Dict[str, Any]:
    """Decode a base64-encoded string and parse it as a JSON dictionary."""
    
    try: 
        # fix the missing padding  
        padding = len(encoded_str) % 4
        if padding!=0:
            encoded_str += '=' * (4 - padding)
        
        # decode the base64  
        decode_bytes = base64.b64decode(encoded_str)
        decode_str=decode_bytes.decode("utf-8")
        
        return decode_access_token(json.loads(decode_str))
    
    except Exception as e:
        raise ValueError (f"Base64 decode failed : {e}")
    