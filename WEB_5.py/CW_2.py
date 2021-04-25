import requests
import pygame
import os
from find_spn import find_spn

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = "37.588392,55.734036"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}


response = requests.get(search_api_server, params=search_params)
if not response:
    raise RuntimeError('Ошибка')
json_response = response.json()
organization = json_response["features"][0]
org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
delta = "0.01"
jll, spn = find_spn(org_address)
map_params = {
    "ll": jll,
    "spn": spn,
    "l": "map",
    "pt": ["{0},pm2dgl~{1},pm2dgl".format(jll,address_ll)]
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(response.url)
map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    while pygame.event.wait().type != pygame.QUIT:
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)
except Exception as a:
    print(a)