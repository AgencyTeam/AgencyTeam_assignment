# AgencyTeam_assignment


**통합적으로 사용할 수 있는 Web application 구현**

- Web Application Framework : Flask(+uWSGI)

- Web Server : NGINX

- DB : SQLite3

- DevOps : Docker (ubuntu 20.04)

- UI : Bootstrap (HTML, CSS, JS)



**기능 1 : 발주파일 생성**

    서비스를 통해 들어온 주문 정보가 담긴 Excel 파일을 기반으로 브랜드 발주서 작성에 필요한 정보가 담긴 Excel 파일을 생성
    
    - 각 플랫폼에서 발생한 주문 정보가 담긴 Excel 파일 (input)
    
    - Sheet 내용이 주문 정보와 상품의 가격 정보가 들어있는 두 가지 Sheet 필요
    
    - 추가적인 내용 ex) 주문자 정보, 주문자 전화번호 등 (input)

        • 주문자 이름/번호/주소 등 개인정보
        
        • 주문자 ID 넘버 (신분증-세관용 정보)
        
        • 상품 정보 (SKU넘버, 컬러, 사이즈 등)
        
        • 상품 가격 정보 (정상가, 판매가, 정산가격 등)
        
        • ...

    - input data 를 형식에 맞추어서 브랜드 발주서에 필요한 엑셀 파일로 변환 (output)



**기능 2 : 물류파일 생성**

    서비스를 통해 들어온 주문 정보가 담긴 Excel 파일 기반으로 물류 운송장 작성에 필요한 정보가 담긴 Excel 파일을 생성
    
    - 각 플랫폼에서 발생한 주문 정보가 담긴 Excel 파일 (input)
    
    - 추가적인 내용 ex) 주문자 정보, 주문자 전화번호 등 (input)

        • 주문자 이름/번호/주소 등 개인정보
        
        • 주문자 ID 넘버 (신분증-세관용 정보)
        
        • 상품 정보 (SKU넘버, 컬러, 사이즈 등)
        
        • 상품 가격 정보 (정상가, 판매가, 정산가격 등)
        
        • ...

    - input data 를 형식에 맞추어서 물류 운송장에 필요한 엑셀 파일로 변환 (output)


**기능 3 : 업로드파일 생성**

    - 각 브랜드로 부터 받은 통합된 데이터 포맷의 상품 기본 정보 엑셀 파일 (input)

        • 브랜드명
        
        • 상품코드
        
        • 이미지
        
        • 제품명
        
        • 색상
        
        • 사이즈
        
        • ...

    - 상품 정보가 담긴 엑셀 파일을 각 플랫폼 업로드 시트에 맞춘 엑셀파일로 변환
    
        • 국내 업로드 시트 (output)
        
        • 동남아 업로드 시트 (output)
        
        • 중국 업로드 시트 (output)

**부가 기능**
    
    관리자 로그인 기능
    
    기능 1, 2 에서 추가적인 정보의 default 값 설정 기능

# 서버 실행 방법

**OS : Windows, MacOS, Linux(Ubuntu 20.04)**

**1. docker-compose [NGINX + Flask(+uWSGI)]**

docker-compose.yml 이 있는 경로에서

    # URL에서 localhost 로 접속가능
    
    $ docker-compose up -d --build

**2. Flask 내장 서버 이용**

'transform' 모듈이 있는 경로에서 (./app)

[Linux, MacOS]

    $ export FLASK_APP=transform
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

[Windows cmd]

    > set FLASK_APP=transform
    > set FLASK_ENV=development
    > flask init-db
    > flask run

[Windows PowerShell]

    > $env:FLASK_APP='transform'
    > $env:FLASK_ENV='development'
    > flask init-db
    > flask run

※ flask init-db : DB Clear Command

# 개발 환경 설정 방법

**docker-compose**

    [./app/Dockerfile]
    ...
    ENV FLASK_ENV=production
    ...
    
이 부분을

    [./app/Dockerfile]
    ...
    ENV FLASK_ENV=development
    ...

로 변경 후

    $ docker-compose up -d --build
