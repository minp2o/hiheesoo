from django.http import JsonResponse
import numpy as np
import pandas as pd
import os
from django.conf import settings

# CSV 파일 불러오기 및 JSON 반환 함수
def file_open_by_numpy(request):
    # 파일 경로 설정 (BASE_DIR을 사용하여 절대 경로로 지정)
    file_path = os.path.join(settings.BASE_DIR, 'test_data.CSV')
    
    # CSV 파일을 불러와 JSON 형식으로 변환
    try:
        # CSV 파일을 Pandas DataFrame으로 불러오기
        df = pd.read_csv(file_path, encoding='cp949')
        
        # DataFrame을 JSON 형식으로 변환 (리스트 형태로 변환)
        json_data = df.to_dict(orient='records')
        
        # JSON 응답 반환
        return JsonResponse(json_data, safe=False)
    
    except Exception as e:
        # 오류 발생 시 오류 메시지를 JSON으로 반환
        return JsonResponse({'error': str(e)}, status=500)


# 평균 나이에 가장 가까운 10개의 행 선택

def average_ten(request):
    # 파일 경로 설정 (BASE_DIR을 사용하여 절대 경로로 지정)
    file_path = os.path.join(settings.BASE_DIR, 'test_data.CSV')
    
    # CSV 파일을 불러와 JSON 형식으로 변환
    try:
        # CSV 파일을 Pandas DataFrame으로 불러오기
        df = pd.read_csv(file_path, encoding='cp949')
        mean_age = df['나이'].mean()
        df['나이 차이'] = (df['나이'] - mean_age).abs()    # 평균 나이와의 차이 계산
        closest_ages = df.nsmallest(10, '나이 차이')  # 차이가 가장 작은 10개 행 선택
        closest_ages[['이름', '나이', '성별', '직업', '사는곳']]
        # DataFrame을 JSON 형식으로 변환 (리스트 형태로 변환)
        json_data = closest_ages.to_dict(orient='records')
        
        # JSON 응답 반환
        return JsonResponse(json_data, safe=False)
    
    except Exception as e:
        # 오류 발생 시 오류 메시지를 JSON으로 반환
        return JsonResponse({'error': str(e)}, status=500)

    
    