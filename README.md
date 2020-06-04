# BigDataVisualize
   
빅데이터 시각화 웹 서비스 개발 / Django 프레임워크 / MVT 패턴
   
-----
   
## 목차
[1. 가상 개발환경 만들기 (feat.Django)](https://github.com/KaJaeHyeob/BigDataVisualize#1-%EA%B0%80%EC%83%81-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0-featdjango)
   
[2. MVT 패턴에 따라 웹 서비스 개발](https://github.com/KaJaeHyeob/BigDataVisualize#2-mvt-%ED%8C%A8%ED%84%B4%EC%97%90-%EB%94%B0%EB%9D%BC-%EC%9B%B9-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C)
   
-----
   
## 1. 가상 개발환경 만들기 (feat.Django)
주의) Mac OS 기준

### 1) 가상 개발환경을 설치할 디렉토리 생성
```
mkdir dir_name
```
<img width="837" alt="capture1" src="https://user-images.githubusercontent.com/62693219/83730054-7f9acf00-a683-11ea-8b5e-c100ee02335e.png">

##
### 2) 디렉토리 안에 비어있는 가상 개발환경 생성
```
cd dir_name
python -m venv venv_name
```
<img width="837" alt="capture2" src="https://user-images.githubusercontent.com/62693219/83730063-8295bf80-a683-11ea-9c1f-a033731e2e44.png">

##
### 3) 가상 개발환경 활성화 및 Django 설치
```
source venv_name/bin/activate
pip install django
```
<img width="837" alt="capture3" src="https://user-images.githubusercontent.com/62693219/83730065-83c6ec80-a683-11ea-846e-a71ccc662e02.png">

##
### 4) Django 사용할 프로젝트 디렉토리 생성
```
django-admin startproject project_dir_name
```
<img width="837" alt="capture4" src="https://user-images.githubusercontent.com/62693219/83730067-845f8300-a683-11ea-84e4-7c2719d888d2.png">

##
### 5) 서버 구동 및 확인
```
cd project_dir_name
python3 manage.py runserver
```
<img width="837" alt="capture5" src="https://user-images.githubusercontent.com/62693219/83730069-84f81980-a683-11ea-9e8b-c47d1ba15555.png">

브라우저에서 localhost:8000 접속 시 다음과 같은 화면이 나오면 성공

<img width="1146" alt="capture6" src="https://user-images.githubusercontent.com/62693219/83730071-8590b000-a683-11ea-8429-77a56b97d694.png">

##
### 6) 애플리케이션 개발 시작
```
python manage.py startapp app_name
```
<img width="837" alt="capture7" src="https://user-images.githubusercontent.com/62693219/83730074-86294680-a683-11ea-9539-b43381998a75.png">

-----

## 2. MVT 패턴에 따라 웹 서비스 개발

### 1) MVT 패턴 구상

#### 모델(Model) : DB 접근 (비즈니스 로직 수행을 가능하게 함)
1. 클라이언트로부터 받은 csv파일을 로컬저장소에 저장
2. 저장한 csv파일의 파일경로를 DB에 저장
3. csv파일의 데이터 시각화 이미지 생성 및 로컬저장소에 저장
4. 이미지 파일경로를 DB에 저장
5. 템플릿에게 이미지 파일경로 전달

#### 뷰(view) : 모델과 템플릿 상호작용 관리 (HTTP 요청을 받고 알맞은 HTTP 응답을 보냄)
1. HTTP 요청에 따라 알맞은 뷰가 호출됨 (urls.py 통해서 이뤄짐)
2. 뷰는 모델을 사용하여 비즈니스 로직을 수행하고, 클라이언트에게 템플릿을 반환함으로써 HTTP 응답

#### 템플릿(Templete) : 동적 웹 페이지 생성 (뷰에서 render() 통해서 클라이언트에게 제공)
1. csv파일을 안 받은 경우, form을 포함한 동적 웹 페이지 제공
2. csv파일을 받은 경우, 이미지 파일을 포함한 동적 웹 페이지 제공




참고 : [django](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/)


