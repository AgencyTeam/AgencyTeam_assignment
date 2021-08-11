# base-line image
FROM python:3.9.6-buster

# 프로젝트 clone
RUN git clone https://github.com/AgencyTeam/AgencyTeam_assignment.git

# 작업 디렉토리를 /AgencyTeam_assignment 으로 지정
WORKDIR /AgencyTeam_assignment

# pip install 실행
RUN pip install -r requirements.txt

# Docker 에게 port 5000을 쓰겠다고 선언
EXPOSE 5000

# 환경변수 설정
ENV FLASK_APP transform
ENV FLASK_ENV development

# DB 설정
RUN flask db-init

# entrypoint
ENTRYPOINT ["flask"]

# 컨테이너 실행 시 flask run --host 0.0.0.0 실행
CMD ["run", "--host", "0.0.0.0"]