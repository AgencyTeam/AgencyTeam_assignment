# AgencyTeam_assignment_1

---

- 과제
    1. **디캔트 서비스를 통해 들어온 주문 처리의 경로를 이해하고 정보 처리의 자동화를 위한 방법**
    - problem : 브랜드 발주서와 물류 운송장을 수기로 작성하여 많은 시간이 소요됨.
    - solution : 브랜드 발주서와 물류 운송장 작성의 자동화
    - input : 해외 주문 정보

        • 주문자 이름/번호/주소 등 개인정보
        • 주문자 ID 넘버 (신분증-세관용 정보)
        • 상품 정보 (SKU넘버, 컬러, 사이즈 등)
        • 상품 가격 정보 (정상가, 판매가, 정산가격 등)

    - input data를 형식에 맞추어서 브랜드 발주서에 필요한 데이터 포맷 생성
    - input data를 형식에 맞추어서 물류 운송장에 필요한 데이터 포맷 생성
    1. **디캔트 플랫폼에 상품정보를 등록하기 위한 다채널 플랫폼의 양식 중 정형화된 데이터 포맷을 만들고 이를 자동 기입/추출할 수 있는 방법**
    - problem : Decant 플랫폼에 상품정보를 등록하는 것에 수기로 정보를 입력하여 업로드에 많은 시간이 소요됨.
    - solution : Decant 플랫폼에 상품정보를 등록하는 것의 자동화
    - input 상품 기본 정보

        • 상품명
        • 상품 sku넘버 (스타일넘버)
        • 컬러정보
        • 사이즈정보
        • 가격 정보
        • 원단정보
        • 상품 설명

    - data들을 정형화된 데이터 포맷(JSON, XML 등)으로 정제.
    - 정제된 데이터(상품 업로드를 위한 데이터)들을 대량으로 업로드


---

- 예상 input/output

    **INPUT** 

    - 제공되는 데이터, 제공되지 않더라도 접근할 수 있는 데이터.
    - 상품정보, 주문정보

    **OUTPUT** 

    브랜드 발주서 , 물류 파일 자동 변환 

    상품 텍스트 정보를 통해 상품정보 자동 기입

---

- 용어 정리
    - MD : Merchandiser의 약자. 상품기획을 전문적으로 다루는 사람
    - 풀필먼트 : 물류 전문업체가 판매업체들에게 수수료를 받고 상품의 입고와 보관, 주문, 포장, 출고 등 물류 **일괄 대행 서비스를 제공**하는 것
    - NFT : 대체 불가능한 토큰(Non-Fungible Token)
    - PG : 전자지급결제대행 Payment Gateway
    - commodity : 상품
    - invoice : 송장
    - B2B : Business to Business
    - B2C : Business to Customer

LF알레그리 작업시트 - 물류사로 넘어가는 데이터 포맷

자동화 할 수 있는 아이디어

화요일 목요일 (본사 광화문)

- 과제1

    input 데이터가 (csv, xlsx 등) 엑셀 파일일 경우,

    각 컬럼이 무엇이랑 매칭되는지 찾아내야 함. ex) 발주파일의 '상품코드'와 주문파일의'product model'이랑 매칭됨.

    ['product model', 'vendor product No.', 'product quantity', 'order No.', 'create time', 'customer name', 'customer phone', 'province', 'city', 'area', 'detailed address', 'settle price']

    order No. → 외부몰주문번호,  주문 메모
    'product model' → 상품코드
    'vendor product No. → 오른쪽 3자리 숫자 > 사이즈코드
    'product quantity' →  주문수량
    'create time' → 시간제외 날짜값 > 결제일시
    settle price/67*100 → 실판매가

    소비자가, 배송비 → 마스터파일에서 코드 기준으로 검색.

    - 발주파일
    - 물류파일

- 헤지스 HW List
- 국내 서버용

- 동남아 서버용
