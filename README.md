# BigDataVisualize
빅데이터 시각화 웹 서비스 개발 / Django 프레임워크 / MVT 패턴
===

## 목차
1. 가상 개발환경 만들기 (feat.Django)
2. MVT 패턴에 따라 웹 서비스 개발
-----

### 1. 가상 개발환경 만들기 (feat.Django)
주의) Mac Os 기준

1) 가상 개발환경을 설치할 디렉토리 생성
'''
mkdir dir_name
'''

2) 디렉토리 안에 비어있는 가상 개발환경 생성
cd dir_name
python -m venv venv_name

3) 가상 개발환경 활성화 및 Django 설치
source venv_name/bin/activate
pip install django

4) Django 사용할 프로젝트 디렉토리 생성
django-admin startproject project_dir_name . 
주의) project_dir_name 과 . 사이에 한 칸 공백

5) 서버 구동 및 확인
python3 manage.py runserver



