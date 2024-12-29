## 프로젝트 설정
FastAPI 기반으로 백엔드를 구성했습니다. 프로젝트 테스트를 위해 다음과 같은 순서를 따라 환경설정을 진행합니다.

### 1. 가상환경설정
FastAPI를 비롯하여 다른 파이썬 프로젝트와의 충돌을 피하기 위해 가상환경설정을 진행합니다. 맥북 기준으로 진행합니다.
```bash
python -m venv venv
```
다음의 명령어를 통해 가상환경을 실행합니다.
```bash
source venv/bin/activate
```
가상환경을 실행시킨 상태로 둬야 패키지를 설치할 때 별도의 독립공간으로 두게 됩니다.



### 2. 패키지 설치
가상환경을 실행시킨 채로 패키지 설치를 진행합니다. 패키지 매니저 pip를 업데이트합니다.
```bash
python -m pip install --upgrade pip
```


 requirements.txt에 필요한 패키지와 버전들이 있습니다.
```bash
pip install -r requirements.txt
```

### 3. .env 설정
프로젝트는 openai를 사용하고 있습니다. 따라서 .env를 통해 api 키를 설정해야합니다.

다음의 명령어를 통해 .env 파일을 루트 디렉토리에서 생성합니다.
```bash
touch .env
```

.env 파일에 들어가서 api키 설정을 넣습니다.
```
OPENAI_API_KEY=결제된_api_키
```

이후에 프로젝트 작업 가능합니다.

## 프로젝트 실행
### API 서버 실행
다음의 명령어를 통해 프로젝트를 실행할 수 있습니다. `--reload`는 프로젝트에 변경사항이 있을 경우에 자동으로 재실행하는 옵션입니다.
```bash
uvicorn app.main:app --reload
```


### API docs 확인하기
FastAPI는 swagger를 지원합니다. 로컬에서 다음의 주소를 통해 API 문서에 접속하고 테스트까지 진행가능합니다.
```plaintext
http://127.0.0.1:8000/docs
```


## push 하기 전 주의사항
### 패키지 업데이트 하기
개발 중에 패키지를 새로 설치한 경우에 requirement.txt에 해당 사항을 반영해야합니다. 다음의 명령어를 실행함으로써 설치 된 패키지 목록이 업데이트 됩니다.
```bash
pip freeze > requirements.txt
```