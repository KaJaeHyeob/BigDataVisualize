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
   
### 2) 디렉토리 안에 비어있는 가상 개발환경 생성
```
cd dir_name
python -m venv venv_name
```
   
### 3) 가상 개발환경 활성화 및 Django 설치
```
source venv_name/bin/activate
pip install django
```
   
<img width="1236" alt="capture1" src="https://user-images.githubusercontent.com/62693219/82775784-b56dd580-9e83-11ea-8f14-77141e47a23b.png">
   
### 4) Django 사용할 프로젝트 디렉토리 생성
```
django-admin startproject project_dir_name
```
   
### 5) 서버 구동 및 확인
```
cd project_dir_name
python3 manage.py runserver
```
   
<img width="1192" alt="capture2" src="https://user-images.githubusercontent.com/62693219/82775795-bf8fd400-9e83-11ea-8333-b9e0ed4502bb.png">
   
브라우저에서 localhost:8000 접속 시 다음과 같은 화면이 나오면 성공
   
<img width="1146" alt="capture3" src="https://user-images.githubusercontent.com/62693219/82748422-aa139f00-9ddc-11ea-94bb-d56d5c1c3b93.png">

### 6) 애플리케이션 개발 시작
```
python manage.py startapp app_name
```
   
<img width="1236" alt="capture4" src="https://user-images.githubusercontent.com/62693219/82775807-c74f7880-9e83-11ea-82e5-9c158b1f7299.png">
   
-----
   
## 2. MVT 패턴에 따라 웹 서비스 개발
   
### 1) MVT 패턴 구상
모델(Model) : DB 접근 및 비즈니스 로직 수행
* 클라이언트로부터 받은 csv파일을 로컬저장소에 저장
* 저장한 csv파일의 파일경로를 DB에 저장
* csv파일을 

뷰(view) : 모델과 템플릿 상호작용 관리
-> 

템플릿(Templete) : 동적 웹 페이지 생성
-> 

