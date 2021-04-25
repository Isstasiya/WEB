from requests import get, post, delete, put

print(put('http://localhost:5000/api/jobs').json())      #Данных вообще нет
print(put('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'job': 'Заголовок',
                 'team-leader': 1,
                 'work_size': 17,
                 'collaborators': '1, 2'}).json())       #Правильный
print(put('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок',
                 'team-leader': 1,
                 'work_size': 20,
                 'collaborators': '1, 2, 3',
                 'id': "fef"}).json())                   #неверный тип данных
print(put('http://localhost:5000/api/jobs',
           json={'team-leader': 1,
                 'collaborators': '1, 2, 3'}).json())       #Не все поля
print(get('http://localhost:5000/api/jobs').json())         #Все работы