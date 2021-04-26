import requests

def find_spn(address):
    req = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    print(req)
    res = requests.get(req)
    if res:
        js = res.json()
    else:
        raise RuntimeError('Ошибка')
    top = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    coor = top["Point"]["pos"]
    coor = ','.join(coor.split())
    env = top["boundedBy"]["Envelope"]
    s = abs(float(env["lowerCorner"].split(" ")[0]) - float(env["upperCorner"].split(" ")[0])) / 2
    t = abs(float(env["lowerCorner"].split(" ")[1]) - float(env["upperCorner"].split(" ")[1])) / 2
    print(",".join([str(s), str(t)]))
    return coor, ",".join([str(s), str(t)])