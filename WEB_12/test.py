from requests import get, post, delete

print(get('http://localhost:8080/api/v2/users/1').json())
print(get('http://localhost:8080/api/v2/users/-1').json()) ## Неверний айди
print(post('http://localhost:8080/api/v2/users/', json={"surname": "Iss", 
                                               "name": "Stasiya",
                                               "age": 17,
                                               "position": "junior-prog",
                                               "speciality": "pthon-developer",
                                               "address": "School #166",
                                               "email": "stasi@gmail.com",
                                               "hashed_password": "wow20016789"}).json())
print(post('http://localhost:8080/api/v2/users/', json={"surname": "Iss", 
                                               "name": "Stasiya",
                                               "age": 17,
                                               "position": "junior-prog",
                                               "speciality": "pthon-developer"}).json()) ## не все поля
print(post('http://localhost:8080/api/v2/users/').json()) ## полей нет
print(get('http://localhost:8080/api/v2/users').json())
print(delete('http://localhost:8080/api/v2/users/5'))
print(delete('http://localhost:8080/api/v2/users/5')) ## Такого айди нет
print(get('http://localhost:8080/api/v2/users').json())