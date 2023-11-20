import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 엑셀 파일들의 경로
excel_files = ['full_brake.xlsx', 'same_dv.xlsx', 'switch_dv.xlsx']

# 레이블 설정
labels = {'full_brake.xlsx': 'Full Brake', 'same_dv.xlsx': 'Same DV', 'switch_dv.xlsx': 'Switch DV'}

# 데이터프레임 초기화
df_list = []

# 엑셀 파일에서 데이터 읽어오기
for excel_file in excel_files:
    df = pd.read_excel(excel_file, header=None, names=['velocity', 'distance', 'rear car'], skiprows=1)
    df['label'] = labels[excel_file]
    df_list.append(df)

# 모든 데이터 프레임을 하나로 합치기
df = pd.concat(df_list, ignore_index=True)

# 'T'와 'F'를 1과 0으로 변환
df['rear car'] = df['rear car'].map({'T': 1, 'F': 0})

# 레이블 매핑
label_mapping = {'Full Brake': 0, 'Same DV': 1, 'Switch DV': 2}
df['label'] = df['label'].map(label_mapping)

# 특징과 레이블 분리
X = df[['velocity', 'distance', 'rear car']]
y = df['label']

# 모델 생성 및 훈련
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 새로운 입력에 대한 예측
new_data = {'velocity': [80],
            'distance': [12],
            'rear car': [1]}  # 'T' for rear car
new_df = pd.DataFrame(new_data)

prediction_prob = model.predict_proba(new_df)
prediction = model.predict(new_df)[0]

# 예측 결과 출력
for i, choice in label_mapping.items():
    print(f'Predicted Probability ({i}): {prediction_prob[0][choice]*100:.2f}%')

# 가장 높은 확률의 선택
highest_probability_label = max(label_mapping, key=lambda k: prediction_prob[0][label_mapping[k]])

print(f'Most Likely Choice: {highest_probability_label}')
