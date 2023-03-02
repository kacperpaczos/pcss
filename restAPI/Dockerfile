FROM python:3

ADD app.py /
ADD database.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install mysql-connector-python

EXPOSE 26379

CMD [ "python", "./app.py" ]
