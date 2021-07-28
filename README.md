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

---

- 예상 input/output

    **INPUT** 

    - 제공되는 데이터, 제공되지 않더라도 접근할 수 있는 데이터.
    - 상품정보, 주문정보

    **OUTPUT** 

    브랜드 발주서 , 물류 파일 자동 변환 

    상품 텍스트 정보를 통해 상품정보 자동 기입

---

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
