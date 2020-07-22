# BigDataVisualize
   
빅데이터 시각화 웹 서비스 개발 | Django 프레임워크 | MVT 패턴
   
-----
   
## 목차
[1. 가상 개발환경 만들기 (feat.Django)](https://github.com/KaJaeHyeob/BigDataVisualize#1-%EA%B0%80%EC%83%81-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0-featdjango)

[2. 데이터베이스 설치하기 (feat. MySQL)](https://github.com/KaJaeHyeob/BigDataVisualize/blob/master/README.md#2-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-feat-mysql)
   
[3. MVT 패턴에 따라 웹 서비스 개발](https://github.com/KaJaeHyeob/BigDataVisualize#3-mvt-%ED%8C%A8%ED%84%B4%EC%97%90-%EB%94%B0%EB%9D%BC-%EC%9B%B9-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C)
   
-----
   
## 1. 가상 개발환경 만들기 (feat.Django)
주의) Mac OS 기준

### 1) 가상 개발환경을 설치할 디렉토리 생성
```
mkdir dir_name
```
<img width="837" alt="capture1" src="https://user-images.githubusercontent.com/62693219/83730054-7f9acf00-a683-11ea-8b5e-c100ee02335e.png">

### 2) 디렉토리 안에 비어있는 가상 개발환경 생성
```
cd dir_name
python -m venv venv_name
```
<img width="837" alt="capture2" src="https://user-images.githubusercontent.com/62693219/83730063-8295bf80-a683-11ea-9c1f-a033731e2e44.png">

### 3) 가상 개발환경 활성화 및 Django 설치
```
source venv_name/bin/activate
pip install django
```
<img width="837" alt="capture3" src="https://user-images.githubusercontent.com/62693219/83730065-83c6ec80-a683-11ea-846e-a71ccc662e02.png">

### 4) Django 사용할 프로젝트 디렉토리 생성
```
django-admin startproject project_dir_name
```
<img width="837" alt="capture4" src="https://user-images.githubusercontent.com/62693219/83730067-845f8300-a683-11ea-84e4-7c2719d888d2.png">

### 5) 서버 구동 및 확인
```
cd project_dir_name
python3 manage.py runserver
```
<img width="837" alt="capture5" src="https://user-images.githubusercontent.com/62693219/83730069-84f81980-a683-11ea-9e8b-c47d1ba15555.png">

브라우저에서 localhost:8000 접속 시 다음과 같은 화면이 나오면 성공

<img width="1146" alt="capture6" src="https://user-images.githubusercontent.com/62693219/83730071-8590b000-a683-11ea-8429-77a56b97d694.png">

### 6) 애플리케이션 개발 시작
```
python manage.py startapp app_name
```
<img width="837" alt="capture7" src="https://user-images.githubusercontent.com/62693219/83730074-86294680-a683-11ea-9539-b43381998a75.png">

-----

## 2. 데이터베이스 설치하기 (feat. MySQL)
주의) Mac OS 기준. 다양한 데이터베이스로 가능하나 MySQL로 진행. Homebrew 설치는 생략

### 1) 기존 데이터베이스 삭제 (위험! 필요한 경우에만 할 것!)

다양한 데이터베이스를 겪다 보니 종류 및 버전별로 뒤범벅이었다.

어떻게든 지우지 않고 진행하려 했으나, 계속해서 오류가 발생하였고, 일부분 갈아엎기로 했다.

데이터베이스 종류, 버전, 설치방식(brew 설치, dmg파일 설치 등)에 따라 저장경로가 다르기 때문에, 꼼꼼하고 조심스럽게 rm -rf를 진행하였다.

### 2) MySQL 설치
```
brew install mysql
```
<img width="837" alt="capture2_1" src="https://user-images.githubusercontent.com/62693219/83735969-f9cf5180-a68b-11ea-8e3f-de80ed1cc2d1.png">

### 3) MySQL 서비스 시작
```
brew services start mysql
```
<img width="837" alt="capture2_2" src="https://user-images.githubusercontent.com/62693219/83735975-fcca4200-a68b-11ea-8ddf-6dad32dc8c52.png">

### 4) MySQL 접속
첫 접속일 경우, 아래와 같이 접속 후 비밀번호 설정
```
mysql -u root
```
<img width="837" alt="capture2_3" src="https://user-images.githubusercontent.com/62693219/83735978-fdfb6f00-a68b-11ea-83d9-28ea978da1ea.png">

첫 접속이 아닐 경우, 아래와 같이 접속 후 비밀번호 입력
```
mysql -u root -p
```
<img width="837" alt="capture2_4" src="https://user-images.githubusercontent.com/62693219/83735983-fe940580-a68b-11ea-93ce-e26f1b0facdb.png">

새로운 유저를 만들어서 사용하는 것도 가능하지만, 생략하겠다.

### 5) 데이터베이스 생성
```
CREATE DATABASE database_name;
```
<img width="837" alt="capture2_5" src="https://user-images.githubusercontent.com/62693219/83735984-ff2c9c00-a68b-11ea-9e48-d2565e65ec40.png">

### 6) 데이터베이스 조회
```
SHOW DATABASES;
```
<img width="837" alt="capture2_6" src="https://user-images.githubusercontent.com/62693219/83735985-ffc53280-a68b-11ea-9bb0-c374fe98640a.png">

이후 데이터베이스 관련된 모든 작업은 Django 프레임워크의 모델이 자동으로 수행해준다.

이를 위해 settings.py에서 데이터베이스 정보 설정, 터미널에서 마이그레이션 명령어를 통한 테이블 업데이트가 필요하다.

이에 대한 내용은 뒤에서 다시 설명하겠다.

-----

## 3. MVT 패턴에 따라 웹 서비스 개발

### 1) MVT 패턴 구상

#### 모델(Model) : DB 접근 (비즈니스 로직 수행을 가능하게 함)
1. 클라이언트로부터 받은 csv파일을 로컬저장소에 저장
2. 저장한 csv파일의 파일경로를 DB에 저장
3. csv파일의 데이터 시각화 이미지 생성 및 로컬저장소에 저장 (복잡함을 줄이기 위해 모듈로 분할함)
4. 이미지 파일경로를 DB에 저장
5. 템플릿에게 이미지 파일경로 전달

#### 뷰(view) : 모델과 템플릿 상호작용 관리 (HTTP 요청을 받고 알맞은 HTTP 응답을 보냄)
1. HTTP 요청에 따라 알맞은 뷰가 호출됨 (urls.py 통해서 이뤄짐)
2. 뷰는 모델을 사용하여 비즈니스 로직을 수행하고, 클라이언트에게 템플릿을 반환함으로써 HTTP 응답

#### 템플릿(Template) : 동적 웹 페이지 생성 (뷰에서 render() 통해서 클라이언트에게 제공)
1. 클라이언트에게 알맞은 동적 웹 페이지 제공 (csv파일 요청, 이미지 제공)

-----

참고 : [django 공식 홈페이지](https://docs.djangoproject.com/ko/3.0/intro/tutorial01/), [jesse님](https://blog.jesse.kim/post/26)


