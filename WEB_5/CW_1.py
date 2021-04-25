import requests

s = input()
p = int(input())
a = int(input())
b = int(input())

url = f'{s}:{p}'
par = {
    'a': a,
    'b': b
    }
resp = requests.get(url, params=par)
res = resp.json()
print(sorted(res['result']))
print(res['check'])