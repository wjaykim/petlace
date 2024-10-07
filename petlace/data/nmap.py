import time
import urllib.parse
from pathlib import Path

import requests

from .places import places_trip

places_copy = places_trip.copy()

places_new = places_trip[(places_trip['image_url'] == '') & (places_trip['nmap_url'] == '')]

s = requests.Session()
count = 0
for place in places_new.itertuples():
    try:
        time.sleep(1)
        count += 1
        print(count, '/', len(places_new))

        response = None
        json = None
        query = str(place.addr) + ' ' + str(place.name)
        params = {
            'query': query,
            'type': 'all',
            'searchCoord': '127.02228240000164;37.473752599999386',
            'boundary': '',
        }
        headers = {
            'Accept': '*/*',
            'Referer': 'https://map.naver.com/p/search/' + urllib.parse.quote(query),
            'Host': 'map.naver.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        }
        response = s.get("https://map.naver.com/p/api/search/allSearch", params=params, headers=headers) #verify='/Users/user/Downloads/charles-ssl-proxying-certificate.pem'

        if response.status_code == 503:
            print('503')
            break

        json = response.json()

        nmap_places = json['result']['place']['list']
        nmap_place = nmap_places[0]
        index = place[0]

        image_url = nmap_place['thumUrl']
        places_new.at[index, 'image_url'] = (image_url if image_url is not None else '')
        nmap_url = 'https://map.naver.com/p/entry/place/' + nmap_place['id']
        places_new.at[index, 'nmap_url'] = nmap_url
    except BaseException as e:
        places_copy.drop(index=place[0], inplace=True)
        places_new.drop(index=place[0], inplace=True)
        print(place.name, e)

places_copy.update(places_new)
places_copy.to_csv(str(Path(__file__).resolve().parent) + '/places_new.csv', index=False, encoding='utf-8-sig')
