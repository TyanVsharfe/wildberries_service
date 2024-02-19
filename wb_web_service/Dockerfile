FROM python:3.11

COPY ../requirements.txt ./app/requirements.txt
COPY ../wb_web_service   ./app/wb_web_service

RUN apt-get update && apt-get install
RUN pip install -r ./app/requirements.txt

ENV PYTHONPATH=./app

EXPOSE 8000

CMD ["python", "-O", "./app/wb_web_service/main.py"]