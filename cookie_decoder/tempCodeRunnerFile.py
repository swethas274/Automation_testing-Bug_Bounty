import jwt 
from base64_decode import decode_base64_to_dict
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
        
        cookie_dict["access_token"]={"header": decode_header, "payload": decode_playload}
    except Exception as e:
        cookie_dict["access_token"] = {"error" : f"JWT decode failed: {e}", "original_token": token} 
    
    return cookie_dict

def save_dict_to_file(data:dict, filepath:str) -> None:
    with open (filepath, "w", encoding="utf-8") as f:
        json.dump(data,f,indent=4, ensure_ascii=False)

if __name__=="__main__":
    cookie=input("Enter base64 encoded string: ")
    decode_dict=decode_base64_to_dict(cookie)
    result_dict=decode_access_token(decode_dict)
    # print(result_dict)
    email=decode_dict.get("email", "default_user")
    filepath=get_uniqune_filename(email)
    save_dict_to_file(result_dict, filepath)
    print(f"saved to {filepath}")