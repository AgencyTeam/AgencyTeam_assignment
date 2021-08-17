```docker
# base-line image
FROM python:3.9.6-buster

# 프로젝트 clone
RUN git clone https://github.com/AgencyTeam/AgencyTeam_assignment.git

# 작업 디렉토리를 /AgencyTeam_assignment 으로 지정
WORKDIR /AgencyTeam_assignment

# pip install 실행
RUN pip install -r requirements.txt

# 이 이미지는 5000번 포트를 외부에 공개할 예정이다
# 이것이 있다고 해도 포트를 매핑시키지 않으면 소용없음.
EXPOSE 5000

# 환경변수 설정
ENV FLASK_APP transform
ENV FLASK_ENV development

# DB 설정
RUN mkdir upload_files
RUN flask init-db

# entrypoint
ENTRYPOINT ["flask"]

# 컨테이너 실행 시 flask run --host 0.0.0.0 실행
CMD ["run", "--host", "0.0.0.0"]
```