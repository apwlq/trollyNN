import pandas as pd
import random

# 엑셀 파일 생성
excel_file = pd.ExcelWriter('full_brake.xlsx', engine='openpyxl')

# 데이터 프레임 생성
df = pd.DataFrame()

# 난수 발생 함수 (정수)
def generate_random_values():
    return random.randint(0, 50), random.randint(0, 10), random.choice(['F'])  # 풀 브레이크
    # return random.randint(30, 100), random.randint(15, 20), random.choice(['F'])      # 등가속 감속
    # return random.randint(50, 100), random.randint(0, 10), random.choice(['T'])       # 가변 가속감속

# 열의 개수 (10000개)
num_columns = 100

# 열 이름
columns = ['속도', '거리', '뒷차유무']

# 3개의 행에 대해 난수 채우기
for i in range(3):
    data = [generate_random_values() for _ in range(num_columns)]
    df_row = pd.DataFrame(data, columns=columns)
    df = pd.concat([df, df_row], ignore_index=True)

# 데이터프레임을 엑셀 파일에 쓰기
df.to_excel(excel_file, index=False, sheet_name='Sheet1')

# 엑셀 파일 저장
excel_file.save()
