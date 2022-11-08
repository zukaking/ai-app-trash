FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY ./docker/python/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install
WORKDIR /app

#ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]