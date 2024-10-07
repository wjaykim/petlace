from pathlib import Path

import pandas as pd

places = pd.read_csv(str(Path(__file__).resolve().parent) + '/places.csv')
places.rename(columns={
    '시설명': 'name',
    '위도': 'lat',
    '경도': 'lon',
    '시도 명칭': 'addr1',
    '시군구 명칭': 'addr2',
    '카테고리1': 'category1',
    '카테고리2': 'category2',
    '카테고리3': 'category3'
}, inplace=True)

places['image_url'] = places['image_url'].fillna('')
places['nmap_url'] = places['nmap_url'].fillna('')

places_trip = places[places['category2'] == '반려동반여행']
