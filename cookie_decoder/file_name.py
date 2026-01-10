import os

def get_uniqune_filename(email: str, directory: str=".") -> str:
    base_name=email.replace("@", "_").replace(".","_")+"_user"
    filename= f"{base_name}.json"
    filepath=os.path.join(directory, filename)
    counter = 1
    
    while os.path.exists(filepath):
        filename = f"{base_name}({counter}).json" 
        filepath = os.path.join(directory, filename)
        counter+=1
    return filepath
