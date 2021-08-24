# AgencyTeam_assignment

---

**통합적으로 사용할 수 있는 Web application 구현**

- Web Application Framework : Flask(+uwsgi)

- Server : nginx + Oracle Cloud(or AWS EC2)

- DB : Sqlite3

- infra : Docker (ubuntu 20.04)



**과제1 정의**

    디캔트 서비스를 통해 들어온 주문 처리의 경로를 이해하고 정보 처리의 자동화를 위한 방법
    
    - problem : 브랜드 발주서와 물류 운송장을 수기로 작성하여 많은 시간이 소요됨.
    
    - solution : 브랜드 발주서와 물류 운송장 작성의 자동화
    
    - 각 플랫폼에서 발생한 주문 정보가 담긴 엑셀 파일 (input)

        • 주문자 이름/번호/주소 등 개인정보
        
        • 주문자 ID 넘버 (신분증-세관용 정보)
        
        • 상품 정보 (SKU넘버, 컬러, 사이즈 등)
        
        • 상품 가격 정보 (정상가, 판매가, 정산가격 등)
        
        ...

    - input data를 형식에 맞추어서 브랜드 발주서에 필요한 엑셀 파일 생성
    
    - input data를 형식에 맞추어서 물류 운송장에 필요한 엑셀 파일 생성

---

**과제2 정의**

    디캔트 플랫폼에 상품정보를 등록하기 위한 다채널 플랫폼의 양식 중 정형화된 데이터 포맷을 만들고 이를 자동 기입/추출할 수 있는 방법
    
    - problem : Decant 플랫폼에 상품정보를 등록하는 것에 수기로 정보를 입력하여 업로드에 많은 시간이 소요됨.
    
    - solution : Decant 플랫폼에 상품정보를 등록하는 것의 자동화
    
    - 통합된 데이터 포맷의 상품 기본 정보 엑셀 파일 (input)

        • 브랜드명
        
        • 상품코드
        
        • 이미지
        
        • 제품명
        
        • 색상
        
        • 사이즈
        
        ...

    - data가 담긴 엑셀 파일을 각 플랫폼 업로드 시트에 맞춘 엑셀파일로 변환
   
docker-compose 방법 : docker-compose.yml 있는 경로에서 CLI로 'docker-compose up -d --build' 실행하면 됨.

개발 환경 설정 방법 : app 의 Dockerfile 에서 FLASK_ENV=production 을 FLASK_ENV=development 로 수정하면 됨.
