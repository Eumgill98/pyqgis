import processing
from osgeo import gdal
import os

year = 2012 #추출한 해 지정
v = 'C:/Users/ho/Desktop/국립공원 추출 임상도/국립공원별/'#벡터 경로 지정
r = 'C:/20210101_20211229 Terra v.061_sf_evi/SF/' #레스터 경로 지정

#22개의 국립공원 임상도 벡터 이름 리스트
raster_name = ['gaya', 'gyeongju', 'gyeryong', 'naejang', 'dadohae', 'deogyu', 'mudeung', 'byeonsan', 'bukhan', 'seorak', 'sobaek', 'songni', 'odae', 'worak' , 'wolchul', 'halla', 'juwang', 'jiri', 'chiak', 'taebaek', 'taean', 'hallyeo']

#실행
for i in range(22): #22개의 국립공원
    vectorFiles = raster_name[i]+'.shp' #벡터 레스터에서 뽑아 .shp 결합
    for j in range(23): #23의 EVI지도 -> 다른 수인 경우 수정 필수!!!!!!!!!
        os.chdir('C:/20210101_20211229 Terra v.061_sf_evi/SF') #레스터 레이어 경로 불러오기
        rasterFiles = os.listdir(os.getcwd())#모든 레스터 레이어 목록 불러오기
        v_path = v+vectorFiles #벡터레이어 지정
        r_path = r+rasterFiles[j] #레스터 레이어 지정
        
        #파라미터 지정
        #"INPUT = 입력 벡터', 'INPUT_RASTER'=입력 레스터, 'RASTER_BAND':레스터 밴드(디폴트 1), 'COLUMN_PREFIX':출력 접두사(디폴트: '_'), 'STATISTICS':계산할 식 (0 — 개수(Count)1 — 합계(Sum)2 — 평균(Mean)3 — 중간값(Median)4 — 표준 편차(St. dev.)5 — 최소값(Minimum) — 최대값(Maximum)7 — 범위(Range)8 — 희귀값(Minority)9 — 최빈값(Majority)10 — 다양도(Variety)11 — 변동(Variance)), 'OUTPUT': 산출물 저장 경로 및 방식
        parm = {
        'INPUT': v_path ,'INPUT_RASTER':r_path, 'RASTER_BAND':1, 'COLUMN_PREFIX':'_', 'STATISTICS':[0,1,2], 'OUTPUT':'C:/output/'+str(year)+'_'+raster_name[i]+'_'+rasterFiles[j][:-4]+'.csv'}
        
        #구역 통계 실행 
        processing.run("native:zonalstatisticsfb", parm)
    print(raster_name[i]+'의 임상도를 추출완료!!.')
print('-'*50)
print('모든 작업을 완료했습니다.')

