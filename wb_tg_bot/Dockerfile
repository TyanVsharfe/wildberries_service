FROM python:3.11

COPY ../requirements.txt ./app/requirements.txt
COPY ../wb_tg_bot        ./app/wb_tg_bot

RUN apt-get update && apt-get install
RUN pip install -r ./app/requirements.txt

ENV PYTHONPATH=./app

EXPOSE 8005

CMD ["python", "-O", "./app/wb_tg_bot/main.py"]