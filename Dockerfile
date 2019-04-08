FROM python:3

WORKDIR /usr/src/app

RUN pip install boto3

COPY /src /usr/src/app

CMD [ "python", "./s3_script.py" ]