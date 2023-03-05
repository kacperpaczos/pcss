FROM python:3.8-slim-buster

WORKDIR /pcss

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /
COPY database.py /

CMD [ "python3", "-m" , "flask", "run", "--host=172.28.0.19"]
