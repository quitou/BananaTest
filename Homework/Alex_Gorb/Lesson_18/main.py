import requests

URL = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}

def get_all_obj():
    response = requests.get(URL)
    assert response.status_code == 200
    print(response.json())

def get_one_obj(id_obj):
    response = requests.get(f"{URL}/{id_obj}")
    assert response.status_code == 200
    assert response.json()['id'] == str(id_obj)
    print(response.json())

def new_obj():
    body = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
    }
    response = requests.post(URL,json=body,headers=headers)
    assert response.status_code == 200 , 'Status code is incorrect'
    return response.json()['id']

def post_obj():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(URL, json=body, headers=headers)
    assert response.status_code == 200 , 'Status code is incorrect'

def update_obj():
    id_obj = new_obj()
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color" : "black"
        }
    }
    response = requests.put(f"{URL}/{id_obj}",json=body,headers=headers)
    assert response.status_code == 200
    print(response.json())
    assert response.json()['data']['color'] == "black" , 'Error color'
    clear(id_obj)

def clear (id_obj):
    requests.delete(f"{URL}/{id_obj}")

def path_obj():
    obj_id = new_obj()
    body = {
        "name": "Apple MacBook Pro 18",
        "data": {
            "year": 2026,
            "price": 3000,
        }
    }
    response = requests.patch(f"{URL}/{obj_id}",json=body,headers=headers)
    assert response.status_code == 200
    assert response.json()['data']['year'] == 2026 , 'Status year is incorrect'
    assert response.json()['data']['price'] == 3000 , 'Status price is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 18" , 'Status name is incorrect'
    clear(obj_id)


def delete_obj():
    id_obj = new_obj()
    response = requests.delete(f"{URL}/{id_obj}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Object with id = {id_obj} has been deleted."


get_all_obj()
get_one_obj(1)
post_obj()
update_obj()
path_obj()
delete_obj()