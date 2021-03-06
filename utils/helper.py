import requests

def get_access_token_sikad():
    body = requests.structures.CaseInsensitiveDict()
    body['username'] = 'Haris'
    body['password'] = 'Haris'
    body['grant_type'] = 'password'
    body['client_id'] = 'web'
    url = 'https://apiumkt.civitas.id/access_token'
    return requests.post(url, data=body).json()['access_token']

def get_user_profiles(key):
    data = ''
    headers = requests.structures.CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {get_access_token_sikad()}"
    if('idMahasiswa' in data):
        url = 'https://sihrd.umkt.ac.id/umar/v3/profil/?uniid=' + key
        ws = requests.get(url)
        data = ws.json()
    else:
        url = 'https://apiumkt.civitas.id/v1/mahasiswa/' + key
        ws = requests.get(url, headers=headers)
        data = ws.json()
    return data

def get_prodi():
    data = ''
    headers = requests.structures.CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {get_access_token_sikad()}"
    url = 'https://apiumkt.civitas.id/v1/prodi/'
    ws = requests.get(url, headers=headers)
    data = ws.json()
    return data