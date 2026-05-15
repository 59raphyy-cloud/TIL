협업하는 팀원들이나 다른 사용자가 프로젝트를 복사(`git clone`)했을 때, 번거로운 설정 없이 **명령어 몇 줄만으로 똑같이 50개의 카테고리 데이터를 DB에 구축할 수 있도록** 안내하는 `README.md` 가이드라인입니다.

프로젝트 루트 디렉토리의 `README.md` 파일에 추가하거나 참고하여 작성하시면 됩니다.

---

# 📝 README.md (초기 카테고리 데이터 세팅 가이드)

프로젝트를 처음 다운로드(Clone)받았거나 데이터베이스를 초기화한 경우, 서비스 운영에 필요한 표준 관심사 카테고리(50개)를 자동으로 생성하기 위해 아래 단계를 순서대로 진행해 주세요.

## 🚀 시작하기 전 확인 사항

본 프로젝트는 이미지 처리를 위해 `Pillow` 라이브러리를, API 구동을 위해 `djangorestframework`를 사용합니다. 반드시 가상환경을 활성화한 후 의존성 패키지를 먼저 설치해 주세요.

```bash
# 1. 가상환경 활성화 (Windows Git Bash 기준)
$ source venv/Scripts/activate

# 2. 필수 패키지 설치
(venv) $ pip install -r requirements.txt

```

*(※ `requirements.txt`에 `Pillow`와 `djangorestframework`가 포함되어 있어야 합니다.)*

---

## 🛠️ DB 마이그레이션 및 초기 데이터 주입 단계

데이터베이스 설계도를 반영하고, 준비된 Fixture 파일(`initial_categories.json`)을 이용해 마스터 데이터를 DB에 마이그레이션하는 과정입니다.

### 1. 데이터베이스 테이블 생성

장고 모델 구조를 바탕으로 로컬 SQLite 데이터베이스에 테이블을 생성합니다.

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate

```

### 2. 초기 카테고리 데이터(Fixture) 로드

`api/fixtures/initial_categories.json`에 미리 정의된 50개의 대분류/소분류 관심사 데이터를 일괄 주입합니다.

```bash
(venv) $ python manage.py loaddata initial_categories.json

```

> **성공 메시지:** `Installed 50 object(s) from 1 fixture(s)` 문구가 나타나면 정상적으로 카테고리 마스터 데이터가 구축된 것입니다.

---

## 🧪 데이터 정상 주입 확인 방법

데이터가 제대로 들어갔는지 검증하고 싶다면 장고 쉘(Django Shell)을 통해 아래와 같이 확인할 수 있습니다.

```bash
(venv) $ python manage.py shell

```

```python
# 장고 쉘 진입 후 실행
>>> from api.models import Category
>>> Category.objects.count()
50  # 50이 출력되면 정상입니다.

>>> Category.objects.first()
<Category: [IT/기술] 반도체>  # 첫 번째 카테고리가 정상 출력되는지 확인

```

---

## ⚠️ 트러블슈팅 (Troubleshooting)

### Q1. `no such table: api_category` 에러가 발생합니다.

* **원인:** DB에 테이블이 만들어지기 전에 데이터를 넣으려고 시도한 경우입니다.
* **해결:** `loaddata` 명령어를 실행하기 전, 반드시 `python manage.py migrate`를 먼저 실행해 주세요.

### Q2. `parent_category` 관련 비어있는 필드(Non-nullable) 경고 창이 뜹니다.

* **원인:** 기존에 생성된 DB 파일(`db.sqlite3`)이나 과거 마이그레이션 이력이 꼬여서 발생하는 장고의 컬럼 무결성 경고입니다.
* **해결 (초기화):** 로컬 개발 환경이므로 아래 순서대로 리셋 후 재진행하는 것이 가장 확실합니다.
1. 로컬의 `db.sqlite3` 파일을 삭제합니다.
2. `api/migrations/` 폴더 내에서 `__init__.py`를 **제외**한 모든 마이그레이션 파일(예: `0001_initial.py`)을 삭제합니다.
3. 다시 위의 [DB 마이그레이션 및 초기 데이터 주입 단계]를 1번부터 실행합니다.