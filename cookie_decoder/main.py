import os
from file_name import get_uniqune_filename
from base64_decode import decode_base64_to_dict
from base64_encode import base64_encode_dict
from save_file import save_dict_to_file
def extract_parameter(data: dict, parent_key ="" , table: dict = None) -> dict:
    if table is None:
        table = {}
    
    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            extract_parameter(value, full_key, table)
        else:
            table[full_key] = value
    return table

def print_parameter_table(param_table: dict) -> None:
    print(f"{'Parameter':<50} | {'Value'}")
    print("-" * 80)
    for param, value in param_table.items():
        print(f"{param:<50} | {value}")

def set_nested_value(data: dict, path: str, value):
    keys = path.split(".")
    ref = data
    for key in keys[:-1]:
        ref = ref[key]
    ref[keys[-1]] = value
    
if __name__ == "__main__":
    cookie_1=input("Enter cookie 1 base64 encoded string:")
    cookie_2=input("Enter cookie 2 base64 encoded string:")
    
    decode_dict_1=decode_base64_to_dict(cookie_1)
    email=decode_dict_1.get("user", {}).get("email", "default_user")
    filepath=get_uniqune_filename(email)
    save_dict_to_file(decode_dict_1, filepath)
    print(f"saved to {filepath}")
    
    decode_dict_2=decode_base64_to_dict(cookie_2)
    
    email_1=decode_dict_2.get("user", {}).get("email", "default_user")
    filepath=get_uniqune_filename(email_1)
    save_dict_to_file(decode_dict_2, filepath)
    print(f"saved to {filepath}")
    
    table_1 = extract_parameter(decode_dict_1)
    table_2 = extract_parameter(decode_dict_2)
    
    print("Choose the parameter to modify with cookie_1 as the base value:")
    print_parameter_table(table_1)
    
    selected_param=input("Enter the parameter name to modify (Note : enter the parameter with same case as shown above):").strip()

    if selected_param not in table_1:
        print(f"Parameter '{selected_param}' not found in cookie 1.")
    else:
        set_nested_value(
            decode_dict_1,
            selected_param,
            table_2[selected_param]
        )
        encoded_cookie=base64_encode_dict(decode_dict_1)
        print("Re-encoded modified cookie 1:", encoded_cookie)
        
        output = {
            "decoded_cookie": decode_dict_1,
            "cookie_base64": encoded_cookie
        }
        
        filepath_final=get_uniqune_filename(email+"_modified")
        save_dict_to_file(output, filepath_final) 
        