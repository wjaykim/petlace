"""places.csv 파일에서 장소에 대한 정보를 추출함."""
import pandas as pd

from petlace.utils import get_file

places = pd.read_csv(get_file("data/places.csv"))
places = places[ places['반려동물 동반 가능정보']=='Y']
places.rename(columns={
    '시설명': 'name',
    '카테고리1': 'category1',
    '카테고리2': 'category2',
    '카테고리3': 'category3',
    '시도 명칭': 'addr1',
    '시군구 명칭': 'addr2',
    '위도': 'lat',
    '경도': 'lon',
    '도로명주소': 'addr',
    '전화번호': 'callNum',
    '홈페이지': 'webSite',
    '운영시간': 'openTime',
    '주차 가능여부': 'parking',
    '입장 가능 동물 크기': 'petSize',
    '반려동물 제한사항': 'petRule',
    '애견 동반 추가 요금': 'extraFee'
}, inplace=True)

places['image_url'] = places['image_url'].fillna('')
places['nmap_url'] = places['nmap_url'].fillna('')
places['addr'] = places['addr'].fillna('')

places_trip = places[places['category2'] == '반려동반여행']
