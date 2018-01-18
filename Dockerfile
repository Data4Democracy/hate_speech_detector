FROM python:3.5-slim

WORKDIR ./src

ADD requirements.txt requirements.txt
ADD app ./app/
ADD ./data/twitter-hate-speech2.csv ./data/

ENV TRAINING_DATA_LOCATION data/twitter-hate-speech2.csv

RUN pip install -r requirements.txt

RUN python -m app.training

ENTRYPOINT ["gunicorn","-b", "0.0.0.0:8000", "app.app:app"]