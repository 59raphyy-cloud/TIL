# 넷플릭스 주가 데이터 분석


## 1. 프로젝트 개요
- Kaggle에서 제공하는 Netflix 주가 데이터(NFLX.csv)를 활용하여, Pandas를 통한 데이터 전처리 기술을 익히고 Matplotlib로 주가 추이를 시각화하는 연습을 진행했습니다.


## 2. 단계별 구현 과정 및 학습 내용


### 1) 데이터 수집 및 로딩
Kaggle API 대신 직접 .zip 파일을 다운로드하고 압축을 해제하여 로컬 환경에서 데이터를 관리하는 법을 익혔습니다.
- NumPy와 Pandas 라이브러리를 설치하고, 새로운 이름(np, pd)으로 불러옴
    > !pip install numpy

    > import numpy as np
- Pandas의 데이터 프레임 생성
    > columns=arr[0]

    > arr = np.delete(arr, 0, 0)
    
    > df = pd.DataFrame(arr, columns=columns)


### 2) 데이터 전처리
데이터파일[['Date', 'Open', 'High', 'Low', 'Close']]와 같이 필요한 컬럼만 추출했습니다.
- iloc 인덱서 사용
    > df.iloc[:, :5]


### 3) 2021년 이후의 데이터 필터링
문자열로 되어 있는 'Date' 컬럼을 pd.to_datetime() 함수를 사용하여 시계열 데이터로 변환했습니다.  
2021년 이후, 2022년 이후 등 특정 시점 이상의 데이터만 필터링하여 분석 대상을 좁히는 법을 배웠습니다.
- 컬럼을 날짜형으로 변환
    > df['Date'] = pd.to_datetime(df['Date'])
- 데이터 필터링
    > filtered_df = df.query("Date >= '2021-01-01'")
    
    > filtered_df.iloc[:, :5]
    - [LEARNED] 변수에 할당만 한 상태이므로 변수명을 한 번 더 작성해야 결과를 볼 수 있음

plot() 함수를 이용해 종가(Close), 고가(High), 저가(Low)의 변동 추이를 시각화했습니다.
- 데이터를 그래프로 시각화 (matplotlib)
    > x = filtered_df.iloc[:, 0]

    > y = filtered_df.iloc[:, 4]
    
    > y = y.astype(float)
    - [LEARNED] y축 데이터를 실수형으로 변환해야 함
    - 데이터가 문자열이면 크기순이 아니라 데이터에 나타난 순서대로 y축에 나열됨
    

### 4) 최고/최저 종가 추출
- 종가의 최대/최소값 추출
    > max_price = max(filtered_df.iloc[:, 4])

    > min_price = min(filtered_df.iloc[:, 4])


### 5) 월별 평균 종가 계산
.resample('ME').mean()을 활용하여 일별 데이터를 월별 평균 데이터로 그룹화하는 고급 기술을 학습했습니다.
- 5열의 데이터를 수치형으로 변환
    > filtered_df[filtered_df.columns[4]] = filtered_df[filtered_df.columns[4]].astype(float)
    - [LEARNED] df.columns[4]는 열의 이름(문자열)일 뿐이며, 실제 데이터에 접근하려면 df[df.columns[4]]와 같이 호출해야 함
- 월 추출 후 평균 계산
    > filtered_df['Month'] = filtered_df['Date'].dt.to_period('M')
    - [LEARNED] dt.year와 dt.to_period('M')의 차이점
      - 단순 연도 구분 vs 연-월 단위 유지
    > monthly_avg = filtered_df.groupby('Month')[filtered_df.columns[4]].mean()
- 계산 결과를 DataFrame으로 저장하여 그래프로 시각화
    > monthly_df = monthly_avg.reset_index()

    > monthly_df.columns = ['Date', 'Average Close Price']
    - [LEARNED] groupby 이후 인덱스로 설정된 기준 열을 reset_index()를 통해 다시 일반 열로 변환해야 함
    > monthly_df['Date'] = monthly_df['Date'].astype(str)
    - [LEARNED] Date 열 데이터 타입을 Period에서 문자열로 변환해야 함


### 6) 2022년 이후 최고/최저/종가 시각화
plot() 함수를 이용해 종가(Close), 고가(High), 저가(Low)의 변동 추이를 시각화했습니다.
범례를 추가하여 여러 데이터를 한 눈에 비교할 수 있도록 설정했습니다.

    > 데이터 생성

        x = filtered_2022_df.iloc[:, 0]
        y = filtered_2022_df.iloc[:, 2]
        y2 = filtered_2022_df.iloc[:, 3]
        y3 = filtered_2022_df.iloc[:, 4]

    > y축 데이터 수치형으로 변환
    
        y = y.astype(float)
        y2 = y2.astype(float)
        y3 = y3.astype(float)

    > 그래프 그리기
    
        plt.plot(x, y, label='High')
        plt.plot(x, y2, label='Low')
        plt.plot(x, y3, label='Close')

    > 범례 추가
    
        plt.legend()


## 3. 느낀점

1. 장수철
- 어려웠던 점
  - Pandas 문법의 생소함: 기존 Python 리스트 방식과 다른 loc, copy(), resample 등 Pandas만의 고유한 문법과 작동 방식이 처음에는 익숙하지 않아 적응이 필요했습니다.
  - 로컬 파일 경로 관리: API가 아닌 직접 다운로드한 파일을 불러올 때 경로 설정과 파일 관리에 대한 어색함이 있었습니다.
  - 시각화 디테일: 그래프에 라벨을 달고 범례를 적절한 위치에 배치하는 코드를 구성하는 데 시행착오가 있었습니다.
- 느낀점
  - 그동안 파이썬의 기본 리스트만으로는 2차원 표 데이터를 다루는 데 한계가 많아 답답함을 느꼈습니다. 하지만 이번에 Pandas의 데이터프레임을 배우면서 복잡한 연산과 필터링을 단 몇 줄의 코드로 해결할 수 있다는 점이 매우 놀라웠습니다. 2차원 데이터 처리의 한계를 극복한 것 같아 정말 뿌듯합니다.
- 발전할 점
  - 다음에는 코드를 쓸 때 그때그때 주석을 달자.

2. 오규연
   - 단순히 함수를 쓰는 것보다 데이터의 타입을 정확히 관리하는 것이 중요함을 체감했습니다.
   - 매번 터미널을 사용을 해서 데이터를 받아왔는데 이번에 pandas를 사용을 하면서 그래프를 통한 시각화가 데이터 이해에 정말 큰 도움이 된다는 것을 깨달았습니다.
   - GUI가 나오기 이전에 CLI로 텍스트로 코딩을 했다고 했는데, GUI로 화면에 내용이 나오는 것의 편리함을 느꼈습니다.
   - 여러 종목 간의 상관관계 분석을 통해 심화해나가고 싶습니다.

