#모듈 불러오기
########################참고 QGIS 파이썬 콘솔에서 실행하세요 #####################

#QGIS API를 외부에서 실행하려면 설정 및 조건이 매우 까다로움
## 따라서 QGIS를 실행하고 파이썬 콘솔에서 이 스크립트를 실행하세요

from osgeo import gdal
import os

#디렉터리 내의 모든 파일 목록

os.chdir('D:\\GEODATA\\inputRaster')
rasterFiles = os.listdir(os.getcwd())

# 여러 장 한번에 처리하기 반복
for i in range(len(rasterFiles)):
	# i번째 hdf 파일 열기
	os.chdir('D:\\GEODATA\\inputRaster')
	hdfLayer = gdal.Open(rasterFiles[i], gdal.GA_ReadOnly)
	# EVI 래스터 레이어 열기
	rLayer = gdal.Open(hdfLayer.GetSubDatasets()[1][0], gdal.GA_ReadOnly)

	# EVI 래스터 출력 위치/이름 지정
	outputName = rLayer.GetMetadata_Dict()['LOCALGRANULEID'][:-4]+'_EVI.tif'
	outputRaster = '..\\outputRaster\\'+ outputName

	# 워프(재투영)
	gdal.Warp(outputRaster, rLayer, dstSRS='EPSG:4326')

	# EVI 워프(재투영)래스터 레이어 열기
	os.chdir('D:\\GEODATA\\outputRaster')
	input_layer = QgsRasterLayer(outputName, 'raster')

	parameters = {'INPUT_A': input_layer, 'BAND_A': 1, # 래스터 밴드
	    'FORMULA': 'A * 0.0001', # 래스터계산식
	    'RTYPE': 5, # 출력 래스터 유형은 Float32
	    'OUTPUT' : rasterFiles[i][:-4] + '_SF.tif'}

	# 래스터 계산기 실행
	processing.runAndLoadResults('gdal:rastercalculator', parameters)
print('완료!!')