FROM python:3.10-buster

RUN useradd -ms /bin/bash gotify
USER gotify
WORKDIR /home/gotify/

COPY src/. .

RUN mkdir output && pip install -r requirements.txt

CMD ["python", "receive.py"]