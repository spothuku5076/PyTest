from urllib.error import HTTPError
import requests
name_dict = {
    1:"Alice",
    2:"Bob",
    3:"Lalit"
}

def get_user_from_db(n):
    return name_dict.get(n)


def get_key_from_db(name):
    for k,v in name_dict.items():
        if v==name:
            return k
    else:
        return -1
    
    
def get_users_from_request():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code==200:
        return response.json()
    
    raise requests.HTTPError