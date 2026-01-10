import json
from file_name import get_uniqune_filename
from typing import Dict, Any       
 
def save_dict_to_file(data:dict, filepath:str) -> None:
    with open (filepath, "w", encoding="utf-8") as f:
        json.dump(data,f,indent=4, ensure_ascii=False)
