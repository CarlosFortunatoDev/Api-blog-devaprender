from requests.auth import HTTPBasicAuth
import requests

# Como consumir APIs com autenticação usando usando Requests
resultado = requests.get('http://localhost:5000/login', auth=('jhonatan', '123456'))
print(resultado.json())

resultado_autores = requests.get(
    'http://localhost:5000/autores', headers={'x-access-token': resultado.json()['token']})
print(resultado_autores)
